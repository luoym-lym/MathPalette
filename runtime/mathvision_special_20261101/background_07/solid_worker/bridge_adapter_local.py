"""Runtime-only wrapper around the checked-in MathVision Solid bridge.

The formal renderer and schema are imported unchanged. Every baseline must match
the formal PNG before the existing PluginRenderer may apply an annotation.
"""
from pathlib import Path
import copy,json,os,sys

PROJECT=next(p for p in Path(__file__).resolve().parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
TASK=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
for key,name in {'MPLCONFIGDIR':'mpl_cache','TEMP':'temp','TMP':'temp','XDG_CACHE_HOME':'cache'}.items():
    target=TASK/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.path.insert(0,str(PROJECT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(TASK/'bridge_render_tmp')
sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
import matplotlib
import numpy as np
from dataset_tools import mathvision_workbench as bridge
from workbench_io import load_config,pixel_hash,file_hash,canonical_hash,environment_versions,WorkbenchError
from renderer_adapter import scene_png
from render_plugins import PluginRenderer

class RuntimeBridgeAdapter:
    def __init__(self):
        self.branch=PROJECT/'SolidGeometry'
        self.config=load_config()
        self.config['runtime_dir']=str(TASK/'bridge_state')
        self.config['output_dir']=str(TASK/'bridge_outputs')
        self.records={r['id']:r for r in map(json.loads,(self.branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines())}
        self.original_paths={qid:self.branch/r['image'] for qid,r in self.records.items()}
        self.scenes={qid:json.loads((self.branch/r['scene']).read_text(encoding='utf-8-sig')) for qid,r in self.records.items()}

    def scene(self,qid):
        if self.records[qid]['source_dataset']!='MathVision':raise ValueError('Only formal MathVision records are accepted')
        return bridge.build_scene(self.branch,self.records[qid])

    def inspect_question(self,qid):
        capture=self.scene(qid)
        try:
            _,actual=scene_png(capture)
            expected=pixel_hash(self.original_paths[qid])
            if actual!=expected:raise WorkbenchError(f'{qid} dedicated MathVision bridge baseline differs from formal PNG')
            with matplotlib.rc_context(capture.settings):capture.fig.canvas.draw()
            width,height=capture.fig.canvas.get_width_height()
            transform=np.array([[1,0,0],[0,-1,height],[0,0,1]])@capture.ax.transData.get_affine().get_matrix()
            return {'original_pixel_sha256':expected,'objects':copy.deepcopy(capture.objects),'snap_points':copy.deepcopy(capture.snap_points),'xlim':list(capture.ax.get_xlim()),'ylim':list(capture.ax.get_ylim()),'canvas':{'width':width,'height':height,'data_to_pixel':transform.tolist(),'pixel_to_data':np.linalg.inv(transform).tolist(),'coordinate_system':'frozen_projected_2d'},'renderer_mode':'checked_in_MathVision_bridge','isolation':ISOLATION}
        finally:capture.close()

    def frozen_inputs(self,qid):
        record=self.records[qid]
        relatives=[record['image'],record['scene'],record['script'],*record.get('runtime_dependencies',[])]
        if record.get('original_image'):relatives.append(record['original_image'])
        files={str((self.branch/r).relative_to(PROJECT)):file_hash(self.branch/r) for r in sorted(set(relatives))}
        for relative in ['dataset_tools/mathvision_workbench.py','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/workbench/config.json','SolidGeometry/workbench/renderer_adapter.py','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/plugin.schema.json','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/workbench_io.py']:
            files[relative]=file_hash(PROJECT/relative)
        return {'question_record_sha256':canonical_hash(record),'files':files,'environment':environment_versions(),'runtime_adapter_sha256':file_hash(__file__)}

    def render_candidate(self,plugin,output_directory):
        target=Path(output_directory).resolve()
        if not target.is_relative_to((PROJECT/'runtime').resolve()):raise ValueError('Output must be below root runtime/')
        qid=plugin['question_id'];before=self.frozen_inputs(qid);metadata=self.inspect_question(qid)
        renderer=PluginRenderer(self.config,self,{qid:metadata})
        normalized,data,pixels=renderer.render(plugin)
        normalized2,data2,pixels2=renderer.render(plugin)
        if data!=data2 or pixels!=pixels2 or normalized!=normalized2:raise ValueError('Independent redraws differ')
        if self.frozen_inputs(qid)!=before:raise ValueError('Formal inputs changed during runtime rendering')
        target.mkdir(parents=True,exist_ok=False)
        (target/'candidate.png').write_bytes(data)
        (target/'plugin.json').write_text(json.dumps(normalized,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        report={'question_id':qid,'pixel_sha256':pixels,'png_sha256':file_hash(target/'candidate.png'),'baseline_matches_formal':True,'deterministic':True,'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(normalized),'renderer_mode':'checked_in_MathVision_bridge','isolation':ISOLATION,'approval_status':'Unreviewed runtime candidate; no Pass or Collect.'}
        (target/'render_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (target/'context.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return report


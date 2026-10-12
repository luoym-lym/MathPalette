"""Pure preparation of formal files; never grants approval or writes files."""
from pathlib import Path
import json,os,re

def wrapper(row,qid,runtime_relative,scene_relative,root_relative,candidate=False):
 fields={k:row[k] for k in ['source_dataset','question','answer','answer_type','subject']};fields['id']=qid
 if 'choices' in row:fields['choices']=row['choices']
 return f'''"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/{runtime_relative!r})
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize({row['renderer_family']!r},fig,destination)
def build_scene():
    return _runtime().build_scene({row['renderer_family']!r},ROOT/{scene_relative!r})
class {qid}:
    def __init__(self):
        self.__dict__.update({fields!r})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/{scene_relative!r}
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/{root_relative!r}/".runtime"/"mathverse_redraw"/{(qid+'.png')!r}).resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/{runtime_relative!r})
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw({row['renderer_family']!r}, self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print({qid}().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
'''

def prepare(root,row,formal_id):
 root=Path(root);package=root/'review_candidates/mathverse';branch=row['subject']
 expected_prefix={'PlaneGeometry':'Plane','SolidGeometry':'Solid','Analytics':'Ana'}[branch]
 if not re.fullmatch(expected_prefix+r'(?:0[1-9]|[1-9][0-9]+)',formal_id):raise ValueError('Formal ID must match its branch and positive canonical number')
 prefix={'PlaneGeometry':'plane','SolidGeometry':'solid','Analytics':'function'}[branch];number=''.join(c for c in formal_id if c.isdigit())
 script=f'dataset_generator/{"questions/" if branch=="Analytics" else ""}{prefix}_plot{number}.py'
 formal={k:row[k] for k in ['source_dataset','source_key','question','answer','answer_type']};formal['id']=formal_id
 if 'choices' in row:formal['choices']=row['choices']
 formal['renderer_family']=row['renderer_family']
 formal.update(image=f'image/{formal_id}.png',original_image=f'originals/{formal_id}.png',scene=f'dataset_generator/scenes/{formal_id}.json',script=script)
 writes={f'{branch}/{formal[k]}':(root/row[k]).read_bytes() for k in ['image','original_image']}
 scene=json.loads((root/row['scene']).read_text());source_notes=json.loads((root/row['provenance']).read_text());source_notes['verification']=json.loads((root/row['verification']).read_text());source_notes['source_key']=row['source_key'];source_notes['candidate_id']=row['id'];source_notes['renderer_family']=row['renderer_family']
 if branch!='Analytics':
  from dataset_tools.catalog import FORMAL_SCENE_FIELDS
  allowed=FORMAL_SCENE_FIELDS[branch];extra={k:v for k,v in scene.items() if k not in allowed}
  if extra:source_notes['geometry_notes']={'additional_model_evidence':extra}
  scene={k:v for k,v in scene.items() if k in allowed}
  assert set(scene)==allowed
 scene['id']=formal_id;scene['status']='user_approved';scene['source_image']=f'../../originals/{formal_id}.png';scene['source_dataset']='MathVerse'
 writes[f'{branch}/{formal["scene"]}']=(json.dumps(scene,ensure_ascii=False,indent=2)+'\n').encode()
 helper=f'{branch}/dataset_generator/mathverse_renderers'
 for file in (package/'shared'/row['renderer_family']).iterdir():
  if file.is_file():writes[f'{helper}/{row["renderer_family"]}/{file.name}']=file.read_bytes()
 writes[f'{helper}/runtime.py']=(package/'shared/runtime.py').read_bytes()
 formal['runtime_dependencies']=sorted(p[len(branch)+1:] for p in writes if p.startswith(helper+'/'))
 base=Path(branch)/script
 writes[str(base)]=wrapper(row,formal_id,os.path.relpath(helper+'/runtime.py',base.parent),os.path.relpath(branch+'/'+formal['scene'],base.parent),os.path.relpath('.',base.parent)).encode()
 return formal,writes,source_notes

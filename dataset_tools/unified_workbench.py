"""Workbench binding for the same protocol classes used by ordinary redraws."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace
import copy
import hashlib
import importlib.util
import io
import json
import threading

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from PIL import Image

RENDER_LOCK=threading.RLock()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def pixel_hash(data):
    source=io.BytesIO(data) if isinstance(data,bytes) else data
    if isinstance(source,Image.Image):
        image=source.convert('RGBA')
    else:
        with Image.open(source) as im:
            image=im.convert('RGBA')
    prefix=f'{image.width}x{image.height}:RGBA:'.encode('ascii')
    return hashlib.sha256(prefix+image.tobytes()).hexdigest()


@dataclass
class Scene:
    fig: object
    ax: object
    objects: list
    artists: dict
    snap_points: list
    settings: dict

    def close(self):
        plt.close(self.fig)


def scene_png(scene):
    stream=io.BytesIO()
    with RENDER_LOCK,matplotlib.rc_context(scene.settings):
        scene.fig.savefig(stream,format='png',dpi=100,facecolor='white',transparent=False,
                          bbox_inches=None,pad_inches=0)
    data=stream.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size!=(768,768) or image.convert('RGBA').getextrema()[3]!=(255,255):
            raise ValueError('Expected an opaque 768x768 PNG')
    return data,pixel_hash(data)


class RendererAdapter:
    def __init__(self,config,expected_manifest=None):
        from workbench_io import WorkbenchError,environment_versions
        self.error=WorkbenchError
        self.config=config
        dataset=Path(config['dataset_file']).resolve()
        self.branch_root=self.branch=dataset.parent
        self.project=self.branch_root.parent
        self.branch_name=self.branch_root.name
        from dataset_tools.catalog import assert_formal_dataset
        assert_formal_dataset(dataset)
        rows=[json.loads(line) for line in dataset.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        if any(r.get('drawing_protocol_version')!='2.0.0' for r in rows):
            raise WorkbenchError('Use the complete unified drawing dataset',409,'baseline_changed')
        self.records={r['id']:r for r in rows}
        self.original_paths={q:self.branch_root/r['image'] for q,r in self.records.items()}
        self.source_paths={q:self.branch_root/r['script'] for q,r in self.records.items()}
        self.source_files=list(self.source_paths.values())
        self.scene_paths={q:self.branch_root/r['scene'] for q,r in self.records.items() if r.get('scene')}
        self.sources={q:{'source_file':str(self.source_paths[q]),'source_class':q,
                         'source_dataset':r['source_dataset'],'branch':self.branch_name,
                         'protocol_version':'2.0.0'} for q,r in self.records.items()}
        shared=self.project/'dataset_tools'
        self.input_files={'dataset.jsonl':dataset,
                          'common_renderer.py':Path(config['common_renderer_file']),
                          'protocol.json':Path(config['protocol_file']),
                          'drawing.py':shared/'drawing.py','unified_workbench.py':shared/'unified_workbench.py',
                          'geometry_dataset.py':shared/'geometry_dataset.py',
                          'drawing_board.py':shared/'drawing_board.py'}
        self.context_paths={}
        for q,row in self.records.items():
            context=self.branch_root/'dataset_generator/contexts'/(q+'.json')
            self.context_paths[q]=context
            self.input_files.update({f'image/{q}.png':self.original_paths[q],
                                     f'question_classes/{self.source_paths[q].name}':self.source_paths[q],
                                     f'contexts/{q}.json':context})
            if q in self.scene_paths:
                self.input_files[f'scenes/{q}.json']=self.scene_paths[q]
        self.environment=environment_versions()
        self.manifest=self.make_manifest()
        if expected_manifest and expected_manifest!=self.manifest:
            raise WorkbenchError('Frozen drawing inputs changed',409,'baseline_changed')
        self.renderer=SimpleNamespace(FONT_FAMILY='DejaVu Sans',DPI=100,FIGSIZE=(7.68,7.68))

    def make_manifest(self):
        values={'files':{name:file_hash(path) for name,path in sorted(self.input_files.items())},
                'environment':self.environment}
        return {**values,'fingerprint':canonical_hash(values)}

    def assert_baseline(self):
        if self.make_manifest()!=self.manifest:
            raise self.error('Drawing inputs changed; restart the workbench',409,'baseline_changed')

    def dependencies(self,qid):
        row=self.records[qid]
        values=['common_renderer.py','protocol.json','drawing.py','unified_workbench.py','geometry_dataset.py','drawing_board.py',
                f'image/{qid}.png',f'question_classes/{Path(row["script"]).name}',f'contexts/{qid}.json']
        if row.get('scene'):
            values.append(f'scenes/{qid}.json')
        return tuple(values)

    question_dependencies=dependencies

    @lru_cache(maxsize=16)
    def _class(self,qid,fingerprint):
        spec=importlib.util.spec_from_file_location('_unified_'+qid+'_'+fingerprint[:12],self.source_paths[qid])
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module,qid)

    def scene(self,qid):
        if qid not in self.records:
            raise self.error('Unknown question',404)
        with RENDER_LOCK:
            source=self.source_paths[qid]
            question=self._class(qid,file_hash(source))()
            canvas=question.draw(_canvas=True)
            context=read(self.context_paths[qid])
            artists={}
            for oid,refs in context['aliases'].items():
                try:
                    actual=[canvas.artists[name][index] for name,index in refs]
                except (KeyError,IndexError):
                    raise self.error('Unified object binding changed: '+oid,409,'object_changed')
                if self.branch_name=='Analytics':
                    if actual:
                        artists[oid]=actual[0]
                else:
                    artists[oid]=actual
            return Scene(canvas.fig,canvas.ax,copy.deepcopy(context['objects']),artists,
                         copy.deepcopy(context['snap_points']),canvas.settings)

    def inspect_question(self,qid):
        context=read(self.context_paths[qid])
        with RENDER_LOCK:
            scene=self.scene(qid)
            try:
                _,digest=scene_png(scene)
                if (digest!=context['render_pixel_sha256'] or
                        file_hash(self.original_paths[qid])!=context['source_png_sha256']):
                    raise self.error('Frozen original or unified redraw changed: '+qid,409,'baseline_mismatch')
                if self.branch_name=='Analytics':
                    canvas={}
                else:
                    from drawing_board import describe_captured_scene
                    canvas=describe_captured_scene(scene,qid)
                return {'original_pixel_sha256':digest,'source_pixel_sha256':context['source_pixel_sha256'],
                        'source_pixels_match':digest==context['source_pixel_sha256'],
                        'objects':scene.objects,'snap_points':scene.snap_points,'canvas':canvas}
            finally:
                scene.close()

    def highlight(self,qid,oid):
        with RENDER_LOCK:
            scene=self.scene(qid)
            try:
                if oid not in scene.artists:
                    raise self.error('Unknown drawing object',404)
                value=scene.artists[oid]
                for artist in value if isinstance(value,list) else [value]:
                    if isinstance(artist,Patch):
                        artist.set_edgecolor('#E11D48')
                    else:
                        artist.set_color('#E11D48')
                    artist.set_linewidth(3)
                scene.fig.text(.02,.98,f'REFERENCE ONLY: {qid} / {oid}',color='#E11D48',fontsize=11,va='top')
                return scene_png(scene)[0]
            finally:
                scene.close()

    def is_native(self,qid):
        return False

    is_author=is_native
    is_expand24=is_native
    is_extensions95=is_native

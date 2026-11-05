"""Data-driven renderer. Importing this module creates no files or figures."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent


def render(scene_file, output, svg=None):
    # Direct invocation has the same task-local cache policy as safe_run.py.
    cache = HERE.parent / '_cache'
    for key, folder in [('MPLCONFIGDIR', cache/'matplotlib'),
                        ('TEMP', cache/'tmp'), ('TMP', cache/'tmp')]:
        os.environ.setdefault(key, str(folder))
        Path(os.environ[key]).mkdir(parents=True, exist_ok=True)
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    sys.dont_write_bytecode = True
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch
    from matplotlib import ft2font
    import numpy as np
    import PIL
    from PIL import Image

    scene = json.loads(scene_file.read_text(encoding='utf-8'))
    output.parent.mkdir(parents=True, exist_ok=True)
    rc = {'font.family': 'DejaVu Sans', 'font.size': 16,
          'svg.fonttype': 'path', 'svg.hashsalt': 'Plane236-author-originals',
          'path.simplify': False, 'lines.antialiased': True}
    with matplotlib.rc_context(rc):
        fig = plt.figure(figsize=(7.68,7.68), dpi=100, facecolor='white')
        ax = fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set_xlim(scene['view']['xlim'])
        ax.set_ylim(scene['view']['ylim'])
        ax.set_aspect('equal', adjustable='box')
        ax.set_autoscale_on(False)
        ax.axis('off')
        points = scene['points']
        artists = []
        for obj in scene['objects']:
            xy = [points[p] for p in obj['points']]
            if obj['type'] == 'segment':
                artist, = ax.plot([p[0] for p in xy], [p[1] for p in xy],
                    color=obj.get('color','#000000'), linewidth=1,
                    linestyle=(0,(4,3)) if obj.get('linestyle')=='dashed' else '-',
                    solid_capstyle='round', dash_capstyle='butt',
                    zorder=1 if obj['role']=='grid_guide' else 3,
                    antialiased=True)
            elif obj['type'] == 'arrow':
                artist = FancyArrowPatch(xy[0],xy[1],arrowstyle='-|>',
                    mutation_scale=12,linewidth=1,color='#000000',
                    shrinkA=0,shrinkB=0,zorder=4)
                ax.add_patch(artist)
            else:
                raise ValueError(f"Unsupported object: {obj['type']}")
            artist.set_gid(obj['id'])
            artists.append(artist)
        for label in scene['labels']:
            artist = ax.annotate(label['text'], points[label['point']],
                xytext=label['offset_pt'],textcoords='offset points',
                fontsize=18,fontfamily='DejaVu Sans',fontstyle='normal',
                color='black',ha='center',va='center',clip_on=False,zorder=5)
            artist.set_gid(label['id'])
            artists.append(artist)
        fig.savefig(output,dpi=100,facecolor='white',transparent=False,
                    bbox_inches=None,metadata={'Software':'Plane236 staged author renderer'})
        if svg:
            svg.parent.mkdir(parents=True,exist_ok=True)
            fig.savefig(svg,format='svg',facecolor='white',transparent=False,
                        bbox_inches=None,metadata={'Date':None,'Creator':'Plane236 staged author renderer'})
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        extents = {a.get_gid():list(map(float,a.get_window_extent(renderer).bounds)) for a in artists}
        plt.close(fig)
    rgba = np.asarray(Image.open(output).convert('RGBA'))
    yy,xx = np.where(np.any(rgba[:,:,:3] < 245,axis=2))
    bbox = [int(xx.min()),int(yy.min()),int(xx.max()),int(yy.max())]
    sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
    record = {'process_id':os.getpid(),'utc':datetime.now(timezone.utc).isoformat(),
        'command':sys.argv,'scene':scene_file.name,'output':str(output.relative_to(HERE)),
        'size_px':[int(rgba.shape[1]),int(rgba.shape[0])],
        'opaque':bool(np.all(rgba[:,:,3]==255)),
        'png_sha256':sha(output),'rgba_sha256':hashlib.sha256(rgba.tobytes()).hexdigest(),
        'scene_sha256':sha(scene_file),'renderer_sha256':sha(__file__),
        'content_bbox_px':bbox,'artist_extents_bottom_origin_px':extents,
        'dependencies':{'python':platform.python_version(),'matplotlib':matplotlib.__version__,
            'numpy':np.__version__,'Pillow':PIL.__version__,'freetype':ft2font.__freetype_version__},
        'environment':{k:os.environ.get(k) for k in ['PYTHONDONTWRITEBYTECODE','MPLCONFIGDIR','TEMP','TMP']}}
    output.with_suffix('.render.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:record[k] for k in ['process_id','output','rgba_sha256','content_bbox_px']}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='baseline.png')
    parser.add_argument('--svg')
    args = parser.parse_args()
    path = lambda v: (HERE/v).resolve() if v else None
    render(HERE/'scene.json',path(args.output),path(args.svg))


if __name__ == '__main__':
    main()

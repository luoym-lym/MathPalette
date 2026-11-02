"""Read-only adapter for the existing dedicated Solid MathVision bridge.

Only the adapter interface is provided here. Geometry construction and Special
operations are the existing library implementations, with exact PNG guards.
"""
import copy
import json
from pathlib import Path

import matplotlib
import numpy as np

from dataset_tools import mathvision_workbench as bridge
from dataset_tools.catalog import assert_formal_dataset
from renderer_adapter import scene_png
from workbench_io import WorkbenchError, pixel_hash


class RendererAdapter:
    def __init__(self, config):
        self.config=config
        dataset=Path(config['dataset_file']).resolve()
        self.branch=dataset.parent
        assert_formal_dataset(dataset)
        self.records={r['id']:r for r in map(json.loads,dataset.read_text(encoding='utf-8-sig').splitlines())}
        self.original_paths={qid:self.branch/r['image'] for qid,r in self.records.items()}

    def scene(self,qid):
        record=self.records[qid]
        if record['source_dataset']!='MathVision':
            raise ValueError('Dedicated bridge only accepts formal MathVision records')
        return bridge.build_scene(self.branch,record)

    def inspect_question(self,qid):
        capture=self.scene(qid)
        try:
            _,actual=scene_png(capture)
            expected=pixel_hash(self.original_paths[qid])
            if actual!=expected:
                raise WorkbenchError(f'{qid} dedicated bridge no-op pixels differ from formal PNG')
            with matplotlib.rc_context(capture.settings):
                capture.fig.canvas.draw()
            width,height=capture.fig.canvas.get_width_height()
            transform=np.array([[1,0,0],[0,-1,height],[0,0,1]])@capture.ax.transData.get_affine().get_matrix()
            return {'original_pixel_sha256':expected,'objects':copy.deepcopy(capture.objects),
                    'snap_points':copy.deepcopy(capture.snap_points),'xlim':list(capture.ax.get_xlim()),
                    'ylim':list(capture.ax.get_ylim()),'canvas':{'width':width,'height':height,
                    'data_to_pixel':transform.tolist(),'pixel_to_data':np.linalg.inv(transform).tolist(),
                    'coordinate_system':'frozen_projected_2d'},'renderer_mode':'checked_in_MathVision_bridge'}
        finally:
            capture.close()

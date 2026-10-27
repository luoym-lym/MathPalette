"""Scoped fill-edge rasterization: disable polygon AA to prevent false white mesh seams.
Native geometry, protocol validation, stroke AA, fonts and colors unchanged.
"""
import common_renderer as R

def install():
 if getattr(R.render_scene,'_upper_fill_patch',False):return
 old=R.render_scene
 def render(*args,**kwargs):
  fig,checks=old(*args,**kwargs)
  for ax in fig.axes:
   for patch in ax.patches:patch.set_antialiased(False)
  return fig,checks
 render._upper_fill_patch=True
 R.render_scene=render

#

import bpy

bpy.context.scene.render.engine = 'BLENDER_RENDER'
for material in bpy.data.materials:
    material.use_nodes = False
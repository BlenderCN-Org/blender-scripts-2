#

import bpy
bpy.context.scene.render.engine = 'CYCLES'
for material in bpy.data.materials:
    material.use_nodes = True
import bpy
op = bpy.context.active_operator

op.filepath = 'Y:\\mozvr\\work\\a-saturday-night\\assets\\avatar1\\_avatar1.dae'
op.apply_modifiers = True
op.export_mesh_type = 0
op.export_mesh_type_selection = 'view'
op.selected = True
op.include_children = False
op.include_armatures = False
op.include_shapekeys = True
op.deform_bones_only = False
op.active_uv_only = True
op.include_uv_textures = False
op.include_material_textures = True
op.use_texture_copies = True
op.triangulate = True
op.use_object_instantiation = True
op.use_blender_profile = False
op.sort_by_name = False
op.export_transformation_type = 0
op.export_transformation_type_selection = 'matrix'
op.open_sim = False

import bpy

decimals = 0
scale = 1000

obj = bpy.context.active_object.data
verts = []
faces = []
for v in obj.vertices:
    x = round(v.co.x * scale, decimals)
    y = round(v.co.z * scale, decimals)
    z = round(-v.co.y * scale, decimals)
    if decimals == 0:
        x = int(x)
        y = int(y)
        z = int(z)
    verts.append(str(x))
    verts.append(str(y))
    verts.append(str(z))

	
for f in obj.polygons:
	for v in f.vertices:
	    faces.append(str(v))

print()
print(obj.name)
print()
print('vertices: ['+','.join(verts)+'],')
print('faces: ['+','.join(faces)+']')

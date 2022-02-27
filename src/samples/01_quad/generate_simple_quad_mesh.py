from meshgen.quadmesh import QuadMesh
from meshgen.vector import Vector3

mesh_filename = 'proceduralmesh.stl'

def generate_simple_quad():
    quad = QuadMesh()
    quad.direction1 = Vector3(0.0,1.3,4.5)
    quad.direction2 = Vector3(4.5, 2.3, 0.0)

    quad.create().create_mesh().save(mesh_filename)


if __name__ == '__main__':
	generate_simple_quad()

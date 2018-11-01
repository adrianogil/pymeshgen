from meshbuilder import MeshBuilder
from vector import Vector3

mesh_builder = MeshBuilder()

mesh_builder.add_quad(Vector3(0.0,1.3,4.5), Vector3(4.5, 2.3, 0.0))
quad =  mesh_builder.create_mesh()

quad.save('proceduralmesh.stl')
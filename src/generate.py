from meshbuilder import MeshBuilder
from vector import Vector3

from circlemesh import CircleMesh



def generate_simple_quad():
    mesh_builder = MeshBuilder()
    mesh_builder.add_quad(Vector3(0.0,1.3,4.5), Vector3(4.5, 2.3, 0.0))
    quad =  mesh_builder.create_mesh()

    quad.save('proceduralmesh.stl')


circle_mesh = CircleMesh()
mesh_builder = circle_mesh.create()
mesh_builder.create_mesh().save('proceduralmesh.stl')
from meshgen.meshbuilder import MeshBuilder
from meshgen.vector import Vector3

from meshgen.circlemesh import CircleMesh
from meshgen.cylindermesh import CylinderMesh
from meshgen.conemesh import ConeMesh
from meshgen.quadmesh import QuadMesh

from meshgen.parallelepipedmesh import ParallelepipedMesh

from meshgen.castletowermesh import CastleTowerMesh
from meshgen.castlemesh import CastleMesh

mesh_filename = 'proceduralmesh.stl'

def generate_simple_quad():
    quad = QuadMesh()
    quad.direction1 = Vector3(0.0,1.3,4.5)
    quad.direction2 = Vector3(4.5, 2.3, 0.0)

    quad.create().create_mesh().save(mesh_filename)

def generate_parallepiped():
    mesh = ParallelepipedMesh()
    mesh.direction1 = Vector3(0.0,1.3,4.5)
    mesh.direction2 = Vector3(4.5, 2.3, 0.0)
    mesh.direction3 = mesh.direction1.cross_product(mesh.direction2)

    mesh.create().create_mesh().save(mesh_filename)

def generate_circles():
    circle_mesh = CircleMesh()
    circle_mesh.direction1 = Vector3.forward()
    mesh_builder = circle_mesh.create()

    circle_mesh.radius = 3
    mesh_builder2 = circle_mesh.create()
    mesh_builder2.translate(Vector3.up().multiply(2))

    mesh_builder = mesh_builder.join(mesh_builder2)

    mesh_builder.create_mesh().save(mesh_filename)

def generate_cylinder():
    cylinder_mesh = CylinderMesh()
    mesh_builder = cylinder_mesh.create()
    mesh_builder.create_mesh().save(mesh_filename)

def generate_cone():
    ConeMesh().create().create_mesh().save(mesh_filename)

def generate_castle_tower():
    CastleTowerMesh().create().create_mesh().save(mesh_filename)

def generate_castle():
    CastleMesh().create().create_mesh().save(mesh_filename)

generate_castle()
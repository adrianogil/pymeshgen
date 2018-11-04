from meshbuilder import MeshBuilder
from vector import Vector3

from circlemesh import CircleMesh
from cylindermesh import CylinderMesh
from conemesh import ConeMesh
from quadmesh import QuadMesh

from castletowermesh import CastleTowerMesh

mesh_filename = 'proceduralmesh.stl'

def generate_simple_quad():
    quad = QuadMesh()
    quad.direction1 = Vector3(0.0,1.3,4.5)
    quad.direction2 = Vector3(4.5, 2.3, 0.0)

    quad.create().create_mesh().save(mesh_filename)

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

def generate_castle():
    CastleTowerMesh().create().create_mesh().save(mesh_filename)

# generate_castle()
generate_simple_quad()
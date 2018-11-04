
from vector import Vector3

from meshbuilder import MeshBuilder
from quadmesh import QuadMesh

class ParallelepipedMesh:
    def __init__(self):
        self.size1 = 3
        self.size2 = 3
        self.size3 = 3
        self.origin = Vector3.zero()
        self.direction1 = Vector3.forward()
        self.direction2 = Vector3.right()
        self.direction3 = Vector3.up()
        self.segments_dir1 = 10
        self.segments_dir2 = 10
        self.segments_dir3 = 10

    def create(self):
        mesh_builder = MeshBuilder()

        quad = QuadMesh()
        quad.origin = self.origin

        quad.direction1 = self.direction1
        quad.direction2 = self.direction2
        quad.segments_dir1 = self.segments_dir1
        quad.segments_dir2 = self.segments_dir2

        mesh_builder = quad.create()

        quad.direction1 = self.direction1
        quad.direction2 = self.direction3
        quad.segments_dir1 = self.segments_dir1
        quad.segments_dir2 = self.segments_dir3

        mesh_builder = quad.create().join(mesh_builder)

        return mesh_builder

    
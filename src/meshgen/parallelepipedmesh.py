
from meshgen.vector import Vector3

from meshgen.meshbuilder import MeshBuilder
from meshgen.quadmesh import QuadMesh

from meshgen.meshunion import MeshUnion

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

        quad.size1 = self.size1
        quad.size2 = self.size2
        quad.direction1 = self.direction1
        quad.direction2 = self.direction2
        quad.segments_dir1 = self.segments_dir1
        quad.segments_dir2 = self.segments_dir2

        up_quad = quad.create().translate(self.direction3.multiply(0.5 * self.size3))
        down_quad = quad.create().translate(self.direction3.multiply(-0.5 * self.size3))

        meshUnion = MeshUnion();
        meshUnion.size = self.size3;
        meshUnion.total_segments = self.segments_dir3;

        tunnel = meshUnion.create(up_quad.get_submesh(["border"]), down_quad.get_submesh(["border"]));

        return up_quad.join(down_quad).join(tunnel)

    
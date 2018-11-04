from meshunion import MeshUnion
from circlemesh import CircleMesh

from vector import Vector3

class CylinderMesh:
    def __init__(self):
        self.radius = 1.0
        self.direction1 = Vector3.forward()
        self.direction2 = Vector3.right()
        self.height = 2.0
        self.total_perimeter_vertices = 20
        self.total_vertical_segments = 1

    def create(self):
        circle_mesh = CircleMesh()
        circle_mesh.radius = self.radius
        circle_mesh.direction1 = self.direction1
        circle_mesh.direction2 = self.direction2
        circle_mesh.total_vertices = self.total_perimeter_vertices

        direction3 = self.direction1.cross_product(self.direction2).normalized()

        up_circle = circle_mesh.create().translate(direction3.multiply(0.5 * self.height))

        down_circle = circle_mesh.create().translate(direction3.multiply(-0.5 * self.height))

        meshUnion = MeshUnion();
        meshUnion.size = self.height;
        meshUnion.total_segments = self.total_vertical_segments;

        tunnel = meshUnion.create(up_circle, down_circle);

        return up_circle.join(down_circle).join(tunnel)
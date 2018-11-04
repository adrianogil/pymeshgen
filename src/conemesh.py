from vector import Vector3

from meshbuilder import MeshBuilder
from circlemesh import CircleMesh

from meshunion import MeshUnion

class ConeMesh:
    def __init__(self):
        self.radius = 1.0
        self.height = 1.0
        self.direction1 = Vector3.forward()
        self.direction2 = Vector3.right()
        self.direction3 = Vector3.up()
        self.total_perimeter_vertices = 20
        self.total_vertical_segments = 1

    def create(self):
        circleMesh = CircleMesh();
        circleMesh.radius = self.radius;
        circleMesh.direction1 = self.direction1;
        circleMesh.direction2 = self.direction2;
        circleMesh.totalVertices = self.total_perimeter_vertices;

        if self.direction3.minus(Vector3.up()).magnitude() < 0.001:
            self.direction3 = self.direction1.cross_product(self.direction2).normalized();

        baseCircle = circleMesh.create().translate(self.direction3.multiply(-0.5 * self.height));

        top = MeshBuilder();
        top.add_vertice(Vector3(0,-0.5*self.height,0).add(self.direction3.multiply(self.height)), ["border"]);

        meshUnion = MeshUnion();
        meshUnion.size = self.height;
        meshUnion.total_segments = self.total_vertical_segments;

        cone = meshUnion.create(top, baseCircle);

        return cone.join(baseCircle);
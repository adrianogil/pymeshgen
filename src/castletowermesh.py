from vector import Vector3

from cylindermesh import CylinderMesh
from conemesh import ConeMesh 

class CastleTowerMesh:
    def __init__(self):
        self.radius = 0.5
        self.height = 10.0

    def create(self):
        cylinder = CylinderMesh();

        cylinder.radius = self.radius;
        cylinder.direction1 = Vector3(1.0, 0.0, 0.0);
        cylinder.direction2 = Vector3(0.0, 0.0, 1.0);
        cylinder.total_perimeter_vertices = 30;
        cylinder.height = 0.4*self.height;

        meshBuilder = cylinder.create().translate(Vector3.up().multiply(0.2*self.height));

        cylinder.radius = 0.7*self.radius;
        cylinder.height = 0.2*self.height;

        meshBuilder = cylinder.create() \
            .translate(Vector3.up().multiply(0.5*self.height)) \
            .join(meshBuilder);

        cone = ConeMesh();
        cone.radius = 0.9 * self.radius;
        cone.height = 0.4 * self.height;
        cone.total_vertical_segments = 1;
        coneMeshBuilder = cone.create() \
                    .translate(Vector3.up().multiply(self.height - 0.5*cone.height));

        meshBuilder = meshBuilder.join(coneMeshBuilder);

        return meshBuilder;

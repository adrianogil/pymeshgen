from meshgen.vector import Vector3

from meshgen.cylindermesh import CylinderMesh
from meshgen.conemesh import ConeMesh 

class CastleTowerMesh:
    def __init__(self):
        self.radius = 0.5
        self.height = 10.0
        self.tower_pieces = 4
        self.total_perimeter_vertices = 30

    def create(self):
        cylinder = CylinderMesh();

        cylinder.radius = self.radius;
        cylinder.direction1 = Vector3.right();
        cylinder.direction2 = Vector3.forward();
        cylinder.total_perimeter_vertices = self.total_perimeter_vertices
        cylinder.height = 0.4*self.height;

        meshBuilder = cylinder.create();

        last_height = 0
        last_radius = self.radius
        for t in range(0, self.tower_pieces):
            last_radius = 0.87*last_radius
            cylinder.radius = last_radius
            cylinder.height = 0.6*self.height/self.tower_pieces
            last_height = last_height + cylinder.height

            meshBuilder = cylinder.create() \
                .translate(Vector3(0.0, last_height, 0.0)) \
                .join(meshBuilder);

        cone = ConeMesh();
        cone.radius = 0.9 * self.radius;
        cone.height = 0.2 * self.height;
        cone.total_vertical_segments = 1;
        coneMeshBuilder = cone.create() \
                    .translate(Vector3.up().multiply(0.6*self.height));

        meshBuilder = meshBuilder.join(coneMeshBuilder);

        return meshBuilder;

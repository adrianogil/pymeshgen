from vector import Vector3
from meshbuilder import MeshBuilder

import numpy as np

class CircleMesh:
    def __init__(self):
        self.radius = 10
        self.angle_start = 0
        self.angle_end = 360
        self.direction1 = Vector3.up()
        self.direction2 = Vector3.right()
        self.total_vertices=100


    def create(self, radius=None, \
        angle_start=None, angle_end=None, \
        direction1=None, direction2=None, \
        total_vertices=None):

        if radius is None:
            radius = self.radius
        if angle_start is None:
            angle_start = self.angle_start
        if angle_end is None:
            angle_end = self.angle_end
        if direction1 is None:
            direction1 = self.direction1
        if direction2 is None:
            direction2 = self.direction2
        if total_vertices is None:
            total_vertices = self.total_vertices

        # print('radius: %s' % (radius,))
        # print('angle_start: %s' % (angle_start,))
        # print('angle_end: %s' % (angle_end,))
        # print('direction1: %s' % (direction1,))
        # print('direction2: %s' % (direction2,))
        # print('total_vertices: %s' % (total_vertices,))

        builder = MeshBuilder()

        angles_per_vertices = (np.pi/180.0) * (angle_end - angle_start) / total_vertices

        radiusAmount = 0

        for i in range(0, total_vertices):
            radius_amount = i * angles_per_vertices + angle_start * (np.pi/180.0);
            point = direction1.multiply(radius * np.cos(radius_amount))
            point = point.add(direction2.multiply(radius * np.sin(radius_amount) ));
            builder.add_vertice(point, ["border"]);

        builder.add_vertice(Vector3.zero(), ["center"]);

        v1 = v2 = 0

        for i in range(0, total_vertices):
            v1 = i;
            v2 = (i+1) % total_vertices;

            builder.add_triangle(v1, v2, total_vertices);
            builder.add_triangle(v2, v1, total_vertices);

        return builder;
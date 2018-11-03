from stl import mesh
from vector import Vector3

import numpy as np

class MeshBuilder:
    def __init__(self):
        self.vertices = []
        self.triangles = []

    def add_quad(self, v1, v2):
        initial_index = len(self.vertices)

        self.vertices.append(Vector3.zero())
        self.vertices.append(v1)
        self.vertices.append(v1.add(v2))
        self.vertices.append(v2)

        self.add_triangle(initial_index+0, initial_index+1, initial_index+3)
        self.add_triangle(initial_index+1, initial_index+3, initial_index+2)
        self.add_triangle(initial_index+0, initial_index+3, initial_index+1)
        self.add_triangle(initial_index+1, initial_index+2, initial_index+3)

    def add_vertice(self, v, groups=None):
        # print('MeshBuilder.add_vertice - v - ' + str(v))
        self.vertices.append(v)

    def add_triangle(self, t0, t1, t2):
        self.triangles.append([t0,t1,t2])

    def scale(self, fscale):
        new_vertices = []

        for v in self.vertices:
            new_vertices.append(v.multiply(fscale))

        self.vertices = new_vertices

    def translate(self, tscale):
        new_vertices = []

        for v in self.vertices:
            new_vertices.append(v.add(tscale))

        self.vertices = new_vertices

    def create_mesh(self):
        new_mesh = mesh.Mesh(np.zeros(len(self.triangles), dtype=mesh.Mesh.dtype))
        for i, f in enumerate(self.triangles):
            for j in range(3):
                # print(str(i))
                # print(str(self.vertices[f[j]].value()))
                new_mesh.vectors[i][j] = np.transpose(self.vertices[f[j]].value())

        return new_mesh
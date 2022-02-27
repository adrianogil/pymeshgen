from stl import mesh
from meshgen.vector import Vector3

import numpy as np

class MeshBuilder:
    def __init__(self):
        self.vertices = []
        self.triangles = []
        self.vertices_groups = {'default':[]}

    def clone(self):
        new_mesh_builder =  MeshBuilder()

        new_mesh_builder.vertices = self.vertices.copy()
        new_mesh_builder.triangles = self.triangles.copy()

        return new_mesh_builder

    def add_vertice(self, v, groups=None):
        # print('MeshBuilder.add_vertice - v - ' + str(v))
        self.vertices.append(v)

        if groups is not None:
            for g in groups:
                if g != "default":
                    if g in self.vertices_groups:
                        self.vertices_groups[g].append(v)
                    else:
                        self.vertices_groups[g] = [v]
        self.vertices_groups['default'].append(v)


    def get_vertices(self, group_name='default'):
        return self.vertices_groups[group_name]

    def add_triangle(self, t0, t1, t2):
        self.triangles.append([t0,t1,t2])

    def scale(self, fscale):
        new_vertices = []

        for v in self.vertices:
            new_vertices.append(v.multiply(fscale))
        self.vertices = new_vertices

        for g in self.vertices_groups:
            new_vertices = []
            for vg in self.vertices_groups[g]:
                new_vertices.append(vg.multiply(fscale))
            self.vertices_groups[g] = new_vertices



    def translate(self, tscale):
        new_vertices = []

        for v in self.vertices:
            new_vertices.append(v.add(tscale))
        self.vertices = new_vertices

        for g in self.vertices_groups:
            new_vertices = []
            for vg in self.vertices_groups[g]:
                new_vertices.append(vg.add(tscale))
            self.vertices_groups[g] = new_vertices

        return self


    def create_mesh(self):
        new_mesh = mesh.Mesh(np.zeros(len(self.triangles), dtype=mesh.Mesh.dtype))
        for i, f in enumerate(self.triangles):
            for j in range(3):
                # print(str(i))
                # print(str(self.vertices[f[j]].value()))
                new_mesh.vectors[i][j] = np.transpose(self.vertices[f[j]].value())

        return new_mesh

    def join(self, mesh_builder):
        new_mesh_builder = MeshBuilder()

        total_vertices_b1 = len(self.vertices)

        for v in self.vertices:
            new_mesh_builder.vertices.append(v)
        for v in mesh_builder.vertices:
            new_mesh_builder.vertices.append(v)

        for t in self.triangles:
            new_mesh_builder.triangles.append(t)
        for t in mesh_builder.triangles:

            t[0] = t[0] + total_vertices_b1
            t[1] = t[1] + total_vertices_b1
            t[2] = t[2] + total_vertices_b1

            # print(str(t))

            new_mesh_builder.triangles.append(t)

        return new_mesh_builder

    def get_submesh(self, groups):
        new_mesh_builder = MeshBuilder()

        new_vertices = []
        vertices_index = []

        for g in groups:
            if g in self.vertices_groups:
                for v in self.vertices_groups[g]:
                    new_vertices.append(v)
                    for i in range(0, len(self.vertices)):
                        if v.minus(self.vertices[i]).magnitude() < 0.0001:
                            vertices_index.append(i)
                            break

        new_triangles = []
        for t in self.triangles:
            if t[0] in vertices_index and \
               t[1] in vertices_index and \
               t[2] in vertices_index:
               new_triangles.append(t)

        new_mesh_builder.vertices = new_vertices
        new_mesh_builder.triangles = new_triangles

        return new_mesh_builder



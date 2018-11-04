
from vector import Vector3

from meshbuilder import MeshBuilder

class QuadMesh:
    def __init__(self):
        self.origin = Vector3.zero()
        self.direction1 = Vector3.forward()
        self.direction2 = Vector3.right()
        self.segments_dir1 = 10
        self.segments_dir2 = 10
        self.size1 = 2
        self.size2 = 2



    def create(self):

        mesh_builder = MeshBuilder()

        size_dir1 = self.size1 * 1.0 / self.segments_dir1
        size_dir2 = self.size2 * 1.0 / self.segments_dir2

        for x in range(0, self.segments_dir1):
            for y in range(0, self.segments_dir2):
                initial_index = len(mesh_builder.vertices)

                initial_point = self.origin.add(self.direction1.multiply(x*size_dir1)).add(self.direction2.multiply(y*size_dir2))
                v1 = self.direction1.multiply((x+1)*size_dir1)
                v2 = self.direction2.multiply((y+1)*size_dir2)

                if x == 0 or y == 0:
                    mesh_builder.add_vertice(initial_point, ['border'])
                else:
                    mesh_builder.add_vertice(initial_point)

                if x == self.segments_dir1-1:
                    mesh_builder.add_vertice(initial_point.add(v1), ['border'])
                else:
                    mesh_builder.add_vertice(initial_point.add(v1))

                if x == self.segments_dir1-1 or y == self.segments_dir2-1:
                    mesh_builder.add_vertice(initial_point.add(v1).add(v2), ['border'])
                else:
                    mesh_builder.add_vertice(initial_point.add(v1).add(v2))

                if y == self.segments_dir2-1:
                    mesh_builder.add_vertice(initial_point.add(v2), ['border'])
                else:
                    mesh_builder.add_vertice(initial_point.add(v2))

                mesh_builder.add_triangle(initial_index+0, initial_index+1, initial_index+3)
                mesh_builder.add_triangle(initial_index+1, initial_index+3, initial_index+2)
                mesh_builder.add_triangle(initial_index+0, initial_index+3, initial_index+1)
                mesh_builder.add_triangle(initial_index+1, initial_index+2, initial_index+3)

        return mesh_builder
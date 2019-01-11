
from meshgen.vector import Vector3

from meshgen.meshbuilder import MeshBuilder

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

        self.size_dir1 = self.size1 * 1.0 / self.segments_dir1
        self.size_dir2 = self.size2 * 1.0 / self.segments_dir2

        group = ['border', 'border', 'default', 'default']
        for x in range(0, self.segments_dir1+1):
            mesh_builder = self.generate_quad(x, 0, mesh_builder, group)

        group = ['default', 'border', 'border', 'default']
        for y in range(0, self.segments_dir2+1):
            mesh_builder = self.generate_quad(self.segments_dir1, y, mesh_builder, group)

        group = ['default', 'default', 'border', 'border']
        for x in range(0, self.segments_dir1+1):
            mesh_builder = self.generate_quad(self.segments_dir1-x, self.segments_dir2, mesh_builder, group)

        group = ['border', 'default', 'default', 'border']
        for y in range(0, self.segments_dir2+1):
            mesh_builder = self.generate_quad(0, self.segments_dir2-y, mesh_builder, group)

        default_group = ['default', 'default', 'default', 'default']
        for x in range(1, self.segments_dir1):
            for y in range(1, self.segments_dir2):
                mesh_builder = self.generate_quad(x, y, mesh_builder, default_group)

        return mesh_builder

    def generate_quad(self, x, y, mesh_builder, group=['default', 'default', 'default', 'default']):
        initial_index = len(mesh_builder.vertices)

        initial_point = self.origin.add(self.direction1.multiply(x*self.size_dir1)).add(self.direction2.multiply(y*self.size_dir2))
        v1 = self.direction1.multiply((x+1)*self.size_dir1)
        v2 = self.direction2.multiply((y+1)*self.size_dir2)

        mesh_builder.add_vertice(initial_point, [group[0]])
        mesh_builder.add_vertice(initial_point.add(v1), [group[1]])
        mesh_builder.add_vertice(initial_point.add(v1).add(v2), [group[2]])
        mesh_builder.add_vertice(initial_point.add(v2), [group[3]])

        mesh_builder.add_triangle(initial_index+0, initial_index+1, initial_index+3)
        mesh_builder.add_triangle(initial_index+1, initial_index+3, initial_index+2)
        mesh_builder.add_triangle(initial_index+0, initial_index+3, initial_index+1)
        mesh_builder.add_triangle(initial_index+1, initial_index+2, initial_index+3)

        return mesh_builder
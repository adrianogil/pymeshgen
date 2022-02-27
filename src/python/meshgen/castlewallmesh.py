from meshgen.parallelepipedmesh import ParallelepipedMesh
from meshgen.meshunion import MeshUnion
from meshgen.castletowermesh import CastleTowerMesh
from meshgen.vector import Vector3

class CastleWallMesh:
    def __init__(self):
        self.number_towers = 10
        self.tower_height_segments = 10
        self.round_radius_segments = 20
        self.boundary = None
        self.wall_thick = 0.1
        self.wall_size_x = 100
        self.wall_size_y = 10
        self.wall_size_z = 60
        self.center_pos = Vector3(0.0, -0.5 * self.wall_size_y + 4, 0.0)

    def create_using_custom_boundary(self):
        ''' WIP '''
        inner_wall = self.boundary
        outside_wall = self.boundary.clone()
        outside_wall.scale(self.wall_thick)

        mesh_union = MeshUnion()

        wall_plane = mesh_union.create(inner_wall, outside_wall)

        return wall_plane

    def create(self):
        p0 = self.center_pos\
            .add(Vector3.forward().multiply(0.5*self.wall_size_z))\
            .add(Vector3.right().multiply(0.5*self.wall_size_x))

        p1 = p0.add(Vector3.forward().multiply(-1 * self.wall_size_z))
        p2 = p1.add(Vector3.right().multiply(-1 * self.wall_size_x))
        p3 = p2.add(Vector3.forward().multiply(self.wall_size_z))


        parallelepiped = ParallelepipedMesh()
        parallelepiped.direction1 = Vector3.forward()
        parallelepiped.direction2 = Vector3.right()
        parallelepiped.direction3 = Vector3.up()
        parallelepiped.size1 = self.wall_size_z
        parallelepiped.size2 = self.wall_thick
        parallelepiped.size3 = self.wall_size_y
        parallelepiped.origin = p0.multiply(0.5).add(p1.multiply(0.5))

        mesh_builder = parallelepiped.create()

        parallelepiped.size1 = self.wall_thick
        parallelepiped.size2 = 2 * self.wall_size_x
        parallelepiped.origin = p1.multiply(0.5).add(p2.multiply(0.5))

        mesh_builder = parallelepiped.create().join(mesh_builder)

        # parallelepiped.origin = Vector3(0.6*self.total_size1, \
        #                                 0.35*self.total_size3, \
        #                                 0.6*self.total_size2)
        # parallelepiped.size1 = 0.4*self.total_size1
        # parallelepiped.size2 = 0.4*self.total_size2
        # parallelepiped.size3 = 0.1*self.total_size3

        # mesh_builder = parallelepiped.create().join(mesh_builder)

        return mesh_builder

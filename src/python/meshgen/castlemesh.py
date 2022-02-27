from meshgen.maincastlemesh import MainCastleMesh
from meshgen.castlewallmesh import CastleWallMesh

from meshgen.quadmesh import QuadMesh


class CastleMesh:
    def __init__(self):
        self.total_size1 = 15
        self.total_size2 = 15
        self.total_size3 = 50
        self.space_to_wall = 1.2

    def create(self):
        castle = MainCastleMesh()

        castle.total_size1 = self.total_size1
        castle.total_size2 = self.total_size2
        castle.total_size3 = self.total_size3

        mesh_builder = castle.create()

        quad = QuadMesh()
        quad.size1 = self.space_to_wall * self.total_size1
        quad.size2 = self.space_to_wall * self.total_size2

        wall = CastleWallMesh()
        # wall.boundary = quad.create().get_submesh(["border"])
        mesh_builder = wall.create().join(mesh_builder)

        return mesh_builder

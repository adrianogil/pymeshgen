from meshgen.parallelepipedmesh import ParallelepipedMesh
from meshgen.castletowermesh import CastleTowerMesh

from meshgen.vector import Vector3

class MainCastleMesh:
    def __init__(self):
        self.total_size1 = 15
        self.total_size2 = 15
        self.total_size3 = 50

    def create(self):
        parallelepiped = ParallelepipedMesh()
        parallelepiped.direction1 = Vector3.forward()
        parallelepiped.direction2 = Vector3.right()
        parallelepiped.direction3 = Vector3.up()
        parallelepiped.size1 = self.total_size1
        parallelepiped.size2 = self.total_size2
        parallelepiped.size3 = 0.2*self.total_size3

        mesh_builder = parallelepiped.create()

        parallelepiped.origin = Vector3(0.2*self.total_size1, \
                                        0.2*self.total_size3, \
                                        0.2*self.total_size2)
        parallelepiped.size1 = 0.8*self.total_size1
        parallelepiped.size2 = 0.8*self.total_size2
        parallelepiped.size3 = 0.2*self.total_size3

        mesh_builder = parallelepiped.create().join(mesh_builder)

        parallelepiped.origin = Vector3(0.6*self.total_size1, \
                                        0.35*self.total_size3, \
                                        0.6*self.total_size2)
        parallelepiped.size1 = 0.4*self.total_size1
        parallelepiped.size2 = 0.4*self.total_size2
        parallelepiped.size3 = 0.1*self.total_size3

        mesh_builder = parallelepiped.create().join(mesh_builder)

        tower = CastleTowerMesh()
        tower.radius = 0.35*self.total_size1
        tower.height = 0.5*self.total_size3
        tower_origin = Vector3(self.total_size1, \
                               0.5*self.total_size3, \
                               self.total_size2)

        mesh_builder = tower.create().translate(tower_origin)\
            .join(mesh_builder)

        return mesh_builder
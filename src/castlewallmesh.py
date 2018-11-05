
from castletowermesh import CastleTowerMesh

class CastleWallMesh:
    def __init__(self):
        self.number_towers = 10
        self.tower_height_segments = 10
        self.round_radius_segments = 20
        self.boundary = None
        self.wall_length = 0.1

    def create(self):
        inner_wall = self.boundary
        outside_wall = self.boundary.clone().scale(Vector3(0.0, self.wall_thick, 0.0))

        
from meshbuilder import MeshBuilder

class MeshUnion:
    def __init__(self):
        self.size = 1.0
        self.total_segments = 1

    def create(self, meshbuilder1, meshbuilder2, is_round=True):
        mesh_builder = MeshBuilder()

        segment_size = self.size / self.total_segments

        if len(meshbuilder1.get_vertices("border")) == len(meshbuilder2.get_vertices("border")):
            # print("GilLog - MeshUnion::Create - round " + round + " 1 ")

            total_vertices = len(meshbuilder1.get_vertices("border"))

            # print("GilLog - MeshUnion::Create - round " + is_round + "  - total_vertices " + \
                # total_vertices + "  - segment_size " + segment_size + " ")

            for i in range(0, total_vertices):
                # print("GilLog - MeshUnion::Create - meshbuilder1 " + meshbuilder1 + " meshbuilder2 " + meshbuilder2 + " round " + round + "  - meshbuilder1.get_vertices(border)[i] " + meshbuilder1.get_vertices("border")[i] + "  - meshbuilder2.get_vertices(border)[i] " + meshbuilder2.get_vertices("border")[i] + " ");
                
                print("meshbuilder1 - vertice " + str(i) + ": " + str(meshbuilder1.get_vertices("border")[i]))
                print("meshbuilder2 - vertice " + str(i) + ": " + str(meshbuilder2.get_vertices("border")[i]))

                diff_vector = meshbuilder1.get_vertices("border")[i].minus(meshbuilder2.get_vertices("border")[i]).normalized()

                print("diff_vector: " + str(diff_vector))

                for s in range(0, self.total_segments):
                    mesh_builder.add_vertice( \
                        meshbuilder1.get_vertices("border")[i] \
                            .add(diff_vector.multiply(s * segment_size)) \
                        )

                    if i < total_vertices - 1 or is_round:
                        next_index = (i + 1) % total_vertices
                        mesh_builder.add_triangle(
                            i*(self.total_segments+1)+s,
                            i*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s
                            )
                        mesh_builder.add_triangle(
                            i*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s
                            )

                mesh_builder.add_vertice(meshbuilder2.get_vertices("border")[i])
        else:
            tmp = None;

            if len(meshbuilder1.get_vertices("border")) > len(meshbuilder2.get_vertices("border")):
                tmp = meshbuilder1;
                meshbuilder1 = meshbuilder2;
                meshbuilder2 = tmp;

            total_vertices1 = len(meshbuilder1.get_vertices("border"));
            total_vertices2 = len(meshbuilder2.get_vertices("border"));

            vertices2_for_each_v1 = total_vertices2 / total_vertices1;

            current_vertice2 = 0;

            v1_index = 0;

            for i in range(0, total_vertices1):
                v1_index = len(mesh_builder.vertices)
                mesh_builder.add_vertice(\
                            meshbuilder1.get_vertices("border")[i]\
                            )

                v2 = current_vertice2
                while (i == total_vertices1-1 and v2 < total_vertices2) or v2 < current_vertice2 + vertices2_for_each_v1:
                    # Debug.Log("GilLog - MeshUnion::Create - meshbuilder1 " + meshbuilder1 + " meshbuilder2 " + meshbuilder2 + " round " + round + "  - v2 " + v2 + " ");
                    diff_vector = meshbuilder1.get_vertices("border")[i]\
                        .minus(meshbuilder2.get_vertices("border")[v2]).normalized()

                    for s in range(0, self.total_segments):
                        if s > 0:
                            mesh_builder.add_vertice(\
                                meshbuilder1.get_vertices("border")[i]\
                                .add(diff_vector.multiply(s * segment_size))\
                            );

                        if v2 < total_vertices2 - 1 or is_round:
                            next_index = (v2 + 1) % total_vertices2;
                            mesh_builder.add_triangle(
                                v1_index,
                                v1_index + v2*self.total_segments + s + 1,
                                v1_index + v2*self.total_segments + s + 2
                                );

                    mesh_builder.add_vertice(meshbuilder2.get_vertices("border")[v2]);

                    v2 = v2 + 1

                current_vertice2 = current_vertice2 + vertices2_for_each_v1;

        return mesh_builder;
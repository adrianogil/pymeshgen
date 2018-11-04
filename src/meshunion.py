from meshbuilder import MeshBuilder

class MeshUnion:
    def __init__(self):
        self.size = 1.0
        self.total_segments = 1

    def create(self, meshbuilder1, meshbuilder2, is_round=True):
        mesh_builder = MeshBuilder()

        segment_size = float(self.size * 1.0 / self.total_segments)

        if len(meshbuilder1.vertices) == len(meshbuilder2.vertices):
            # print("GilLog - MeshUnion::Create - round " + str(is_round) + " 1 ")

            total_vertices = len(meshbuilder1.vertices)

            # print("GilLog - MeshUnion::Create - round " + is_round + "  - total_vertices " + \
                # total_vertices + "  - segment_size " + segment_size + " ")

            for i in range(0, total_vertices):
                # print("GilLog - MeshUnion::Create - meshbuilder1 " + meshbuilder1 + " meshbuilder2 " + meshbuilder2 + " round " + round + "  - meshbuilder1.get_vertices(border)[i] " + meshbuilder1.vertices[i] + "  - meshbuilder2.get_vertices(border)[i] " + meshbuilder2.vertices[i] + " ");
                
                # print("meshbuilder1 - vertice " + str(i) + ": " + str(meshbuilder1.vertices[i]))
                # print("meshbuilder2 - vertice " + str(i) + ": " + str(meshbuilder2.vertices[i]))

                diff_vector = meshbuilder2.vertices[i].minus(meshbuilder1.vertices[i])
                segment_size = diff_vector.magnitude() / self.total_segments
                diff_vector = diff_vector.normalized()

                # print("diff_vector: " + str(diff_vector))

                for s in range(0, self.total_segments):

                    new_vertice = meshbuilder1.vertices[i] \
                            .add(diff_vector.multiply(float(s) * segment_size))
                    mesh_builder.add_vertice(new_vertice)
                    # print("%s %s %s \n%s\n%s\n%s\n%s" % (s, self.total_segments, segment_size, diff_vector, meshbuilder1.vertices[i], new_vertice, meshbuilder2.vertices[i]))

                    if i < total_vertices - 1 or is_round:
                        next_index = (i + 1) % total_vertices
                        mesh_builder.add_triangle(
                            i*(self.total_segments+1)+s,
                            i*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s
                            )
                        mesh_builder.add_triangle(
                            i*(self.total_segments+1)+s+1,
                            i*(self.total_segments+1)+s,
                            next_index*(self.total_segments+1)+s
                            )
                        mesh_builder.add_triangle(
                            i*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s
                            )
                        mesh_builder.add_triangle(
                            next_index*(self.total_segments+1)+s+1,
                            i*(self.total_segments+1)+s+1,
                            next_index*(self.total_segments+1)+s
                            )

                mesh_builder.add_vertice(meshbuilder2.vertices[i])
        else:
            # print("GilLog - MeshUnion::Create - round " + str(is_round) + " 2 ")
            tmp = None;

            if len(meshbuilder1.vertices) > len(meshbuilder2.vertices):
                tmp = meshbuilder1;
                meshbuilder1 = meshbuilder2;
                meshbuilder2 = tmp;

            total_vertices1 = len(meshbuilder1.vertices);
            total_vertices2 = len(meshbuilder2.vertices);

            vertices2_for_each_v1 = total_vertices2 / total_vertices1;

            current_vertice2 = 0;

            v1_index = 0;

            for i in range(0, total_vertices1):
                v1_index = len(mesh_builder.vertices)
                mesh_builder.add_vertice(\
                            meshbuilder1.vertices[i]\
                            )

                v2 = current_vertice2
                while (i == total_vertices1-1 and v2 < total_vertices2) or v2 < current_vertice2 + vertices2_for_each_v1:
                    # Debug.Log("GilLog - MeshUnion::Create - meshbuilder1 " + meshbuilder1 + " meshbuilder2 " + meshbuilder2 + " round " + round + "  - v2 " + v2 + " ");
                    diff_vector = meshbuilder2.vertices[i].minus(meshbuilder1.vertices[i])
                    segment_size = diff_vector.magnitude() / self.total_segments
                    diff_vector = diff_vector.normalized()

                    for s in range(0, self.total_segments):
                        if s > 0:
                            mesh_builder.add_vertice(\
                                meshbuilder1.vertices[i]\
                                .add(diff_vector.multiply(s * segment_size))\
                            );

                        if v2 < total_vertices2 - 1 or is_round:
                            next_index = (v2 + 1) % total_vertices2;
                            mesh_builder.add_triangle(
                                v1_index,
                                v1_index + v2*self.total_segments + s + 1,
                                v1_index + v2*self.total_segments + s + 2
                                );

                    mesh_builder.add_vertice(meshbuilder2.vertices[v2]);

                    v2 = v2 + 1

                current_vertice2 = current_vertice2 + vertices2_for_each_v1;

        return mesh_builder;
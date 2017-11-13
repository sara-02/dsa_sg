INF = 999999


class FloydWarshall(object):

    def __init__(self, num_vertices):
        self.dist = [[INF] * num_vertices for i in range(num_vertices)]
        self.num_vertices = num_vertices

    @classmethod
    def get_graph_size(cls, graph_row):
        return len(graph_row)

    def initial_dist(self, graph):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                self.dist[i][j] = graph[i][j]

    def floyd_warshall(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                for k in range(self.num_vertices):
                    self.dist[j][k] = min(
                        self.dist[j][k],
                        self.dist[j][i] + self.dist[i][k])

    def print_distance_matrix(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                d = self.dist[i][j]
                if d == INF:
                    d = 'INF'
                print d,
            print "\n"


def main():
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
    num_vertices = FloydWarshall.get_graph_size(graph[0])
    fwd = FloydWarshall(num_vertices)
    fwd.initial_dist(graph)
    fwd.floyd_warshall()
    fwd.print_distance_matrix()


if __name__ == "__main__":
    main()

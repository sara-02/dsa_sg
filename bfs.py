graph_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
vertices = [0, 1, 2, 3, 4]


def mark_visited(node):
    graph_matrix[node][node] = -1


def is_visited(node):
    return graph_matrix[node][node] == -1


def neighbour(vertex):
    nl = []
    c = len(graph_matrix[vertex])
    for n, p in zip(graph_matrix[vertex], range(c)):
        if n == 1:
            nl.append(p)
    return nl

queue = []
parent = {}
for v in vertices:
    parent[v] = -1

start_node = vertices[0]
mark_visited(start_node)
queue.append(start_node)

while len(queue) != 0:
    v = queue.pop(0)
    print chr(65 + v)
    for x in neighbour(v):
        if not is_visited(x):
            queue.append(x)
            mark_visited(x)
            parent[x] = v

for k, v in parent.items():
    print chr(65 + k), chr(65 + v)

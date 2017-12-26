class UnionFind(object):

    def __init__(self, USE_RANK=False):
        self.parent = []
        self.rank = []
        self.USE_RANK = USE_RANK

    def initailise(self, num_nodes):
        if self.USE_RANK:
            self.rank = [0] * num_nodes
        self.parent = range(num_nodes)

    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.find_parent(self.parent[node])

    def union(self, node_1, node_2):
        if self.USE_RANK:
            return self.union_with_rank(node_1, node_2)
        else:
            return self.union_no_rank(node_1, node_2)

    def union_no_rank(self, node_1, node_2):
        node_1_class = self.find_parent(node_1)
        node_2_class = self.find_parent(node_2)
        if node_1_class != node_2_class:
            self.parent[node_1_class] = node_2_class

    def union_with_rank(self, node_1, node_2):
        node_1_class = self.find_parent(node_1)
        node_2_class = self.find_parent(node_2)
        if node_1_class != node_2_class:
            if self.rank[node_1_class] < self.rank[node_2_class]:
                self.parent[node_1_class] = node_2_class
            elif self.rank[node_1_class] > self.rank[node_2_class]:
                self.parent[node_2_class] = node_1_class
            else:
                self.parent[node_1_class] = node_2_class
                self.rank[node_2_class] += 1

if __name__ == '__main__':
    # Without Ranking
    uf1 = UnionFind()
    uf1.initailise(5)
    assert all(uf1.find_parent(i) == i for i in range(5))
    uf1.union(0, 1)
    assert uf1.parent == [1, 1, 2, 3, 4]
    uf1.union(2, 3)
    assert uf1.parent == [1, 1, 3, 3, 4]
    uf1.union(3, 4)
    assert uf1.parent == [1, 1, 3, 4, 4]
    before = uf1.parent
    uf1.union(2, 4)
    after = uf1.parent
    assert before == after

    # With Ranking
    uf2 = UnionFind(USE_RANK=True)
    uf2.initailise(5)
    assert all(uf2.find_parent(i) == i for i in range(5))
    assert all(uf2.rank[i] == 0 for i in range(5))
    uf2.union(0, 1)
    assert uf2.rank == [0, 1, 0, 0, 0]
    assert uf2.parent == [1, 1, 2, 3, 4]
    uf2.union(2, 3)
    assert uf2.rank == [0, 1, 0, 1, 0]
    assert uf2.parent == [1, 1, 3, 3, 4]
    uf2.union(3, 4)
    assert uf2.rank == [0, 1, 0, 1, 0]
    assert uf2.parent == [1, 1, 3, 3, 3]
    before = uf2.parent
    uf2.union(2, 4)
    assert uf2.rank == [0, 1, 0, 1, 0]
    after = uf2.parent
    assert before == after

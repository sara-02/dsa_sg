"""
Given a value n, determine how many simple graphs in total for size upto N.
Example: for N = 2
n = 0 # 0 nodes
possible = 0 # no graph is
n = 1 # one node
possible = 1 # a null graph
n = 2 # 2 nodes
possible = 2 # a null graph and a graph with 2 nodes and 1 edge
total possible = 1 + 1 + 2 = 4
General formula:
For a graph with n nodes,
there can be 0 < |E| < n*(n-1)/2 edges.
These range from zero for no edges to total edges for complete graph of n vertices.
And for every edge e, it can either be used in a graph or not. 
So total graph combination are 2^max_edges_possible for a given n.
"""

def num_graphs(n):
    count = 0
    for nodes in range(n + 1):
        max_edges = nodes * (nodes - 1) // 2
        total_simple_possible = 2**max_edges
        count += total_simple_possible
    return count

if __name__ == "__main__":
    print("Possible total graphs upto N for")
    print("N = 0 is : ", num_graphs(0))
    print("N = 1 is : ", num_graphs(1))
    print("N = 2 is : ", num_graphs(2))
    print("N = 9 is : ", num_graphs(9))
    print("N = 10 is : ", num_graphs(10))

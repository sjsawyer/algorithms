'''
Implementation of Kruskal's Aglorithm to find the Minimum Spanning
Tree (MST) of a graph.

Uses the "Union Find / Disjoint Set" data structure, which enables the
ability to check if two sets are disjoint in essentially O(1) time
(allowing us to check if greedily adding the next "best" edge to our tree
will result in a cycle in an efficient manner)

'''
import sys


def kruskal(graph):
    '''
    Kruskal's Algorithm to return the MST of graph `graph`

    graph: adjacency matrix representation of a graph

    Returns: a list of edges in the graph, where an edge is a 3 element
             tuple (weight, vertex1, vertex2)
    '''
    # use integers to represent each vertex
    vertices = [i for i in range(len(graph))]
    # initialize each vertex in the graph to belong to its own set
    parent = [i for i in vertices]
    # since each vertex is initialized in its own set, which we
    # represent as trees, their ranks (depth) are initialized to 0
    rank = [0 for _ in vertices]

    def _find(v):
        '''
        Return the "representative/root" node of the set/tree that `v`
        belongs to.
        Simultaneously applies path compression, connecting every node
        in the set/tree to the root node.
        '''
        if parent[v] != v:
            parent[v] = _find(parent[v])
        return parent[v]

    def _union(v1, v2):
        '''
        If v1 and v2 are in the same set, join the sets and update the
        rank of the new set appriately
        '''
        v1root = _find(v1)
        v2root = _find(v2)
        if v1root != v2root:
            if rank[v1root] < rank[v2root]:
                parent[v1root] = v2root
            else:
                parent[v2root] = v1root
                if rank[v1root] == rank[v2root]:
                    rank[v1root] += 1

    # we need to sort all of the edges by their weights
    # can insert them into a heap and then pop them off, but here
    # we'll just reverse sort them in a list and pop from the end
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            # invalid weights in the graph are currently represented
            # by 0, so change them to "infinity"
            weight = graph[i][j] or sys.maxint
            edges.append((weight, i, j))
    edges.sort(reverse=True)
    # `mst` will store the edges in our MST
    mst = []
    # Begin Kruskal
    n_vertices = len(vertices)
    # if our graph has n vertices, we stop when our tree has n-1 edges
    while len(mst) < n_vertices-1:
        e = edges.pop()
        if _find(e[1]) != _find(e[2]):
            # add the edges to the same set and add the edge to
            # our tree
            _union(e[1], e[2])
            mst.append(e)
    return mst


def main():
    from sample_graphs import g2_data
    adj_matrix, labels = g2_data
    mst = kruskal(adj_matrix)
    weight = sum(map(lambda x: x[0], mst))
    print "Edges in MST:"
    for edge in mst:
        print labels[edge[1]] + "->" + labels[edge[2]]
    print "MST Weight: {}".format(weight)


if __name__ == '__main__':
    main()

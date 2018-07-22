'''
Prim's algorithm is another greedy algorithm to generate a MST from a graph.
At any stage of the algorithm, we have two sets of vertices: the first set
contains vertices we have already added to the MST, and the second set contains
vertices we have yet to add. We then find a cut of the two sets (a set of edges
connecting the two sets), pick the minimum weight edge from the cut, and add to
the mst set the vertex not currently in it.

'''
import heapq
import sys


def _gen_neighbours(vertex, g, mst_set):
    '''
    Return a generator of the neighbours of a given vertex `vertex` in graph
    `g`, where `g` is an adjacency matrix, `vertex` the corresponding index of
    the vertex in the graph, and 0 is used to represent no connection between
    two vertices in the adjacency matrix

    '''
    return (i for i in range(len(g)) if g[vertex][i] and not mst_set[i])


def prim(g):
    # Initalize two "sets": one containing vertices we still need to add to the
    # mst and one containing vertices we have already added
    # We can in fact represent the "to add" set using a priority queue, as we
    # will always be interested in retrieving the minimum weight edge
    to_add = []
    mst_set = [False for _ in g]
    # minimum weight edges so far
    # These will be added to the priority queue, and we will be updating the
    # values of the minimum weight edge as the algorithm progresses, so we need
    # to use a datatype that can reference items in the priority queue
    # (e.g. list)
    mwe = [[sys.maxint, i] for i in range(len(g))]
    # To reconstruct the tree
    parent = [None for _ in g]
    # Initially we have to add all vertices to the set
    for cost_and_vertex in mwe:
        heapq.heappush(to_add, cost_and_vertex)
    while to_add:
        # next vertex of minimum weight edge
        _, vertex = heapq.heappop(to_add)
        # Add the vertex to the mst set
        mst_set[vertex] = True
        # Update the minimum weight edges of the neighbours of this vertex
        # that have NOT been added to the mst
        for neighbour in _gen_neighbours(vertex, g, mst_set):
            if g[vertex][neighbour] < mwe[neighbour][0]:
                # the weigt of edge vertex->neighbour is lower cost than the
                # current minimum
                mwe[neighbour][0] = g[vertex][neighbour]
                parent[neighbour] = vertex
        # maintain the heap invariant
        heapq.heapify(to_add)
    # Return the edges and weights
    edges = []
    for i in range(len(parent)):
        if parent[i] is not None:
            par, child = parent[i], i
            weight = g[par][child]
            edges.append((weight, par, child))
    return edges


def main():
    from sample_graphs import g2_data
    adj_matrix, labels = g2_data
    mst = prim(adj_matrix)
    weight = sum(map(lambda x: x[0], mst))
    print "Edges in MST:"
    for edge in mst:
        print labels[edge[1]] + "->" + labels[edge[2]]
    print "MST Weight: {}".format(weight)


if __name__ == '__main__':
    main()

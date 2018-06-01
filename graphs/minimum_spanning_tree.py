from collections import deque


def minimal_spanning_tree(graph, root):
    '''
    Find the minimal spanning tree in the graph `graph` that starts at the node
    `root` in graph `graph`. The result is a tree such that the path between
    any vertex in the tree and `root` in the tree is the shortest path between
    that vertex and `root` in the original graph `graph`

    graph: a dict whose keys are the nodes in the graph and value is a set
           containing the node's neighbors

    root: a node in the graph from which to start the search

    '''
    # the mst we will return
    tree = {}
    # queue to keep track of the vertices in a BFS order
    queue = deque()
    # the set of vertices we have visited so far
    visited = set()
    # check for an empty graph
    if not graph:
        return tree
    # initialize the tree
    for node in graph:
        tree[node] = set()
    # we start at the root
    queue.append(root)
    visited.add(root)
    while queue:
        # we have nodes left to explore
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                # have not seen this node yet, so add it
                visited.add(neighbor)
                queue.append(neighbor)
                # neighbor and node are adjacent in the tree
                tree[neighbor].add(node)
                tree[node].add(neighbor)
    return tree


def main():
    from sample_graphs import g1
    mst = minimal_spanning_tree(g1)
    for k, v in mst.iteritems():
        print "{}: {}".format(k, " ".join(v))


if __name__ == '__main__':
    main()

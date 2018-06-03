def depth_first_search(graph, start, end):
    '''
    Find a path from the `start` note in `graph` to the `end` node in `graph`,
    searching in a depth-first manner.

    graph: a dict whose keys are the nodes in the graph and value is a set
           containing the node's neighbors

    start: a node in the graph from which to start the search

    end: a node in the graph from which to start the search

    '''
    # nodes we have visited so far
    # to replicate a stack, we will use list() which is O(1) with LIFO operations
    unvisited = []
    # nodes we have seen so far
    seen = set()
    # where we came from in the path
    previous = {k: None for k in graph.iterkeys()}
    # initalize
    unvisited.append(start)
    seen.add(start)
    node = None
    while unvisited:
        # explore the most recent node added
        node = unvisited.pop()
        if node == end:
            # the search is over
            # get path from `previous` after this point
            break
        for neighbor in graph[node]:
            if neighbor not in seen:
                unvisited.append(neighbor)
                seen.add(neighbor)
                previous[neighbor] = node
    # reconstruct the path in reversed order
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    # return path in the correct order
    path.reverse()
    return path


def main():
    from sample_graphs import g1
    start = 'a'
    end = 'f'
    path = depth_first_search(g1, start, end)
    print " -> ".join(node for node in path)


if __name__ == '__main__':
    main()


import sys
import heapq


def dijkstra(D, start, end):
    '''
    Find the shortest path in a weighted graph from a source node to a target
    node. Will return RuntimeError if no path is found (i.e. could occur if the
    graph is disconnected)

    D: weighted adjacency matrix representation of the graph, where `D[i][j]`
       is the cost to travel from node `i` to node `j`

    start: index of the source node

    end: index of the target node

    '''
    # priority queue prioritizing vertices with the lowest costs
    pq = []
    # keep track of where we've come from
    previous = [None for _ in D]
    # create a list of cost, index pairs to serve as pointers to items in
    # the priority queue, so that we can modify items in the pq in place
    # distance to start node is 0, all others is "infinity"
    costs = [[sys.maxint, i] for i in xrange(len(D))]
    costs[start][0] = 0
    # initialize the priority queue
    for i in xrange(len(D)):
        heapq.heappush(pq, costs[i])
    while pq:
        # get the next lowest cost node from the priority queue
        cost_to_i, i = heapq.heappop(pq)
        if i == end:
            # we arrived at the optimal solution
            break
        if cost_to_i == sys.maxint:
            # `end` is not reachable from `start`
            raise RuntimeError("No path from {} to {} found".format(start, end))
        # explore the neighbors of this node
        for j in xrange(len(D)):
            if D[i][j] != 0:
                # i and j are adjacent
                cost_with_i = cost_to_i + D[i][j]
                if cost_with_i < costs[j][0]:
                    # update with the new cost
                    costs[j][0] = cost_with_i
                    previous[j] = i
                    # maintain heap structure
                    heapq.heapify(pq)
    # reconstruct the path in reversed order
    path = []
    prev = end
    while prev is not None:
        path.append(prev)
        prev = previous[prev]
    path.reverse()
    return path


def main():
    from sample_graphs import g2, g2_labels
    start, end = 'a', 'c'
    startidx, endidx = g2_labels.index(start), g2_labels.index(end)
    path = dijkstra(g2, startidx, endidx)
    labeled_path = [g2_labels[i] for i in path]
    print " -> ".join(labeled_path)


if __name__ == '__main__':
    main()

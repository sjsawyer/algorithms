import sys
import heapq


def astar(D, H, start, end):
    '''
    Find the shortest path in a weighted graph from a source node to a target
    node, using the heuristic adjacency matrix `H` to improve performance.
    Will return RuntimeError if no path is found (i.e. could occur if the
    graph is disconnected)

    D: weighted adjacency matrix representation of the graph, where `D[i][j]`
       is the cost to travel from node `i` to node `j`

    H: heuristic (e.g. "estimated") distances from each node in the graph to
       the target node `end`

    start: index of the source node

    end: index of the target node

    '''
    # priority queue prioritizing vertices with the lowest costs
    # prioritizing is done using a combination of the heuristic distance and
    # the actual distance
    pq = []
    # keep track of where we've come from
    previous = [None for _ in D]
    # create a list of heuristic-cost, actual cost, index triples to serve as
    # pointers to items in the priority queue, so that we can modify items in
    # the pq in place
    costs = [[sys.maxint, sys.maxint, i] for i in xrange(len(D))]
    # combined actual-heuristic cost for start node
    costs[start][0] = H[start]
    # actual distance from start node is 0
    costs[start][1] = 0
    # initialize the priority queue
    for i in xrange(len(D)):
        heapq.heappush(pq, costs[i])
    while pq:
        # get the next lowest cost node from the priority queue
        h_cost, cost_to_i, i = heapq.heappop(pq)
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
                # compare the actual total cost so far with the actual total
                # cost using i (not the heuristic cost)
                cost_with_i = cost_to_i + D[i][j]
                if cost_with_i < costs[j][1]:
                    # update with the new cost
                    costs[j][1] = cost_with_i
                    # update the new cost with heuristic
                    costs[j][0] = costs[j][1] + H[j]
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
    from sample_graphs import g3_data
    g3, labels, coords = g3_data
    start, end = 's', 'e'
    startidx, endidx = labels.index(start), labels.index(end)
    # heurist will be the euclidean distance to the target node
    endx, endy = coords[endidx]
    H = [((coord[0]-endx)**2 + (coord[1]-endy)**2)**0.5
         for coord in coords]
    path = astar(g3, H, startidx, endidx)
    labeled_path = [labels[i] for i in path]
    print " -> ".join(labeled_path)


if __name__ == '__main__':
    main()

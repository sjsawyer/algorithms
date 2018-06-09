def knapsack(weights, values, max_weight):
    '''
    Given `n` items i = 1,..,n, where each item has a value values[i] and
    weight weights[i], find a subset such that the total weight is less than
    or equal to `max_weight`, and the sum of the values is maximized.
    '''
    
    n = len(values)
    # Let D[n][w] be the optimal value using items <= n and max weight w
    D = [[None for w in xrange(max_weight+1)] for n in xrange(n)]

    def opt(n, w):
        '''
        Returns the optimal value that can be found using all items of index
        <= `n` and a max weight capacity of `w`

        We can use the recurrence relation

            opt(n, w) = max(opt(n-1,w), opt(n-1,w-weights[n])+values[n])

        to determine the solution in a top down manner, using the table `D` to
        assist in memoization of overlapping subproblems.

        '''
        if D[n][w] is not None:
            return D[n][w]
        elif w == 0 or n == 0:
            D[n][w] = 0
            return D[n][w]
        elif w-weights[n] < 0:
            return opt(n-1, w)
        else:
            D[n][w] = max(opt(n-1, w), opt(n-1, w-weights[n]) + values[n])
            return D[n][w]

    # the solution we are looking for
    maxval = opt(n, max_weight)

    # work backwards to retrive the item indices chosen in the optimal solution
    items = []
    n_, w_ = len(values)-1, max_weight
    while D[n_][w_]:
        # check where we came from
        if w_ - weights[n_] < 0:
            # we did not take item `n`
            n_ -= 1
        elif D[n_-1][w_] > D[n_-1][w_-weights[n_]] + values[n_]:
            # we did not take item `n`
            n_ -= 1
        else:
            # we took item `n`
            w_ -= weights[n_]
            items.append(n_)
            n_ -= 1

    return maxval, items


def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_weight = 50
    maxval, idxs = knapsack(weights, values, max_weight)
    print "Maximum value: {}".format(maxval)
    print "Values chosen: {}".format([values[i] for i in idxs])
    print "Weights chosen: {}".format([weights[i] for i in idxs])


if __name__ == '__main__':
    main()

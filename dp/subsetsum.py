def subsetsum(setofnums, value, method='recursive'):
    '''
    Given the set of nonnegative integers `setofnums` and the integer `value`,
    determine if there is a subset of element in `setofnums` that sum to `value`.

    >>> subsetsum([3, 9, 2, 1, 5], 15)
    True

    >>> subsetsum([10, 2, 8, 4, 6], 13)
    False

    '''

    def _subsetsum(n, v):
        '''
        Returns True if there is a set of numbers in `setofnums` up to index `n`
        that add to the value `v`, and False otherwise.
        '''
        if v == 0:
            # can always use 0 items to get value of 0
            return True
        elif n < 0 and v > 0:
            # cannot use 0 items to get a positive value
            return False
        else:
            # check if there is a set of items up to `n-1` that does not
            # use item `n` and adds to `v`, or if there is one to which we can
            # add ourselves to sum to the value `v`
            return _subsetsum(n-1, v) or _subsetsum(n-1, v-setofnums[n])

    def _subsetsum_bu(setofnums, value):
        '''
        Solves the problem working bottom up by starting with the base cases
        and iteratively extending optimal solutions for smaller values of `n`
        to larger values of `n`.
        '''

        # E[n][v] is True if there is a subset of `setofnums` up in index
        # `n` that adds to the value `v`, and False otherwise
        E = [[None for v in xrange(value+1)] for n in range(len(setofnums))]

        # We are recursing on n, so we need n = 0 populated
        # n = 0 corresponds to when we only have the first item, so E[n][v]
        # will be true if v == 0 or v == setofnums[n]
        for v in range(value+1):
            E[0][v] = (v == 0) or (v == setofnums[0])
        # We are also recursing on v, so we need v = 0 populated
        # E[n][0] = True for all n (can always take 0 items to have value of 0)
        for n in range(len(setofnums)):
            E[n][0] = True

        # Populate the rest of the table
        for n in range(1, len(setofnums)):
            for v in range(1, value+1):
                if v - setofnums[n] < 0:
                    E[n][v] = E[n-1][v]
                else:
                    E[n][v] = E[n-1][v] or E[n-1][v - setofnums[n]]

        # return the value we are interested in
        return E[len(setofnums)-1][value]

    # Use the specified method
    if method == 'recursive':
        return _subsetsum(len(setofnums)-1, value)
    elif method == 'bottomup':
        return _subsetsum_bu(setofnums, value)


def main():
    print subsetsum([3, 9, 2, 1, 5], 100, method='bottomup')


if __name__ == '__main__':
    main()

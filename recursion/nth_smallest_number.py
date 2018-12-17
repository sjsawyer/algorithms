def nth_smallest_number(l, n):
    ''' Return the `n`th smallest number of the list `l` in linear time

    Side effects: Mutates `l`

    >>> l = [4, 7, 1, 3, 8, 5]
    >>> nth_smallest_number(l, 2)
    3
    >>> nth_smallest_number(l, 5)
    7
    >>> nth_smallest_number(l, 10)
    None

    '''
    if len(l) < n:
        return None

    # We use two auxiliary methods to aid us

    def _partition_and_get_new_pivot_idx(i, j):
        '''
        Mutate the sublist of `l`, `l[i..j]`, so that `l[i]` is now in the
        correct location as if `l` were sorted (essentially the subroutine of
        quick sort).  The important thing to note here is that we return the
        new index of `l[i]`
        '''
        pivot = l[i]
        swap_idx = i+1
        for j in range(i+1, j+1):
            if l[j] < pivot:
                l[j], l[swap_idx] = l[swap_idx], l[j]
                swap_idx += 1
        new_pivot_idx = swap_idx - 1
        l[i], l[new_pivot_idx] = l[new_pivot_idx], l[i]
        return new_pivot_idx

    def _nth_smallest_number(i, j, n):
        '''
        Return the `n`th smallest number from `l[i..j]` (`j` inclusive),
        where `n=0` corresponds to the smallest number, `n=1` the second
        smallest, etc.
        '''
        # first, we correctly place the ith element of l to find the mth
        # smallest number, where m could be anything between i and j
        correct_idx = _partition_and_get_new_pivot_idx(i, j) - i
        # subtract one because of zero indexing
        if correct_idx == n:
            # We are done
            return l[correct_idx + i]
        elif correct_idx > n:
            # The element we seek lies to the left
            return _nth_smallest_number(i, correct_idx-1, n)
        else:
            # The element we seek lies to the right, so we want to find the
            # (n-correct_idx-1)th smallest number in the right sublist
            return _nth_smallest_number(correct_idx+i+1, j, n-correct_idx-1)

    # now consider n as being 0 indexed
    return _nth_smallest_number(0, len(l)-1, n-1)


def main():
    tests = [
        {'l': [4, 8, 3, 9, 7, 1, 5],
         'n': 5,
         'answer': 7},

        {'l': [8, 7, 6, 5, 4, 3, 1],
         'n': 2,
         'answer': 3},

        {'l': [1, 2, 3, 4, 5],
         'n': 4,
         'answer': 4},

        {'l': [3, 4, 1, 6, 9],
         'n': 5,
         'answer': 9},

        {'l': [3, 7, 3, 5, 8, 5, 2],
         'n': 4,
         'answer': 5},

        {'l': [1, 2, 3],
         'n': 10,
         'answer': None},
    ]

    for test in tests:
        print "l={}, n={}, expected={}, actual={}".format(
            test['l'], test['n'], test['answer'],
            nth_smallest_number(test['l'], test['n']))


if __name__ == '__main__':
    main()

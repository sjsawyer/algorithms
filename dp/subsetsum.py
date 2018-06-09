def subsetsum(setofnums, value):
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

    return _subsetsum(len(setofnums)-1, value)


def main():
    print subsetsum([3, 9, 2, 1, 5], 15)


if __name__ == '__main__':
    main()

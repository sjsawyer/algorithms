import sys


def maximal_subsequence(l):
    '''
    Returns the sum of the maximal subsequence of l, where the maximal
    subsequence is defined as the sequence of elements in l from index i to
    index j such that the sum is maximized, as well as the corresponding `i`
    and `j`

    >>> maximal_subsequence([2, -5, -6, 7, 12, -4, -3, 8, -1])
    20, 3, 7

    '''

    def _best_max_sub_from_m(m):
        '''
        Find the maximal subsequence in `l` such that the leftmost index `i`
        satsfies `i<=m` and the rightmost index 'j' satisfies `j>m`, and
        returns the sum, `i` and `j`
        '''
        # leftmost
        cumsum_l, bestsofar_l, besti = 0, -sys.maxint, m
        for i in xrange(m, -1, -1):
            cumsum_l += l[i]
            if cumsum_l >= bestsofar_l:
                bestsofar_l = cumsum_l
                besti = i
        # rightmost
        cumsum_r, bestsofar_r, bestj = 0, -sys.maxint, m+1
        for j in xrange(m+1, len(l)):
            cumsum_r += l[j]
            if cumsum_r >= bestsofar_r:
                bestsofar_r = cumsum_r
                bestj = j
        # combine
        return bestsofar_l + bestsofar_r, besti, bestj

    def _max_sub_helper(i, j):
        '''
        Finds the maximal subsequence of `l` which starts at index
        `i` and ends at index `j`, as well as the start and ending indices
        '''
        if i == j:
            return l[i], i, j
        # Divide the list in half. Then the maximal subsequence can be expressed
        # as the maximum of the maximal subsequence contained in the leftmost
        # half, the maximal subsequence contained in the rightmost half, and the
        # maximal subsequence which starts in the leftmost half and ends in the
        # rightmost half
        m = (i + j)/2
        leftmaxsubsum, li, lj = _max_sub_helper(i, m)
        rightmaxsubsum, ri, rj = _max_sub_helper(m+1, j)
        midmaxsubsum, mi, mj = _best_max_sub_from_m(m)
        return max((leftmaxsubsum, li, lj),
                   (rightmaxsubsum, ri, rj),
                   (midmaxsubsum, mi, mj))

    return _max_sub_helper(0, len(l)-1)



def main():
    seq = [2, -5, -6, 7, 12, -4, -3, 8, -1]
    sum, i, j = maximal_subsequence(seq)
    print "Maximal subsequence of {}:".format(seq)
    print "Sum: {}, i: {}, j: {}".format(sum, i, j)
    print "Subsequence: {}".format(seq[i:j+1])


if __name__ == '__main__':
    main()

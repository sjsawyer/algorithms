def longest_contiguous_subsequence(s1, s2):
    '''
    Returns the longest contiguous subsequence between sequences `s1` and `s2`

    >>> s1 = [5, 7, 3, 1, 2, 3, 8, 4]
    >>> s2 = [9, 1, 2, 3, 7, 6]
    >>> longest_contiguous_subsequence(s1, s2)
    [1, 2, 3]

    '''

    l1 = len(s1)  # m
    l2 = len(s2)  # n

    # Let L[m][n] be the length of the longest contiguous subsequence ending
    # at element `m-1` in `s1` and `n-1` in `s2`
    L = [[None for n in xrange(l2+1)] for m in xrange(l1+1)]

    # longest contiguous subsequences of any position of a sequence and an
    # empty sequence is 0 length
    for m in xrange(l1+1):
        L[m][0] = 0
    for n in xrange(l2+1):
        L[0][n] = 0

    max_len = 0
    m_max, n_max = None, None
    for m in xrange(1, l1+1):
        for n in xrange(1, l2+1):
            if s1[m-1] != s2[n-1]:
                L[m][n] = 0
            else:
                L[m][n] = 1 + L[m-1][n-1]
                # keep track of max len
                if L[m][n] > max_len:
                    max_len = L[m][n]
                    m_max, n_max = m, n
    # The longest contiguous subseqence ends at `m_max-1` in `s1` and has a
    # length of `max_len`
    if m_max is None:
        # no contiguous sequence found
        return []
    else:
        return s1[m_max-max_len:m_max]


def main():
    s1 = [5, 7, 9, 1, 2, 3, 8, 4]
    s2 = [9, 1, 2, 3, 7, 6]
    print longest_contiguous_subsequence(s1, s2)


if __name__ == '__main__':
    main()

def lcs(s1, s2):
    '''
    Return the longest common subsequence of `s1` and `s2`

    >>> lcs([5, 1, 4, 7, 2, 6], [3, 1, 4, 8, 6])
    [1, 2, 6]

    '''

    l1 = len(s1)  # m
    l2 = len(s2)  # n

    # L[m][n] = length of lcs using s1[0,..,m-1] and s2[0,..,n-1]
    # NOTE: L[m][n] corresponds to s1[m-1], s2[n-1]
    L = [[None for n in xrange(l2+1)] for m in xrange(l1+1)]

    # Base cases
    # if one of the sequences is empty, return 0
    for m in range(l1+1):
        L[m][0] = 0
    for n in range(l2+1):
        L[0][n] = 0

    # Populate the rest of the table
    for m in range(1, l1+1):
        for n in range(1, l2+1):
            if s1[m-1] == s2[n-1]:
                L[m][n] = 1 + L[m-1][n-1]
            else:
                L[m][n] = max(L[m-1][n], L[m][n-1])

    # length of the longest common subsequence
    lcs_len = L[l1][l2]

    # work backwards to find the corresponding subsequence
    seq = [None for i in range(lcs_len)]
    current_seq_idx = lcs_len-1
    m, n = l1, l2
    while L[m][n]:
        if L[m-1][n] < L[m][n]:
            # we used s1[m-1]
            seq[current_seq_idx] = s1[m-1]
            m -= 1
            current_seq_idx -= 1
        elif L[m][n-1] > L[m][n]:
            # we used s2[n-1]
            seq[current_seq_idx] = s2[n-1]
            n -= 1
            current_seq_idx -= 1
        else:
            # we did not use s1[m-1] nor s2[n-1]
            m -= 1
            n -= 1

    return seq


def main():
    s1 = [5, 1, 4, 7, 2, 6]
    s2 = [3, 1, 4, 8, 6]
    seq = lcs(s1, s2)
    print s1
    print s2
    print "LCS: {}".format(seq)


if __name__ == '__main__':
    main()

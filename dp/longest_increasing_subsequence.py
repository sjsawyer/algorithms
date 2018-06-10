def longest_increasing_subsequence(s):
    '''
    Return the longest increasing subsequence in s.

    >>> s = [-3, 7, 1, 3, 5, 9, 2, 12, -5, 7]
    >>> longest_increasing_subsequence(s)
    [-3, 1, 3, 5, 9, 12]

    NOTE: Implementation with DP is O(n**2), which is not the most efficient

    '''

    l = len(s)
    # edge case
    if l == 0:
        return 0

    # Let L[m] be the length of the longest increasing subsequence in `s`
    # where the last element in the sequence is `s[m]`
    L = [None for m in range(l)]

    # LIS of a sequence of length 1 is 1
    L[0] = 1

    # Populate the rest of the table and keep track of the max LIS length
    max_lis = 1
    max_m = 0
    for m in range(1, l):
        # need to find the element j < m where s[j] < s[m] and
        # L[j] is maximized
        current_lis = 0
        for j in range(0, m):
            if s[j] < s[m] and L[j] > current_lis:
                current_lis = L[j]
        L[m] = current_lis + 1
        # keep track of max lis
        if L[m] > max_lis:
            max_lis = L[m]
            max_m = m

    # reconstruct the LIS from the table `L`
    lis = [None for i in range(max_lis)]
    current_m = max_m
    prev_m = current_m - 1
    remaining_lis = max_lis - 1
    lis[remaining_lis] = s[current_m]
    while remaining_lis:
        if L[current_m] == L[prev_m] + 1 and s[current_m] > s[prev_m]:
            # we came from s[`prev_m`]
            remaining_lis -= 1
            lis[remaining_lis] = s[prev_m]
            current_m = prev_m
            prev_m -= 1
        else:
            # we did not come from s[`prev_m`], consider the one before
            prev_m -= 1

    return lis


def main():
    s = [-3, 7, 1, 3, 5, 9, 2, 12, -5, 7]
    print s
    print "LIS: {}".format(longest_increasing_subsequence(s))


if __name__ == '__main__':
    main()

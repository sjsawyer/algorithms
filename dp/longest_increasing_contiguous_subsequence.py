def longest_increasing_contiguous_subsequence(s):
    '''
    Return the longest increasing subsequence in s.

    >>> s = [-3, 7, 1, 3, 5, 9, -5, 7]
    >>> longest_increasing_contiguous_subsequence(s)
    [1, 3, 5, 9] 

    '''

    l = len(s)
    # Let L[m] be the length of the longest increasing subsequence in `s`
    # where the last element in the sequence is `s[m-1]`
    L = [None for m in range(l+1)]

    # LIS of an empty sequence is 0
    L[0] = 0
    # LIS of a sequence of length 1 is 1
    L[1] = 1

    # Populate the rest of the table and keep track of the max len
    max_len = 0
    m_max = None
    for m in range(2, l+1):
        if s[m-1] > s[m-2]:
            L[m] = 1 + L[m-1]
        else:
            L[m] = 1
        # keep track of max
        if L[m] > max_len:
            max_len = L[m]
            m_max = m
    
    return s[m_max - max_len: m_max]



def main():
    s = [-3, 7, 1, 3, 5, 9, -5, 7]
    print longest_increasing_subsequence(s)


if __name__ == '__main__':
    main()

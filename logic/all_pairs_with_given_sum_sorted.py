'''
Q: Given a sorted array `l` and integer `k`, find all pair of elements in `l`
   that add to the given integer `k`. Assume the elements of l are unique.

A: Using the fact that `l` is sorted, we can use a two pointer method to
   achieve O(n) runtime.

'''


def find_sum_pairs(l, k):
    '''
    Examples:
    >>> find_sum_pairs([2, 4, 5, 6, 7, 8, 10], 12)
    [(2, 10), (4, 8), 5, 7)]
    >>> find_sum_pairs([3, 6, 9], 8)
    []

    '''
    sum_pairs = []
    i, j = 0, len(l)-1
    while i < j:
        if l[i] + l[j] > k:
            j -= 1
        elif l[i] + l[j] < k:
            i += 1
        else:
            sum_pairs.append((l[i], l[j]))
            # if elements in l were NOT unique, we could check if
            # l[i+1] == l[i] and l[j-1] == l[j] here
            i += 1
            j -= 1
    return sum_pairs


def main():
    l = [-4, -2, 0, 3, 5, 6, 8, 9]
    k = 8
    print "Sorted list: {}".format(l)
    print "Desired sum: {}".format(k)
    print "All sum pairs: {}".format(find_sum_pairs(l, k))


if __name__ == '__main__':
    main()

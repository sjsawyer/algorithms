'''
Q: Given an unsorted array `l` and integer `k`, find all pair of elements in `l`
   that add to the given integer `k`. Assume the elements of l are unique.

A: We can iterate through the list linearly, and for each element `l[i]` we
   know that we are looking for the element `k-l[i]`. As such, we can store
   this value in a hash set and on each new element `l[i]`, check to see if
   we are in the set.

   Note: If the elements in `l` were not unique, we could use a hash map
   (e.g. dict()) instead of a set, and initialize each value we add to 0.
   Then, if we find out we exist in the set of keys, we can increment
   the value by 1.

'''


def find_sum_pairs(l, k):
    '''
    Examples:
    >>> find_sum_pairs([10, 4, 5, 6, 8, 7, 2], 12)
    [(2, 10), (4, 8), 5, 7)]
    >>> find_sum_pairs([3, 6, 9], 8)
    []

    '''
    sum_pairs = []
    differences_so_far = set()
    for num in l:
        if num in differences_so_far:
            sum_pairs.append((num, k-num))
        else:
            differences_so_far.add(k-num)
    return sum_pairs


def main():
    l = [-2, 6, 0, 3, 5, 8, 9, -4]
    k = 8
    print "Unsorted list: {}".format(l)
    print "Desired sum: {}".format(k)
    print "All sum pairs: {}".format(find_sum_pairs(l, k))


if __name__ == '__main__':
    main()

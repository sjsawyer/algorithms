'''
Q: Given a sorted array `l` and integer `k`, a pair of elements in `l` whose
   sum is closest to `k`
A: Using the fact that `l` is sorted, we can use a two pointer method to
   achieve O(n) runtime, very similar to finding all pairs with a given sum.

'''
import sys


def find_closest_pair(l, k):
    '''
    Examples:
    >>> find_closest_pair([2, 4, 5, 8, 10], 16)
    (5, 10)

    '''
    i, j = 0, len(l)-1
    best_diff = sys.maxint
    best_i, best_j = None, None
    while i < j:
        cur_sum = l[i] + l[j]
        diff = cur_sum - k
        if abs(diff) < best_diff:
            best_diff = abs(diff)
            best_i, best_j = i, j
        if diff > 0:
            j -= 1
        else:
            i += 1
    return l[best_i], l[best_j]




def main():
    l = [2, 4, 5, 8, 10]
    k = 16
    print "Sorted list: {}".format(l)
    print "Desired sum: {}".format(k)
    print "Closest pair: {}".format(find_closest_pair(l, k))


if __name__ == '__main__':
    main()

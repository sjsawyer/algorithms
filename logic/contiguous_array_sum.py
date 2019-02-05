'''
Q: Given an array of integers (positive or negative) `a` and an integer `s`,
   determine the number of contiguous sub-arrays of `a` whose elements sum
   to `s`. For example, if `a=[4, 2, -5, 6, 3, -8, 1, 9]` and `s=1`, then the
   contiguous sub-arrays that sum to 1 are
       [4, 2, -5]
       [-5, 6]
       [6, 3, -8]
       [1]
   so we should return 4.

A: Naive solution would be to generate all contiguous sub-arrays, and determine
   which ones sum to the desired sum. If `n` is the length of the array `a`,
   then we can generate all contiguous subsequences by looping through `i` from
   1 to n, and `j` from `i` to `n`.  This creates n^2 sequences, and summing
   each sequence takes `j-i` time, which (after some math) results in an O(n^3)
   running time algorithm.

   A better solution is to iterate over the array, keeping track of the sum of
   elements so far.  At each element `a[i]`, add the sum of elements
   `s_current` from indices 0 to `i` into a hash map, and check to see if
   `s_current` - `s` is already in the hash map. If it is, then we have another
   contiguous sub array that sums to `s`.

'''


def contiguous_array_sum(a, s):
    '''
    Returns the number of contiguous subarrays of `a` that sum to `s`

    >>> contiguous_array_sum([4, 2, -5, 6, 3, -8, 1, 9], 1)
    4
    >>> contiguous_array_sum([4, 2, 7, 5, 6], 9)
    1
    >>> contiguous_array_sum([5, 3, 1], 7)
    0

    '''
    # Store the total sums of elements up to each index
    # So a key of 10 that maps to 2 means we have seen the sum 10 twice so far
    sum_map = {}
    # Add a sum of 0 to the map, indicating the beginning of the list
    sum_map[0] = 1
    # variable to keep track of the sum
    sum_so_far = 0
    # what we will return
    n_contiguous_sum_arrays = 0

    for i in range(0, len(a)):
        sum_so_far += a[i]
        # add/update the number of occurrences of this sum so far
        sum_map[sum_so_far] = sum_map.get(sum_so_far, 0) + 1
        # check if the difference of where we are now minus the desired sum is
        # in the map
        if (sum_so_far - s) in sum_map:
            # We have a subarray sum
            n_contiguous_sum_arrays += sum_map[sum_so_far - s]

    return n_contiguous_sum_arrays


def main():
    assert contiguous_array_sum([4, 2, -5, 6, 3, -8, 1, 9], 1) == 4
    assert contiguous_array_sum([4, 2, 7, 5, 6], 9) == 1
    assert contiguous_array_sum([5, 3, 1], 7) == 0
    print contiguous_array_sum([4, 0, 2], 0)


if __name__ == '__main__':
    main()

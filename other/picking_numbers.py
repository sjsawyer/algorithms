'''
Q: Given an array of integers, find and print the maximum number of integers
   you can select from the array such that the absolute difference between any
   two of the chosen integers is less than or equal to 1. For example, if your
   array is [1, 1, 2, 2, 4, 4, 5, 5, 5], you can create two subarrays meeting
   the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray
   has 5 elements.

   Constraint on the array `a`: 0 < a[i] < 100

'''


def pickingNumbers(a):
    '''
    Return the length of the longest subsequences in `a` satisfying the above
    constraints, in linear time.

    '''
    # We use the constraint on the array `a` to keep track of the frequency
    # of each element in a
    # freq[n] is frequency for number n+1
    freq = [0 for _ in range(99)]
    for element in a:
        freq[element-1] += 1
    # The two neighbouring elements in `freq` whose sum is greatest give us
    # our solution
    max_sum = 0
    for i in range(len(freq)-1):
        max_sum = max(max_sum, freq[i] + freq[i+1])

    return max_sum


def main():
    a = [4, 6, 5, 3, 3, 1]
    print "Array: {}".format(a)
    print "max subset: [4, 3, 3] => expected length 3"
    print "Computed length: {}".format(pickingNumbers(a))


if __name__ == '__main__':
    main()

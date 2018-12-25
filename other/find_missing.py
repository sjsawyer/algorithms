'''
Q: Given two arrays `arr1` and `arr2` containing positive integers, where
   `arr1` and `arr2` contain the same elements except for the fact that `arr2`
   is missing one element from `arr1`, find the missing element (the elements
   do not have to occur in the same order in both arrays)

A: Naive solutions include sorting both arrays and using a two pointer method,
   and using a hash set and set difference. A better solution is to notice
   that, with the restriction that all elements are positive integers, the
   difference between the sum of the elements in `arr1` and the sum of the
   elements in `arr2` will yield the missing number.

   One should also note that the length of the arrays is not bounded, nor are
   the size of the integer elements. Thus, it is possible in languages that
   use static types for the sum of all elements in one array to overflow.
   We can circumvent this potential issue by noticing that the sum and
   difference of elements of both arrays can be taken in any order we wish, so
   we do it such that the sum/difference never exceeds the value of the
   greatest element of both arrays.

   NOTE: There is also the solution of XORing all of the elements together to
   yield the missing element, which will also work with negative numbers.

'''
import sys


def find_missing(arr1, arr2):
    '''
    Given two lists of integers `arr1` and `arr2` of lengths `n` and `n+1`,
    where the elements of `arr1` are a subset of `arr2`, return the element
    in `arr2` that is missing from `arr1`.

    >>> find_missing([4, 6, 1, 3, 0], [6, 1, 5, 0, 3, 4])
    5

    '''
    assert len(arr1) + 1 == len(arr2)
    # Running total of the sum/diffeence
    s = 0
    # Keep track of the absolute value of the running total
    max_sum = -sys.maxint
    # Pointers to indices of `arr1` and `arr2`
    i1, i2 = 0, 0
    # Sum all elements of `arr2` and subtract all elements of `arr1`
    while i1 < len(arr1) and i2 < len(arr2):
        if s > 0:
            s -= arr1[i1]
            i1 += 1
        else:
            s += arr2[i2]
            i2 += 1
        max_sum = max(max_sum, abs(s))
    # Ensure we've used all elements
    while i1 < len(arr1):
        s -= arr1[i1]
        i1 += 1
        max_sum = max(max_sum, abs(s))
    while i2 < len(arr2):
        s += arr2[i2]
        i2 += 1
        max_sum = max(max_sum, abs(s))
    return s, max_sum


def main():
    test1 = {'arr1': [4, 6, 1, 3, 0],
             'arr2': [6, 1, 5, 0, 3, 4],
             'ans': 5}
    m = sys.maxint
    test2 = {'arr1': [m - i for i in range(100)],
             'arr2': [m - i for i in range(100)] + [m - 200],
             'ans': m - 200}

    for test in (test1, test2):
        arr1, arr2, ans = test['arr1'], test['arr2'], test['ans']
        print "arr1: {}".format(arr1)
        print "arr2: {}".format(arr2)
        print "expected: {}".format(ans)
        print "actual:   {}\n".format(find_missing(arr1, arr2))


if __name__ == '__main__':
    main()

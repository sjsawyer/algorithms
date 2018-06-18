def sum_and_sum_of_squares_of_digits(a, b):
    '''
    Returns the smallest number, of fewer than 100 digits, whose digits sum to
    be `a` and whose squares of digits sum to be `b`.

    Returns None if no number fewer than 100 digits exist.

    >>> sum_and_sum_of_squares_of_digits(6, 14)
    123

    '''

    # We will use D[a][b] to represent the minimum number of digits needed
    # whose sum is `a` and sum of squares is `b`
    # Because our number is at most 100 digits long, the maximum sum can be
    # 9*100 and the maximum sum of squares can be (9**2)*100
    # Our table should thus be 901x8101 (first index of each dimension to be
    # used for when the sums are both 0, representing a valid solution in our
    # recursive algorithm)
    D = [[None for _ in range(8101)] for _ in range(901)]

    # We then have the recursive relation
    # D[a][b] = 1 + min( D[a-i][b-i**2], i=1..9 )
    # Because our array is quite large, we will use a top down approach

    max_digits = 100

    def _numofdigits(a_, b_):
        '''
        Return the smallest number whose digits sum to `a_` and whose squares
        of digits sum to `b_`, using the table `D` for memoization.

        '''
        # Invalid condition
        if a_ < 0 or b_ < 0:
            return max_digits
        # Memoization
        if D[a_][b_] is not None:
            return D[a_][b_]
        # Condition satisfied
        if a_ == 0 and b_ == 0:
            D[a_][b_] = 0
            return D[a_][b_]
        # Recurse
        D[a_][b_] = 1 + min(_numofdigits(a_ - i, b_ - i**2)
                            for i in range(1, 10))
        return D[a_][b_]

    # Minimum number of digits needed
    numdigits = _numofdigits(a, b)

    # Return None if no solution fewer than 101 digits found
    if numdigits > max_digits:
        return None

    # Work backwards to construct the number of minimum digits
    digit_list = []
    a_, b_ = a, b
    while D[a_][b_] != 0:
        for i in range(1, 10):
            if 1 + D[a_-i][b_-i**2] == D[a_][b_]:
                digit_list.append(i)
                a_ -= i
                b_ -= i**2
                break
    # We want the smallest number, so sort the digits
    digit_list.sort()
    # Return as an int
    digit = reduce(lambda x, y: 10*x + y, digit_list)

    return digit


def main():
    ex1 = (6, 14, sum_and_sum_of_squares_of_digits(6, 14))
    ex2 = (20, 30, sum_and_sum_of_squares_of_digits(20, 30))
    ex3 = (20, 31, sum_and_sum_of_squares_of_digits(20, 31))
    ex4 = (18, 162, sum_and_sum_of_squares_of_digits(18, 162))
    print "Sum to {}, squares sum to {}: {}".format(*ex1)
    print "Sum to {}, squares sum to {}: {}".format(*ex2)
    print "Sum to {}, squares sum to {}: {}".format(*ex3)
    print "Sum to {}, squares sum to {}: {}".format(*ex4)


if __name__ == '__main__':
    main()

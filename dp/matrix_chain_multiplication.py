'''
Q: Given a sequence of matrices to be multiplied, determine the order in which
   to conduct the multiplications so that the total number of arithmetic
   operations needed to compute the product is minimized.

   E.g. A is 10 x 30, B is 30 x 5, C is 5 x 60
        (AB)C requires (10*30*5) + (10*5*60) = 4500 operations
        A(BC) requires (30*5*60) + (10*30*60) = 27000 operations

A: To multiply n matrices, there are n-1 ways to place the outermost brackets.
   E.g., for 4 matrics ABCD, we have the following options:
       A(BCD), (AB)(CD), (ABC)D
   Note after placing the brackets, we have to repeat the same procedure on the
   remaining matrices left to be grouped. That is, we create more subproblems
   for ourselves, allowing for a recursive solution. We consider number of
   operations needed for all n-1 placements, and take the minimum of this.

   Let min_num_ops(i, j) be the minimum number of arithmetic operations needed
   to multiply matrices i to j in the chain.

       min_num_ops(1, n) =
           min value for k over 1 < k < n of
               min_num_ops(1, k) + ...
               min_num_ops(k+1, n) + ...
               firstDimension(matrix 1)*secondDimension(matrix k)*secondDimension(matrix n)

'''
import sys


def matrix_chain_multiplication(dims):
    '''
    Given a list `dims` of length n+1 representing a chain of n matrices such
    that the ith matrix is of dimensions dims[i] x dims[i+1], find the minimum
    number of arithmetic operations needed to multiply the chain.

    >>> matrix_chain_multiplication([40, 20, 30, 10, 30])
    26000

    For the above example, we have 4 matrices A 40x20, B 20x30, C 30x10,
    and D 10x20, which can be grouped and multiplied together as A((BC)D)
    for a total of 20*30*10 + 20*10*20 + 40*20*20 = 26000 operations.

    '''
    # dp[i][j] will be the minimum number of operations needed to multiply
    # matrices i, i+1, ..., j-1, j
    # if len(dims) == n, then we have n-1 matrices
    n_matrices = len(dims)-1
    dp = [[None for _ in range(n_matrices)]
          for _ in range(n_matrices)]

    def _min_num_ops(i, j):
        '''
        Returns the minimum number of operations needed to multiply matrices i
        through j, storing and using previously computed values in `dp`

        '''
        if dp[i][j]:
            # We have already calculated this value
            return dp[i][j]
        if j == i:
            # Base case: 1 matrix, no operations needed
            dp[i][j] = 0
            return dp[i][j]
        min_ops = sys.maxint
        # Try all ways to place the outer most set of brackets
        for k in range(i, j):
            if dp[i][k] is None:
                dp[i][k] = _min_num_ops(i, k)
            if dp[k+1][j] is None:
                dp[k+1][j] = _min_num_ops(k+1, j)
            # Number of operations needed for this placement of k
            # Need first dimension of i, 2nd dimension of k, and 2nd dimension
            # of j
            ops = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
            # Update current min value
            min_ops = min(min_ops, ops)
        dp[i][j] = min_ops
        return dp[i][j]

    # The value we are interested in
    return _min_num_ops(0, n_matrices-1)


def main():
    dimss = [[20, 30],
             [30, 10, 20],
             [40, 20, 30, 10, 30]]
    min_opss = [0, 6000, 26000]
    for dims, min_ops in zip(dimss, min_opss):
        print "Matrix dimensions: {}".format(dims)
        print "Excepted number of operations: {}".format(min_ops)
        print "Calculated: {}\n".format(matrix_chain_multiplication(dims))


if __name__ == '__main__':
    main()

def num_ways_to_ascend_stairs(n, m):
    '''
    Return the number of ways to ascend n stairs by taking steps of size
    1, 2, ..., m.

    Recursive tree has m branches, with depth n

    Runtime: O(m^n)
    Space: O(n) due to recursion in tree of depth n

    '''
    # Base cases
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Compute for each step size from here
    total_ways = 0
    for i in range(1, m+1):
        total_ways += num_ways_to_ascend_stairs(n-i, m)
    return total_ways


def num_ways_to_ascend_stairs_memoized(n, m):
    '''
    Memoized Approach

    Runtime: O(n*m)
    Space: O(n)

    '''
    # Let memo[i] be the number of ways for i stairs remaining
    memo = [None for i in range(n+1)]
    # Initialize
    memo[0] = 1
    # Populate the table bottom up
    for n_stairs_remaining in range(1, n+1):
        total_from_here = 0
        for step_size in range(1, m+1):
            if n_stairs_remaining - step_size >= 0:
                total_from_here += memo[n_stairs_remaining - step_size]
        # memoize current state
        memo[n_stairs_remaining] = total_from_here
    # we are done, return the value we are interested in
    return memo[n]


def main():
    for n_stairs in 0, 1, 5, 10:
        for step_sizes in [1, 2, 3, 4]:
            sol = num_ways_to_ascend_stairs(n_stairs, step_sizes)
            assert sol == num_ways_to_ascend_stairs_memoized(n_stairs,
                                                             step_sizes)
            print "n={}, m={}  ans: {}".format(n_stairs, step_sizes, sol)


if __name__ == '__main__':
    main()

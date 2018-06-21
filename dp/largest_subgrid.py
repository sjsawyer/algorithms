def largest_grid_size(grid):
    '''
    Returns the largest subgrid of grid whose elements contain only 1s

    Parameters:
    -----------
    grid: lists of lists, where each sublist is of the same size, and whose
          elements are either 1 or 0

    Returns:
    ------------
    size (int) of the largest subgrid whose elements are only 1s

    '''
    # Create a table `dp` the same size as grid, where dp[i][j] is the size of
    # the largest subgrid of `grid` of all ones whose bottom right entry is at
    # grid[i][j]
    dp = [[None for j in range(len(grid[0]))] for i in range(len(grid))]
    
    # initialize first row and column
    for i in range(len(grid)):
        dp[i][0] = grid[i][0]
    for j in range(len(grid[0])):
        dp[0][j] = grid[0][j]

    # fill in the rest of the subgrid sums
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    # find max of the dp table
    max_grid_size = max(max(row) for row in dp)
    return max_grid_size


def main():
    grid = [[0, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 0]]
    print largest_grid_size(grid)


if __name__ == '__main__':
    main()

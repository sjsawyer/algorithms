'''
Q: Given a grid which has a color in each square, find the largest number of
   squares which have the same color and are adjacent to each other (either
   horizontally or vertically, not diagonally.

   E.g. -----------------
        | B | G | Y | R |
        -----------------
        | B | Y | Y | R |
        -----------------
        | G | G | Y | O |
        -----------------
        | G | B | O | R |
        -----------------

    There are 4 (Y)ellow squares adjacent to each other, and this is the max.

'''

def max_adjacent_colors(grid):
    '''
    Return the largest number of squares which have the same color and are
    adjacent to each other

    '''
    # dp[i][j] stores the greatest number of squares that are adjacent
    # to grid[i][j] (including itself), using only the subgrid
    # grid[0..i][0..j]
    dp = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Keep track of the max number of squares and corresponding color
    max_adjacent, color = dp[0][0], grid[0][0]

    # Populate the rest of the table, bottom up
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i > 0 and grid[i-1][j] == grid[i][j]:
                dp[i][j] += dp[i-1][j]
            if j > 0 and grid[i][j-1] == grid[i][j]:
                dp[i][j] += dp[i][j-1]
            if dp[i][j] > max_adjacent:
                max_adjacent = dp[i][j]
                color = grid[i][j]

    # Return the color and the largest number of adjacent colors.
    return max_adjacent, color


def main():
    grid = [['B', 'G', 'Y', 'R'],
            ['B', 'Y', 'Y', 'R'],
            ['G', 'G', 'Y', 'O'],
            ['G', 'B', 'O', 'R']]

    print max_adjacent_colors(grid)


if __name__ == '__main__':
    main()

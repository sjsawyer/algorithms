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

    The idea is to start at a square in the grid and see how many neighbours
    we can recursively expand to that have the same color, and keep track of
    this value. To ensure we do not revisit neighbours we have seen before,
    we store the coordinates of squares we have seen before in an auxillary
    grid storing binary values the same size as `grid`

    '''
    seen = [[False for _ in range(len(grid[0]))]
            for _ in range(len(grid))]

    def _get_samecolor_neighbours(i, j):
        color = grid[i][j]
        neighbours = set()
        # loop over adjacent neighbours
        for (ni, nj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            # invalid conditions, out of bounds or are ourselves
            if ni < 0 or nj < 0 or ni > len(grid)-1 or nj > len(grid[0])-1:
                pass
            elif grid[ni][nj] == color:
                neighbours.add((ni, nj))
        return neighbours

    def _mac(i, j):
        mac = 0
        if seen[i][j]:
            return 0
        else:
            # count ourselves
            mac += 1
            seen[i][j] = True
            # count our neighbours
            for (ni, nj) in _get_samecolor_neighbours(i, j):
                if not seen[ni][nj]:
                    mac += _mac(ni, nj)
            return mac

    # Perform DFS
    max_mac, color = 0, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            mac = _mac(i, j)
            if mac > max_mac:
                max_mac = mac
                color = grid[i][j]

    return max_mac, color


def main():
    grid1 = [['B', 'G', 'Y', 'R'],
             ['B', 'Y', 'Y', 'R'],
             ['G', 'G', 'Y', 'O'],
             ['G', 'B', 'O', 'R']]

    grid2 = [['B', 'B'],
             ['B', 'B']]

    grid3 = [['Y', 'Y', 'Y', 'Y'],
             ['Y', 'R', 'R', 'Y'],
             ['Y', 'Y', 'Y', 'Y']]

    grid4 = [['R', 'G'],
             ['G', 'R']]

    grid5 = [['P', ]]

    for grid in (grid1, grid2, grid3, grid4, grid5):
        print max_adjacent_colors(grid)


if __name__ == '__main__':
    main()

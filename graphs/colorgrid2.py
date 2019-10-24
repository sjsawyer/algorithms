'''
Q: Given a grid which has a color in each square, return the total number of
   clusters there are of each color, where a cluster should be considered a
   group of same colored cells connected either horizontally or vertically (but
   not diagonally)

   E.g. -----------------
        | B | G | Y | R |
        -----------------
        | B | Y | Y | R |
        -----------------
        | G | G | Y | O |
        -----------------
        | G | B | O | R |
        -----------------

    There are 2 clusters of (B)lue,
              2 clusters of (G)reen,
              2 clusters of (R)ed,
              2 clusters of (O)range,
              1 cluster of (Y)ellow

'''
from collections import defaultdict


def _get_nbrs((row, col), grid, color):
    ''' Find cells adjacent to `(row, col)` of the same color '''
    nbrs = set()
    for (i, j) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nbr_i, nbr_j = row + i, col + j
        if any((nbr_i < 0,
                nbr_j < 0,
                nbr_i == len(grid),
                nbr_j == len(grid[0]))):
            # out of bounds square
            continue
        if grid[nbr_i][nbr_j] == color:
            # an adjacent cell of the same color
            nbrs.add((nbr_i, nbr_j))
    return nbrs


def _mark_connected_seen((row, col), color, seen, grid):
    '''
    Mark all cells belonging to same color cluster as the cell at
    `(row, col)` as seen
    '''
    to_visit = [(row, col)]
    # visit in DFS manner
    while to_visit:
        (cell_row, cell_col) = to_visit.pop()
        if seen[cell_row][cell_col]:
            # we've been here
            continue
        # we haven't been here
        seen[cell_row][cell_col] = True
        # add all adjacent squares of same color to to_visit
        nbrs = _get_nbrs((cell_row, cell_col), grid, color)
        to_visit.extend(nbrs)
    return seen


def count_connected_colors(grid):
    '''
    `grid` is a list of list of characters, where each character
    represents a color
    '''
    n_rows = len(grid)
    n_cols = len(grid[0])
    seen = [[False for _ in range(n_cols)]
            for _ in range(n_rows)]
    color_count = defaultdict(lambda: 0)
    # iterate over entire grid
    for row in range(n_rows):
        for col in range(n_cols):
            if seen[row][col]:
                continue
            else:
                color = grid[row][col]
                color_count[color] += 1
                # mark all squares adjacent to this one seen
                seen = _mark_connected_seen((row, col), color, seen, grid)
    # return mapping, cast from defaultdict to dict
    return dict(color_count)


def main():
    grids = (
        [['b', 't', 'r', 'b', 'b'],
         ['b', 'r', 'b', 'r', 'b']],

        [['a', 'a', 'a'],
         ['a', 'b', 'a'],
         ['a', 'a', 'a']],

        [['r']],

        [[]]
    )

    for grid in grids:
        # print grid to screen
        print "\n".join(" ".join(grid[i])
                        for i in range(len(grid)))
        print count_connected_colors(grid)
        print


if __name__ == '__main__':
    main()

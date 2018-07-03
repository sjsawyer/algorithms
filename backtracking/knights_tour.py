'''
Q: Given a n x n chess board, generate a path for a knight to take so that it
   visits every square only once on the chess board, if possible.

A: Can use backtracking. The below implementation does not make any further
   simplifications to the problem besides checking whether or not moves are
   indeed valid.

   For an 8x8 board, the below implementation will find the following solution:

       0 11  8  5  2 13 16 19
       9  6  1 12 17 20  3 14
      30 27 10  7  4 15 18 21
      63 24 31 28 35 22 47 44
      32 29 26 23 48 45 36 57
      25 62 51 34 39 56 43 46
      52 33 60 49 54 41 58 37
      61 50 53 40 59 38 55 42

'''


def knights_tour(board):
    '''
    Populate an empty chessboard with numbers i from 0 to (mxn)-1, where m
    and n are the length and width of the board, and the location of i
    represents the location of the knight after the ith move.

    Args:
        board: list of lists, initally empty

    Returns:
        board updated with a valid knight's tour, or None if no tour possible

    '''
    # Dimensions of the m x n board
    m = len(board)
    n = len(board[0])

    # Ensure board is initally empty
    for m_ in xrange(m):
        for n_ in xrange(n):
            board[m_][n_] = None

    # define moves a knight can make
    moves = [(-2, -1), (-2, 1), (-1, 2), (-1, -2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    # Unlike the n queens problem where we could place one queen per column in
    # order to reduce the size of our backtracking problem, we cannot make any
    # (simple) simplifications here. As such we simply iterate through all
    # possile valid moves and backtrack on the invalid ones

    def _find_solution(board, last_move, last_move_idx):
        '''
        Find out if there is a way for the knight to make a tour from the
        current state of the board `board` with `last_move` being the
        coordinates of the most recent placement of a knight on move number
        `last_move_idx`.

        If a solution exists, return the board with the tour. If not, return
        `None`

        '''
        if last_move_idx == m*n - 1:
            # We found a tour
            return board
        # try and make a move
        for move_m, move_n in moves:
            next_move = last_move[0] + move_m, last_move[1] + move_n
            next_move_m, next_move_n = next_move
            if ((0 <= next_move_m < m) and
               (0 <= next_move_n < n) and
               board[next_move_m][next_move_n] is None):
                # We can make a valid move
                board[next_move_m][next_move_n] = last_move_idx + 1
                solved_board = _find_solution(board,
                                              next_move,
                                              last_move_idx+1)
                if solved_board is not None:
                    return solved_board
                else:
                    # Backtrack
                    board[next_move_m][next_move_n] = None
        # If we get to this point, we cannot find a solution from the current
        # state of `board`
        return None

    # Place the knight on the upper left square
    board[0][0] = 0
    # Solve from this position
    solved_board = _find_solution(board, (0, 0), 0)
    # Return the solution (potentially None)
    return solved_board


def main():
    m, n = 6, 6
    board = [[None for _ in range(n)] for _ in range(m)]
    solved_board = knights_tour(board)
    if solved_board is not None:
        # Print the board nicely formatted
        print "\n".join(
            reduce(lambda x, y: "{}{:3}".format(x, y),
                   r[1:],
                   "{:3}".format(r[0]))
            for r in solved_board)


if __name__ == '__main__':
    main()

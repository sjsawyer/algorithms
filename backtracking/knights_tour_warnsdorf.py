'''
Q: Given a n x n chess board, generate a path for a knight to take so that it
   visits every square only once on the chess board, if possible.

A: Can use backtracking, with a common simplification to improve efficiency.
   At every next move consideration in this implementation, we move the knight
   to the next valid square which has the fewest possible onward moves.
   Comparing this problem to the more general problem of finding a Hamiltonian
   path in a graph, we move to the next adjacent vertex which has the lowest
   degree.

   For an 8x8 board, the below implementation will find the following solution:

       0 15 30 33  2 17 20 49
      29 34  1 16 31 48  3 18
      14 43 32 59 40 19 50 21
      35 28 41 44 53 58 47  4
      42 13 60 39 46 51 22 57
      27 36 45 52 61 54  5  8
      12 63 38 25 10  7 56 23
      37 26 11 62 55 24  9  6

   NOTE: The runtime is roughly linear in the total size of the chess board,
   however running on any chess board size with more than approximately
   900 in squares is likely to result in stack overflow (this algorithm
   is recursive, and python's default max recursion depth is 1000, so a
   recursive call stack greater than this length will throw a RuntimeError.

'''
import heapq


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

    # In this implementation we use an auxillary matrix the same size as the
    # chess board to keep track of the total number of moves possible from a
    # given vertex.
    vertex_degrees = [[0 for n_ in board[0]]
                      for m_ in board]
    # Use another auxillary array to keep track of the valid onward
    # moves the knight can make from each square to simplify the code
    # later on
    neighbours = [[set() for n_ in board[0]]
                  for m_ in board]
    # Initialize vertex degrees to see how many possible onward moves
    # the knight has at each square on the board, and find the valid
    # onward moves from each square
    for m_ in xrange(m):
        for n_ in xrange(n):
            for move_m, move_n in moves:
                if ((0 <= m_ + move_m < m) and
                   (0 <= n_ + move_n < n)):
                    vertex_degrees[m_][n_] += 1
                    neighbours[m_][n_].add((m_ + move_m, n_ + move_n))

    def _find_solution(board, last_move, last_move_idx, vertex_degrees):
        '''
        Find out if there is a way for the knight to make a tour from the
        current state of the board `board` with `last_move` being the
        coordinates of the most recent placement of a knight on move number
        `last_move_idx`, using `vertex_degrees` to make informed decisions
        as to which neighbours yield the greatest probability of providing
        a solution.

        If a solution exists, return the board with the tour. If not, return
        `None`

        '''
        if last_move_idx == m*n - 1:
            # We found a tour
            return board
        # find all possible valid next moves, and sort according to their
        # vertex degrees
        pq = []
        for neighbour in neighbours[last_move[0]][last_move[1]]:
            if board[neighbour[0]][neighbour[1]] is None:
                # We can make a valid move
                heapq.heappush(pq, (vertex_degrees[neighbour[0]][neighbour[1]],
                                    neighbour))
        while pq:
            # Choose the next neighbour with the lowest degree and check if
            # there exists a solution
            degree, next_move = heapq.heappop(pq)
            board[next_move[0]][next_move[1]] = last_move_idx + 1
            # reduce the degrees of the neighbours
            for neighbour in neighbours[next_move[0]][next_move[1]]:
                vertex_degrees[neighbour[0]][neighbour[1]] -= 1
            solved_board = _find_solution(
                board, next_move, last_move_idx+1, vertex_degrees)
            if solved_board is not None:
                return solved_board
            else:
                # backtrack
                for neighbour in neighbours[next_move[0]][next_move[1]]:
                    vertex_degrees[neighbour[0]][neighbour[1]] += 1

                board[next_move[0]][next_move[1]] = None
        # If we get to this point, we cannot find a solution from the current
        # state of `board`
        return None

    # Place the knight on the upper right square
    board[0][0] = 0
    # Solve from this position
    solved_board = _find_solution(board, (0, 0), 0, vertex_degrees)
    # Return the solution (potentially None)
    return solved_board


def main():
    m, n = 8, 8
    board = [[None for _ in range(n)] for _ in range(m)]
    solved_board = knights_tour(board)
    if solved_board is not None:
        # Print the board nicely formatted
        maxlen = len(str(m*n-1)) + 1
        format_str = "{:%d}" % maxlen
        print "\n".join(
            reduce(lambda x, y: "{}".format(x) + format_str.format(y),
                   r[1:],
                   format_str.format(r[0]))
            for r in solved_board)


if __name__ == '__main__':
    main()

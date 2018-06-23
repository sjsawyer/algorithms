'''
N Queens Problem

Problem: Place N queens on an N x N chess board such that no two queens are
attacking each other.

'''


class Board():
    '''
    Representation of a chess board.
    Queens are represented by 1's, blank squares by 0's

    Args:
        size: the chess board will have dimensions size x size

    '''
    def __init__(self, size):
        self.size = size
        self.board = self._initialize_empty_board()

    def _initialize_empty_board(self):
        ''' Create an empty board of size self.size x self.size '''
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def place(self, row, col):
        ''' Place a queen at position `row`,`col` '''
        self.board[row][col] = 1

    def remove(self, row, col):
        ''' Remove a queen at position `row`,`col` '''
        self.board[row][col] = 0

    def issafe(self, row, col):
        '''
        Check if placing a queen at `row`,`col` results in a configuration
        where no queens are attacking each other.

        Note we do not actually need to check if the column is safe because of
        how our recursive solution is set up.
        in.

        '''
        for r in range(self.size):
            for c in range(self.size):
                # check if this row is safe
                if r == row and self.board[r][c]:
                    return False
                # check if the diagonals are safe
                if abs(r - row) == abs(c - col) and self.board[r][c]:
                    return False
        return True

    def _solve_from_col(self, col):
        '''
        Find a valid configuration from self.board[:][col:], assuming that
        self.board[:][:col] is already valid.

        '''
        if col == self.size:
            # The board is solved
            return True
        # try each position in the current column
        for row in range(self.size):
            if self.issafe(row, col):
                # Place a queen in this row
                self.place(row, col)
                # Try to find a solution from this point
                if self._solve_from_col(col+1):
                    return True
                # We didn't find a solution so backtrack
                self.remove(row, col)
        # if we get to this point, we did not find a solution
        return False

    def solve(self):
        '''
        Find a board configuration in which `size` queens are placed and
        no two are attacking each other.

        '''
        # We start by placing a queen in the first column and solving
        # recursively
        is_solution = self._solve_from_col(0)
        print self if is_solution else "No solution"

    def __str__(self):
        ''' String representation of the current state of the board '''
        board_str = "\n".join(
                        map(" ".join,
                            (map(str, row) for row in self.board)))
        # Print as 'Q's and '-'s
        board_str = board_str.replace('1', 'Q').replace('0', '-')
        return board_str


def main():
    n = 16
    board = Board(n)
    board.solve()


if __name__ == '__main__':
    main()

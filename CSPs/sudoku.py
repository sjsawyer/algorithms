import math


def order_domain_values(square):
    '''
    Use the Least Constraining Values heuristic to order the values of `square`
    '''
    pass


def select_free_square(board, domains):
    '''
    Select the next variable to assign to, using the Most Constrained Variable
    and Most Constraining Variable heuristics
    '''
    # Upper bound on domain size
    min_domain_size = 10
    # The most constained square (possibly multiple)
    mcvs = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # This square is unassigned
                if len(domains[i][j]) < min_domain_size:
                    # This square is more constrained
                    min_domain_size = len(domains[i][j])
                    mcvs = [(i, j)]
                elif len(domains[i][j]) == min_domain_size:
                    mcvs.append((i, j))
    # Return the most constraining square amongst the most contained
    return most_constraining_variable(mcvs)


def most_constraining_variable(squares):
    '''
    Return the most constraining square amongst squares, where the domain sizes
    of the squares in `squares` are all equal and minimum amongst all squares
    in `board`. To do this, we return the square which is involved in the most
    constraints.
    '''
    pass


def AC3(board):
    '''
    Update `board` to be arc consistent, and return anything that was pruned so
    that it can be added back in if we need to backtrack from this
    configuration.
    '''
    pass


def assign_value(board, square, value):
    '''
    Assign the `square` in `board` to have the value `value`
    '''
    pass


def add_back_pruned(board, pruned):
    '''
    Add back the values we pruned from the domains of squares as a result of
    applying AC3 and needing to backtrack.
    '''
    pass


def recursively_backtrack(board, domains, moves_remaining):
    '''
    Try to find a solution from the current state of the `board` and values
    remaining in the `domains` of each square of the board.
    If a solution is possible, return the board. If not, return `None`

    '''
    if moves_remaining == 0:
        return board
    # Select a "good" square to assign to next
    square = select_free_square(board, domains)
    # Select the next "best" value for this square
    for value in order_domain_values(square):
        assign_value(board, square, value)
        # Reduce the domain of other squares if possible
        pruned = AC3(board)
        result = recursively_backtrack(board, domains, moves_remaining-1)
        if result is not None:
            return result
        # We have failed
        add_back_pruned(board, pruned)
    # Cannot assign any value to `square`, so there is no solution from this
    # state
    return None


def solve_sudoku(board):
    '''
    Given an n x n grid representing a sudoku board, return a solved instance
    of the board.
    '''
    # Board and subgrid sizes
    n = len(board)
    subgrid_length = math.sqrt(n)
    # Domain for each square initially contains everything
    domains = [[set(range(1, 10)) for _ in range(n)]
               for _ in range(n)]
    # Solve the board
    return recursively_backtrack(board, domains, n**2)


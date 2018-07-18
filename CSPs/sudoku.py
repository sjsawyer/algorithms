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


def add_back_pruned(pruned):
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
        add_back_pruned(pruned)
    # No solution from this state of the board
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


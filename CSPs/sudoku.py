import math


def constrained(square1, square2, board):
    '''
    Determine if two squares are part of a binary constraint
    E.g., in the same row, column or subgrid of the sudoku board
    '''
    if square1 == square2:
        return False
    if not constrained.hasattr("subgridsize"):
        constrained.subgridsize = math.sqrt(len(board))
    if ((square1[0] == square2[0])    # same row
      or (square1[1] == square2[1])   # same column
      or ((square1[0]/constrained.subgridsize ==
           square2[0]/constrained.subgridsize) and
          (square1[1]/constrained.subgridsize ==
           square2[1]/constrained.subgridsize))):  # same subgrid
        return True
    # Not constrained
    return False


def order_domain_values(board, domains, square):
    '''
    Use the Least Constraining Values heuristic to order the values of `square`
    given the current state of `board` and `domains`
    '''
    n_constraints = {value: 0 for value in domains[square[0]][square[1]]}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not assigned((i, j), board) and\
               constrained(square, (i, j)):
                for value in n_constraints:
                    if value in domains[i][j]:
                        n_constraints[value] += 1
    value_orders = sorted(n_constraints.keys(),
                          key=lambda v: n_constraints[v])
    return value_orders


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
    # Return the most constraining square amongst the most constrained
    return most_constraining_variable(board, mcvs)


def assigned(square, board):
    ''' Check if `square` is currently assigned a value in `board` '''
    return board[square[0]][square[1]] == 0


def most_constraining_variable(board, squares):
    '''
    Return the most constraining square amongst `squares`, where the domain
    sizes of the squares in `squares` are all equal and minimum amongst all
    squares in `board`. To do this, we return the square which is involved in
    the most constraints.
    '''
    max_num_constraints = -1
    mcv = None
    # Quick check in case we don't need to do any computation
    if len(squares) == 1:
        return squares[0]
    for square in squares:
        # Find how many constraints this square is currently involved in
        n_constraints = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 0) and constrained(square, (i, j)):
                    n_constraints += 1
        if n_constraints > max_num_constraints:
            max_num_constraints = n_constraints
            mcv = square
    return mcv


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
    board[square[0]][square[1]] = value


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
    for value in order_domain_values(board, domains, square):
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


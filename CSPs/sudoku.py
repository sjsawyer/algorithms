import math
from collections import deque


def constrained(square1, square2, board):
    '''
    Determine if two squares are part of a binary constraint
    E.g., in the same row, column or subgrid of the sudoku board
    '''
    if square1 == square2:
        return False
    if not hasattr(constrained, "subgridsize"):
        constrained.subgridsize = int(math.sqrt(len(board)))
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
               constrained(square, (i, j), board):
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
    # The most constrained square (possibly multiple)
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
    return board[square[0]][square[1]] != 0


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
                if (board[i][j] == 0) and constrained(square, (i, j), board):
                    n_constraints += 1
        if n_constraints > max_num_constraints:
            max_num_constraints = n_constraints
            mcv = square
    return mcv


def _AC3_remove_inconsistent_values(arc, board, domains):
    '''
    Make this arc consistent by removing any values in the domain of the
    tail of the arc that conflict with those in the head of the arc
    '''
    removed = set()
    tail, head = arc
    tail_domain = domains[tail[0]][tail[1]]
    head_domain = domains[head[0]][head[1]]
    for tail_value in tail_domain:
        consistent = False
        for head_value in head_domain:
            if head_value != tail_value:
                consistent = True
                break
        if not consistent:
            # This value is to be removed from tail's domain
            # Cannot do it yet or else we will get the error
            # RuntimeError: Set changed size during iteration
            removed.add(tail_value)
    # Remove the inconsistent values from tail's domain
    for tail_value in removed:
        tail_domain.remove(tail_value)
    # Return the values we removed
    return removed


def AC3(board, domains):
    '''
    Update `board` to be arc consistent, and return anything that was pruned so
    that it can be added back in if we need to backtrack from this
    configuration.
    '''
    arcs = deque()
    # Generate all constraint arcs for current state
    for i1 in range(len(board)):
        for j1 in range(len(board[0])):
            for i2 in range(len(board)):
                for j2 in range(len(board)):
                    if not (assigned((i1, j1), board) or
                            assigned((i2, j2), board)):
                        # Note constrained returns False if arc points
                        # to itself
                        if constrained((i1, j1), (i2, j2), board):
                            # Append arc for both directions
                            arcs.append(((i1, j1), (i2, j2)))
                            arcs.append(((i2, j2), (i1, j1)))
    # Keep track of removed domain values so we can add them back in
    # if backtracking is needed
    pruned = {}
    while arcs:
        arc = arcs.popleft()
        removed = _AC3_remove_inconsistent_values(arc, board, domains)
        if removed:
            # Update pruned
            pruned[arc[0]] = pruned.get(arc[0], set()).union(removed)
            # Add arcs back on that could now be inconsistent
            # E.g. those pointing to the tail of the current arc
            tail = arc[0]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if not assigned((i, j), board) and \
                       constrained((i, j), tail, board):
                        arcs.append(((i, j), tail))
    return pruned


def assign_value(board, square, value):
    '''
    Assign the `square` in `board` to have the value `value`
    '''
    board[square[0]][square[1]] = value


def add_back_pruned(domains, pruned):
    '''
    Add back the values we pruned from the domains of squares as a result of
    applying AC3 and needing to backtrack.
    '''
    for square, removed in pruned.iteritems():
        domains[square[0]][square[1]].update(removed)


def consistent(value, square, domains, board):
    '''
    Check if assigning `value` to `square` does not break any constraints
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if assigned((i, j), board) \
               and constrained((i, j), square, board) \
               and board[i][j] == value:
                return False
    return True


def update_domains(board, square, value, domains):
    '''
    Update the domains of all constrained squares of `square` after assigning
    `value` to `square`, and return what was removed.
    '''
    removed = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not assigned((i, j), board) \
               and constrained((i, j), square, board) \
               and value in domains[i][j]:
                domains[i][j].remove(value)
                if (i, j) in removed:
                    removed[(i, j)].add(value)
                else:
                    removed[(i, j)] = set([value])
    return removed

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
        if consistent(value, square, domains, board):
            assign_value(board, square, value)
            removed = update_domains(board, square, value, domains)
            # Reduce the domain of other squares if possible
            pruned = AC3(board, domains)
            result = recursively_backtrack(board, domains, moves_remaining-1)
            if result is not None:
                return result
            # We have failed
            assign_value(board, square, 0)
            add_back_pruned(domains, removed)
            add_back_pruned(domains, pruned)
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
    # Domain for each square initially contains everything
    domains = [[set(range(1, n+1)) for _ in range(n)]
               for _ in range(n)]
    # Initial pruning of domains
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                _ = update_domains(board, (i, j), board[i][j], domains)
    # How many moves left to make
    moves_remaining = sum(sum(map(lambda s: s == 0, row))
                          for row in board)
    # Solve the board
    return recursively_backtrack(board, domains, moves_remaining)


def print_board(board):
    print "\n".join(" ".join(map(str, row)) for row in board)


def main():
   board4 = [[0, 0, 0, 4],
             [4, 3, 0, 1],
             [0, 1, 4, 2],
             [2, 4, 1, 0]]

   board9 = [[0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 6, 0, 7, 0, 0, 3, 0],
             [0, 0, 0, 8, 3, 5, 0, 0, 0],
             [0, 0, 3, 6, 0, 0, 0, 7, 0],
             [0, 0, 0, 0, 1, 3, 0, 0, 0],
             [5, 0, 0, 0, 4, 0, 8, 0, 0],
             [1, 0, 5, 3, 0, 7, 0, 2, 6],
             [0, 2, 0, 0, 0, 1, 7, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 8]]


   board92 = [[0, 6, 0, 8, 0, 0, 0, 1, 0],
              [2, 0, 0, 0, 1, 0, 0, 0, 4],
              [0, 0, 0, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 5, 0, 6, 0, 8],
              [0, 1, 0, 0, 0, 0, 0, 2, 0],
              [9, 0, 5, 0, 4, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [5, 0, 0, 0, 3, 0, 0, 0, 2],
              [0, 8, 0, 0, 0, 6, 0, 7, 0]]


   solved_board = solve_sudoku(board92)
   if solved_board:
       print_board(solved_board)

if __name__ == '__main__':
    main()

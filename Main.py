"""
Module containing the main algorithms for solving the N-Queens puzzle.

Usage
_____
One solution: solving for any solution to the N-Queens problem, call
find_solution. This method uses backtracking to solve the N-Queens problem.
The method takes in an int to determine board size and will print the first
solution found to the console or will print no solution found.

Ex. find_solution(4) will write the first solution found to the console.

All solutions: solving for all solutions to the N-Queens problem, call
all_solutions. This method also uses backtracking to solve the N-Queens
problem. The method takes in an int to determine board size and will print all
the solutions found to the console or will print no solution found.

Ex. all_solutions(4) will print every valid solution to the console.

Methods
_______
:method all_solutions(size: int): solves for every solution of the N-Queens
    puzzle of the input size and prints them all (or none found) to console.
:method find_solution(size: int): solves for a single solution of the N-Queens
    puzzle of the input size and prints the solution (or none found) to the
    console.
:method solve_all: actual algorithm for finding all the solutions (everything
    from all_solutions but the console printing). Takes a board, the current
    col and a list of completed boards as input and recursively backtracks to
    find the solutions. Returns list of completed solutions.

"""

from copy import deepcopy
from board import Board

def all_solutions(size: int) -> None:
    """
    Main function for finding every solution given a board size of size.
    Will print all completed board states to console if solution is found.
    Will print "not found" if there is no solution for a board of size size.
    :param size: int representing size of board to find a solution for
    """
    print(f"Results for board of size {size}:")
    board = Board(size)
    results = solve_all(col=0, board=board, results=[])
    if results == []:
        print(f"No valid arrangement for board of size {size}\n")
    for result in results:
        for row in result:
            print(row)
        print()

def solve_all(board: Board, col: int, results: list) -> list:
    """
    Recursive function that searches board using BFS to arrange board into
    all completed states. Will return list of all valid solutions.
    :param board: Board object to search
    :param col: int representing current column to try
    """
    #Completed board found
    if col >= board.size:
        results.append(deepcopy(board.board))
        return results
    for row in range(board.size):
        #check if position is valid
        if check_constraints(board=board, row=row, col=col):
            #update board and continue BFS
            board.mark_tile(row=row, col=col)
            results = solve_all(col=col+1, board=board, results=results)
            board.unmark_tile(row=row, col=col)
    #no valid solutions for current board position
    return results

def find_solution(size: int) -> None:
    """
    Main function for finding a single solution given a board size of size.
    Will print completed board state to console if solution is found.
    Will print "not found" if there is no solution for a board of size size.
    :param size: int representing size of board to find a solution for
    """
    board = Board(size)
    if not solve_one(col=0, board=board):
        print(f"No valid arrangement for board of size {size}")
        return
    board.print_state()

def solve_one(board: Board, col: int) -> bool:
    """
    Recursive function that searches board using BFS to arrange board into
    completed state. Will return True if board state is valid, False otherwise.
    :param board: Board object to search
    :param col: int representing current column to try
    """
    #Completed board found
    if col >= board.size:
        return True
    for row in range(board.size):
        #check if position is valid
        if check_constraints(board=board, row=row, col=col):
            #update board and continue BFS
            board.mark_tile(row=row, col=col)
            if solve_one(col=col+1, board=board):
                return True
            board.unmark_tile(row=row, col=col)
    #no valid solutions for current board position
    return False

def check_constraints(board: Board, row: int, col: int) -> bool:
    """
    Check constraints to see if a queen can be placed on tile.
    :param board: Board object to search
    :param row: int representing row to search
    :param col: int representing current column reached
    """
    if not row_constraint(board=board, row=row, col=col):
        return False
    if not upper_diagonal_constraint(board=board, row=row, col=col):
        return False
    if not lower_diagonal_constraint(board, row, col):
        return False
    return True

def row_constraint(board: Board, row: int, col: int) -> bool:
    """
    Function checking to make sure no queens placed on the same row of the board.
    :param board: Board object to search
    :param row: int representing row to search
    :param col: int representing current column reached
    """
    for i in range(col):
        if board.is_queen(row=row, col=i):
            return False
    return True

def upper_diagonal_constraint(board: Board, row: int, col: int) -> bool:
    """
    Function checking to make sure no queens placed on the diagonal to the
    upper left of the current position.
    :param board: Board object to search
    :param row: int representing row to search
    :param col: int representing current column reached
    """
    #move to first tile in diagonal
    row -= 1
    col -= 1
    #while still in board, test and move to next position return false if fails
    while row >= 0 and col >= 0:
        if board.is_queen(row=row, col=col):
            return False
        row -= 1
        col -= 1
    return True

def lower_diagonal_constraint(board: Board, row: int, col: int) -> bool:
    """
    Function checking to make sure no queens placed on the diagonal to the
    lower left of the current position.
    :param board: Board object to search
    :param row: int representing row to search
    :param col: int representing current column reached
    """
    #move to first tile in diagonal
    row += 1
    col -= 1
    #while still in board, test and move to next position return false if fails
    while row < board.size and col >= 0:
        if board.is_queen(row=row, col=col):
            return False
        row += 1
        col -= 1
    return True

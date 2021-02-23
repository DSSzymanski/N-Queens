"""
This module contains the class Board, which is used to represent a chess board
using a 2d list.

Class Board:
    Attributes
    __________
    :attribute size: int size of board
    :attribute board: 2d list of size (size x size) representing the board.

    Methods
    _______
    :method mark_tile: marks a coordinate of board to represent a queen.
    :method unmark_tile: unmarks a coordinate of board to represent a blank
        tile.
    :method is_queen: returns bool for if a queen is there or not
    :method print_state: prints current board to console.

"""
class Board:
    """
    Class used to represent a chess board.

    Attributes
    __________
    :attribute size: int representing the NxN dimensions of the board.
    :attribute board: 2d list of ints generated with the NxN size attribute
        that stores the data of the board. A 0 represents a blank square, a 1
        represents a square that has a queen on it.

    Methods
    _______
    :method mark_tile(row: int, col:int): A method that marks the location of
        2 ints, (row, col) on the board attribute to contain a 1 (Queen)
        instead of a 0.
    :method unmark_tile(row: int, col:int): A method that unmarks the location
        of 2 ints, (row, col) on the board attribute to return to a 0 (no
        Queen) instead of a 1.
    :method is_queen(row: int, col: int): A method that returns a boolean value
        determining whether the (row, col) coordinate of the board attribute
        contains a 1 (a Queen).
    :method print_state: Prints the current state of the board to console.
    """

    def __init__(self, size: int):
        """
        Initialize Board object.
        :attribute size: int representing size of board.
        :attribute board: 2d list representing a board. Will initialize to size
            of size given and initially contain all 0s to represent an empty
            board.

        :param size: int used to set up the int attribute size and initialize
            the board attribute.
        """
        self.size = size
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]

    def mark_tile(self, row: int, col: int) -> None:
        """
        Set tile on board to 1 to represent queen here.
        :param row: row on grid to place queen
        :param col: column on grid to place queen
        """
        self.board[row][col] = 1

    def unmark_tile(self, row: int, col: int) -> None:
        """
        Unset tile on board to 0 to represent no queen here.
        :param row: row on grid to unplace queen
        :param col: column on grid to unplace queen
        """
        self.board[row][col] = 0

    def is_queen(self, row: int, col: int) -> bool:
        """
        Returns int representing queen or no queen placement of tile
        :param row: row on grid to read
        :param col: column on grid to read
        """
        #print(row, col)
        if self.board[row][col] == 1:
            return True
        return False

    def print_state(self) -> None:
        """
        Prints current state of board to console
        """
        for i in range(self.size):
            print(self.board[i])

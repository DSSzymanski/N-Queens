"""

"""
class Board:

    def __init__(self, size: int):
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

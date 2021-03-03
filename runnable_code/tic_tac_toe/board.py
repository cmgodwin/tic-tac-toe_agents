import numpy as np

from tic_tac_toe.player import Player, PLAYER_NAMES


class CellState:
    EMPTY = -1
    X = Player.X
    O = Player.O

    ALL_STATES = Player.ALL_PLAYERS + [EMPTY]


class Board(object):
    def __init__(self, size=3, k=0):
        self._size = size
        self._board = CellState.EMPTY * np.ones(shape=(size, size),
                                                dtype=np.int8)
        self._k = k

    def row(self, row_num):
        if row_num < 0 or row_num >= self._size:
            raise ValueError("row_num must be between 0 and {}.".format(
                self._size))

        return self._board[row_num, :]

    def col(self, col_num):
        if col_num < 0 or col_num >= self._size:
            raise ValueError("col_num must be between 0 and {}.".format(
                self._size))

        return self._board[:, col_num]

    def cell(self, row_num, col_num):
        if row_num < 0 or row_num >= self._size:
            raise ValueError("row_num must be between 0 and {}.".format(
                self._size))

        if col_num < 0 or col_num >= self._size:
            raise ValueError("col_num must be between 0 and {}.".format(
                self._size))

        return self._board[row_num, col_num]

    def set_cell(self, state, row_num, col_num):
        if state not in CellState.ALL_STATES:
            raise ValueError("Cell state cannot be {}.".format(state))

        if row_num < 0 or row_num >= self._size:
            raise ValueError("row_num must be between 0 and {}.".format(
                self._size))

        if col_num < 0 or col_num >= self._size:
            raise ValueError("col_num must be between 0 and {}.".format(
                self._size))

        self._board[row_num, col_num] = state

    def get_appended_board(self, state, row_num, col_num):
        if state not in CellState.ALL_STATES:
            raise ValueError("Cell state cannot be {}.".format(state))

        if row_num < 0 or row_num >= self._size:
            raise ValueError("row_num must be between 0 and {}.".format(
                self._size))

        if col_num < 0 or col_num >= self._size:
            raise ValueError("col_num must be between 0 and {}.".format(
                self._size))

        self._board[row_num, col_num] = state
        return self

    def get_appended_board_state(self, state, row_num, col_num):
        if state not in CellState.ALL_STATES:
            raise ValueError("Cell state cannot be {}.".format(state))

        if row_num < 0 or row_num >= self._size:
            raise ValueError("row_num must be between 0 and {}.".format(
                self._size))

        if col_num < 0 or col_num >= self._size:
            raise ValueError("col_num must be between 0 and {}.".format(
                self._size))

        self._board[row_num, col_num] = state
        return self._board
        
    @property
    def size(self):
        return self._size

    @property
    def main_diagonal(self):
        return np.diagonal(self._board)

    @property
    def secondary_diagonal(self):
        return np.diagonal(np.fliplr(self._board))

    @property
    def diagonals(self):
        return [self.main_diagonal, self.secondary_diagonal]

    @property
    def rows(self):
        return [self.row(i) for i in range(self._size)]

    @property
    def cols(self):
        return [self.col(i) for i in range(self._size)]

    @property
    def all_lines(self):
        return self.diagonals + self.rows + self.cols

    @property
    def winner(self):
        def _common_element(l):
            index = 0
            consecutive_elements = 1
            for e in l:
                if e == l[index + 1]:
                    consecutive_elements += 1
                    if consecutive_elements == self._k:
                        return e
                else:
                    consecutive_elements = 1
                index += 1
                if index == self.size - 1:
                    return None

        for line in self.all_lines:
            p = _common_element(line)
            if p in Player.ALL_PLAYERS:
                return p

    def print_board(self):
        cell_char = {
            CellState.EMPTY: " ",
            CellState.X: PLAYER_NAMES[CellState.X],
            CellState.O: PLAYER_NAMES[CellState.O],
        }

        def _row_to_str(enumerated_row):
            i, row = enumerated_row
            return "{: >2}   ".format(i) \
                   + " │ ".join(map(lambda c: cell_char[c], row)) + " "

        row_separator = "\n    " + "┼".join(["───"] * self._size) + "\n"
        all_rows = row_separator.join(map(_row_to_str, enumerate(self.rows)))
        header = "    " + " ".join(map(lambda i: " {: <2}".format(i),
                                      range(self._size)))

        print(header + "\n\n" + all_rows)

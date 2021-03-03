from abc import ABC, abstractmethod
from collections import namedtuple

from tic_tac_toe.board import CellState
from tic_tac_toe.player import PLAYER_NAMES


class Move(namedtuple("Move", ["player", "row", "col"])):
    def __repr__(self):
        return "Move(player={},row={},col={})".format(
            PLAYER_NAMES[self.player], self.row, self.col)


class Agent(ABC):
    def __init__(self, player):
        self._player = player

    @abstractmethod
    def next_move(self, board):
        pass

    def _valid_moves(self, board):
        valid_moves = []
        for i in range(board.size):
            for j in range(board.size):
                if board.cell(i, j) == CellState.EMPTY:
                    valid_moves.append(Move(self._player, i, j))

        return valid_moves

import numpy as np

from copy import deepcopy
from tic_tac_toe.player import Player
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.agents.base_agent import Agent, Move


#the suboptimal agent is an implementation of the bruteforce agent in which the board is not restored once it is worked on;
#as a result it only observes the first path it sees to generating a winning sequence and does not respond to the threats of its opponent, 
#however it makes its decisions very quickly
class SuboptimalAgent(Agent):
    board = Board()

    def get_appended_board_state(self, board_state, cell_value, i, j):
        board_state[i][j] = cell_value
        return board_state

    def minimax(self, board_state, maximizer, depth):
        self.board._board = board_state
        # self.board.print_board()
        current_utility = None
        chosen_utility = None
        if self._player == Player.X:
            if self.board.winner == Player.X:
                return 1 / depth
            if self.board.winner == Player.O:
                return -1 / depth
        else:
            if self.board.winner == Player.O:
                return 1 / depth
            if self.board.winner == Player.X:
                return -1 / depth
        if depth == self.board.size ** 2:
            return 0

        # self.board.print_board()
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.cell(i, j) == CellState.EMPTY:
                    if self._player == Player.X:
                        if maximizer and chosen_utility != 1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1)
                            #here the state would be restored, but instead the board simply fills up
                            self.board._board = board_state
                        if not maximizer and chosen_utility != -1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1)
                            self.board._board = board_state
                    else:
                        if maximizer and chosen_utility != 1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1)
                            self.board._board = board_state
                        if not maximizer and chosen_utility != -1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1)
                            self.board._board = board_state

                    if current_utility is not None:
                        if maximizer:
                            if chosen_utility is None or current_utility > chosen_utility:
                                chosen_utility = current_utility
                        else:
                            if chosen_utility is None or current_utility < chosen_utility:
                                chosen_utility = current_utility
        return chosen_utility
        
       
        

    def next_move(self, given_board):
        self.board._size = given_board._size
        self.board._k = given_board._k

        best_move_i = -1
        best_move_j = -1
        maximum = -100
        depth = given_board.size ** 2

        maximizer = True

        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    depth -= 1

        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    if self._player == Player.X:
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 0, i, j), not maximizer, depth+1)
                    else:
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 1, i, j), not maximizer, depth+1)
                    if current is not None:
                        if current > maximum:
                            maximum = current
                            best_move_i = i
                            best_move_j = j
        return Move(self._player, best_move_i, best_move_j)
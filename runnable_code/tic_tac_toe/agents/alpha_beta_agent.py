import numpy as np

from copy import deepcopy
from tic_tac_toe.player import Player
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.agents.base_agent import Agent, Move


#much of the code here is the same as in the bruteforce agent, so for the sake of clarity the elements discussed here will 
#be only those unique to this agent; for descriptions of any undescribed portions, refer to the bruteforce agent

class AlphaBetaAgent(Agent):
    board = Board()
    state_space = 0

    def get_appended_board_state(self, board_state, cell_value, i, j):
        board_state[i][j] = cell_value
        return board_state
    
    #minimax algorithm for pruning, taking the same parameters as the brute force algorithm but this time with alpha and beta
    def minimax(self, board_state, maximizer, depth, alpha, beta):
        self.state_space += 1
        self.board._board = board_state

        current_utility = None
        chosen_utility = None

        #static evaluations
        winner = None
        if depth > self.board._k - 1:
            winner = self.board.winner
        if self._player == Player.X:
            if winner == Player.X:
                return 1 / depth
            if winner == Player.O:
                return -1 / depth
        else:
            if winner == Player.O:
                return 1 / depth
            if winner == Player.X:
                return -1 / depth
        if depth == self.board.size ** 2:
            return 0

        #main recursion block
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.cell(i, j) == CellState.EMPTY:
                    if self._player == Player.X:
                        #in any case where alpha < beta, the recursion will not be entered; this is because if the current greatest choice for the maximizer is
                        #less than the current least choice for the minimizer, there is no other step that can be taken by either player to prevent the outcome 
                        #of the current branch, so the rest of the branch can be pruned
                        if maximizer and chosen_utility != 1 and alpha < beta:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1, alpha, beta)
                            board_state[i][j] = -1
                            self.board._board = board_state
                            #in the case of the maximizer, alpha is stored as the current greatest choice
                            if current_utility > alpha:
                                alpha = current_utility
                        if not maximizer and chosen_utility != -1 and alpha < beta:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1, alpha, beta)
                            board_state[i][j] = -1
                            self.board._board = board_state
                            #in the case of the minimizer, beta is stored as the current least choice
                            if current_utility < beta:
                                beta = current_utility
                    else:
                        if maximizer and chosen_utility != 1 and alpha < beta:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1, alpha, beta)
                            board_state[i][j] = -1
                            self.board._board = board_state
                            if current_utility > alpha:
                                alpha = current_utility
                        if not maximizer and chosen_utility != -1 and alpha < beta:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1, alpha, beta)
                            board_state[i][j] = -1
                            self.board._board = board_state
                            if current_utility < beta:
                                beta = current_utility

                    if current_utility is not None:
                        if maximizer:
                            if chosen_utility is None or current_utility > chosen_utility:
                                chosen_utility = current_utility
                        else:
                            if chosen_utility is None or current_utility < chosen_utility:
                                chosen_utility = current_utility
        return chosen_utility
        
       
        

    def next_move(self, given_board):
        self.state_space = 0
        self.board._k = given_board._k
        self.board._size = given_board._size

        best_move_i = -1
        best_move_j = -1
        maximum = -100
        depth = given_board.size ** 2

        #alpha and beta are initialized to negative and positive infinity
        alpha = float("-inf")
        beta = float("inf")

        maximizer = True

        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    depth -= 1

        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    if self._player == Player.X:
                        #alpha and beta are passed into minimax
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 0, i, j), not maximizer, depth+1, alpha, beta)
                    else:
                        #alpha and beta are passed into minimax
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 1, i, j), not maximizer, depth+1, alpha, beta)
                    if current is not None:
                        if current > maximum:
                            maximum = current
                            best_move_i = i
                            best_move_j = j
        print("State space traversed contained " + str(self.state_space) + " states")
        #the best move is returned
        return Move(self._player, best_move_i, best_move_j)
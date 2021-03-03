import numpy as np

from copy import deepcopy
from tic_tac_toe.player import Player
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.agents.base_agent import Agent, Move



class BruteForceAgent(Agent):
    #initializes the board object and the state space
    board = Board()
    state_space = 0

    #returns a board state with a changed cell value at the given coordinates
    def get_appended_board_state(self, board_state, cell_value, i, j):
        board_state[i][j] = cell_value
        return board_state

    #minimax algorithm for brute force, taking a board configuration integer array, a maximizer boolean, and a depth integer as parameters
    def minimax(self, board_state, maximizer, depth):
        #increments state space and fixes the new board state to the board object at each recursive call
        self.state_space += 1
        self.board._board = board_state

        #initialize current and chosen utility
        current_utility = None
        chosen_utility = None

        #this code block catches any winning boards and returns their evaluations; it minimizes calculation by only calculating board.winner once and setting it
        #to a variable; calculation is reduced further by only calculating board.winner in cases where the depth is deep enough for a winner to be possible,
        #i.e. the depth is greater than or equal to the depth of the winning sequence
        winner = None
        if depth > self.board._k - 1:
            winner = self.board.winner
        if self._player == Player.X:
            if winner == Player.X:
                #depth is accounted for in evaluating the winning board states; this allows the agent to find the quickest path to victory within the game,
                #but it does not change the winrate of the agent (since it will only cause the agent to win in less moves, not more frequently), and it
                #increases calculation time fairly significantly
                return 1 / depth
            if winner == Player.O:
                return -1 / depth
        else:
            if winner == Player.O:
                return 1 / depth
            if winner == Player.X:
                return -1 / depth

        #accounts for the case of a drawn board, returning an evaluation of 0
        if depth == self.board.size ** 2:
            return 0

        #this code block is the main body of the algorithm; it loops through the given board and calculates minimax on every empty square
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.cell(i, j) == CellState.EMPTY:
                    #this if duplicates the functionality of the loop for players X and O
                    if self._player == Player.X:
                        #this if duplicates the functionality of the loop for the maximizer and the minimizer
                        if maximizer and chosen_utility != 1:
                            #sets the currently examined utility equal to the minimax evaluation of the current blank square; the current player's
                            #symbol (X or O) is placed in the coordinates of the blank, and the resulting board is passed as a new board state;
                            #the maximizer/minimizer is swapped and passed; the new depth is passed
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1)
                            #once the recursion is exited, the value that was changed and tested is returned to a blank
                            board_state[i][j] = -1
                            #the board's integer array is reinitialized to the restored board state
                            self.board._board = board_state
                        if not maximizer and chosen_utility != -1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1)
                            board_state[i][j] = -1
                            self.board._board = board_state
                    else:
                        #again, duplicates the functionality of the loop for the maximizer and minimizer
                        if maximizer and chosen_utility != 1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 1, i, j), not maximizer, depth+1)
                            board_state[i][j] = -1
                            self.board._board = board_state
                        if not maximizer and chosen_utility != -1:
                            current_utility = self.minimax(self.get_appended_board_state(board_state, 0, i, j), not maximizer, depth+1)
                            board_state[i][j] = -1
                            self.board._board = board_state

                    #this code block controls the algorithm's decisionmaking; in the case of the maximizer, each utility is compared to the current best and the
                    #greater of the two is stored; the minimizer does the opposite, storing the lowest utility
                    if current_utility is not None:
                        if maximizer:
                            if chosen_utility is None or current_utility > chosen_utility:
                                chosen_utility = current_utility
                        else:
                            if chosen_utility is None or current_utility < chosen_utility:
                                chosen_utility = current_utility

        #when each non-leaf recursive call is complete, the chosen utility is returned instead of a raw value
        return chosen_utility


    def next_move(self, given_board):
        #initializes the state space, the board size, and the k-value
        self.state_space = 0
        self.board._k = given_board._k
        self.board._size = given_board._size

        #initializes the local variables for the best i and j, the chosen utility, and the depth
        best_move_i = -1
        best_move_j = -1
        chosen = -100

        #the player making a move should maximize utility, so they begin as the maximizer
        maximizer = True

        #sets the depth equal to the number of occupied squares by decrementing from a full board of size^2 based on how
        #many empty squares there are
        depth = given_board.size ** 2
        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    depth -= 1

        #this code block duplicates the function of the main loop in the recursion (but with only the maximizer accounted for)
        #this serves as the preliminary step to start off the recursion
        for i in range(given_board.size):
            for j in range(given_board.size):
                if given_board.cell(i, j) == CellState.EMPTY:
                    if self._player == Player.X:
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 0, i, j), not maximizer, depth+1)
                    else:
                        current = self.minimax(self.get_appended_board_state(deepcopy(given_board._board), 1, i, j), not maximizer, depth+1)
                    if current is not None:
                        #keeps track not only of the best utility, but of the coordinates where it was found
                        if current > chosen:
                            chosen = current
                            best_move_i = i
                            best_move_j = j
        #prints the state space after each move
        print("State space traversed contained " + str(self.state_space) + " states")
        #returns the best move
        return Move(self._player, best_move_i, best_move_j)

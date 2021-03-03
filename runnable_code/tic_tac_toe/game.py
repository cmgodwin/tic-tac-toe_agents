import time
import random
import numpy as np

from copy import deepcopy

from .board import Board, CellState
from .player import Player, PLAYER_NAMES

class Performance():
    num_x_wins = 0
    num_o_wins = 0
    num_draws = 0
    player_x_total_time = 0
    player_o_total_time = 0


class Game(object):
    def __init__(self, player_x, player_o, size=3, starting_board=None):
        self._player_x = player_x
        self._player_o = player_o

        self._current_player = (Player.X, self._player_x)
        self._next_player = (Player.O, self._player_o)

        if starting_board is None:
            self._board = Board(size=size)

        self._num_rounds = 0

    def initiate_random_state(self):
        while True:
            self._board._board = np.ones(shape=(self._board.size, self._board.size), dtype=np.int8)
            self._board._board *= -1
            num_empty = 0
            counter = 0
            #board_size - 2 ensures the number of moves will not equal the board size or the board size - 1, both of which would cause a pre-decided result
            num_moves = random.randint(0, self._board.size ** 2 - 2)
            #loop guarantees that num_moves will be an even number, so that X remains as the first player
            while num_moves % 2 == 1:
                num_moves = random.randint(0, self._board.size ** 2 - 2)

            for k in range(num_moves):
                for i in range(self._board.size):
                    for j in range(self._board.size):
                        if self._board.cell(i, j) == CellState.EMPTY:
                            num_empty += 1

                rand_guy = random.randint(1, num_empty)
                num_empty = 0
                counter = 0
                for i in range(self._board.size):
                    for j in range(self._board.size):
                        if self._board.cell(i, j) == CellState.EMPTY:
                            counter += 1
                            if rand_guy == counter:
                                #this if gives the condition for X and O; if the number being looped through is even, X is played, and if it is odd, O is played
                                if k % 2 == 0:
                                    self._board._board[i][j] = 0
                                    self._num_rounds += 1
                                else:
                                    self._board._board[i][j] = 1
                                    self._num_rounds += 1
            if self._board.winner not in Player.ALL_PLAYERS:
                break

    def play(self, board_size, k, random_state):
        self._board = Board(size=board_size, k=k)

        if random_state == "y":
            self.initiate_random_state()
        agent_performance = Performance()
        initial_player = self._current_player[1]
        first_player = True
        first_player_total_time = 0
        second_player_total_time = 0
        while (self._board.winner is None
               and self._num_rounds < self._board.size ** 2):
            self._show_board()
            initial_move_moment = time.time()
            self._make_next_move()
            self._current_player, self._next_player = \
                self._next_player, self._current_player
            self._num_rounds = self._num_rounds + 1
            final_move_moment = time.time()
            elapsed_move_time = final_move_moment - initial_move_moment
            if first_player:
               first_player_total_time += elapsed_move_time
            else:
               second_player_total_time += elapsed_move_time
            first_player = not first_player

        if initial_player._player == 0:
            agent_performance.player_x_total_time = first_player_total_time
            agent_performance.player_o_total_time = second_player_total_time
        else:
            agent_performance.player_o_total_time = first_player_total_time
            agent_performance.player_x_total_time = second_player_total_time

        self._show_board()
        if self._board.winner is None:
            print("It's a draw!")
            agent_performance.num_draws += 1
        else:
            print("Congratulations, {} won!".format(
                PLAYER_NAMES[self._board.winner]))

            if self._board.winner == Player.X:
                agent_performance.num_x_wins += 1

            if self._board.winner == Player.O:
                agent_performance.num_o_wins += 1
        print("Player X time: " + str(agent_performance.player_x_total_time))
        print("Player O time: " + str(agent_performance.player_o_total_time))
        return agent_performance
       
        
        

    def _show_board(self):
        self._board.print_board()
        print("")

    def _make_next_move(self):
        move = self._current_player[1].next_move(deepcopy(self._board))

        assert move.player == self._current_player[0]
        assert self._board.cell(move.row, move.col) == CellState.EMPTY

        self._board.set_cell(move.player, move.row, move.col)

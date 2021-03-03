import random

from tic_tac_toe.player import Player
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.agents.base_agent import Agent, Move

#makes a random move among its available moves
class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        num_empty = 0
        counter = 0
        for i in range(board.size):
            for j in range(board.size):
                if board.cell(i, j) == CellState.EMPTY:
                    num_empty += 1

        if num_empty != 0:
            rand_guy = random.randint(1, num_empty)
            for i in range(board.size):
                for j in range(board.size):
                    if board.cell(i, j) == CellState.EMPTY:
                        counter += 1
                        if rand_guy == counter:
                            return Move(self._player, i, j)
        
                    
                


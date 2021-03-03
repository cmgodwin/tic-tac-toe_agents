# Optimal Tic-Tac-Toe Agents

The main purpose of this project was to implement brute force and alpha-beta pruning agents that play tic-tac-toe optimally.

To try out the code, download runnable_code and run the main.py file with python using a command line.

The two other files in the root of the repository are my main contribution to the code. The rest of the code was provided as the basis for the assignment.

The brute-force agent is an optimal tic-tac-toe player utilizing the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax)

The alpha-beta agent improves on the brute-force agent by implementing [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

Since they both make optimal choices, the moves made by these two as tic-tac-toe players are not different. However, the execution time for the alpha-beta agent is significantly lower, since it ignores large portions of the game tree that are irrelevant.

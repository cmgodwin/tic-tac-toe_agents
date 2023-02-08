# Optimal Tic-Tac-Toe Agents

The main purpose of this project was to implement brute force and alpha-beta pruning agents that play tic-tac-toe optimally.

To try out the code, and run the `main.py` file in the `runnable_code` folder.

The two other files in the root of the repository are my main contribution to the code, along with the user-input and stats collecting in main.py. The rest of the code was provided as the basis for the assignment.

The brute-force agent is an optimal tic-tac-toe player utilizing the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax).

The alpha-beta agent improves on the brute-force agent by implementing [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

Since they both make optimal choices, the moves made by these two as tic-tac-toe players are not different. However, the execution time for the alpha-beta agent is significantly lower, since it ignores large portions of the game tree that are irrelevant.

To demonstrate this, here are the first three moves from two different games, one between two brute-force agents and one between two alpha-beta agents:

<img src="https://github.com/cmgodwin/tic-tac-toe_agents/blob/main/agent_output/brute_force_moves.png?raw=true" height=527><img src="https://github.com/cmgodwin/tic-tac-toe_agents/blob/main/agent_output/alpha-beta_moves.png?raw=true">

We can see that the amount of states processed by the brute-force method for each move is much higher. As a result, the brute-force agents take about 11 seconds to play out a full 3x3 tic-tac-toe game, while the alpha-beta agents take just under 1 second. 

import time

from tic_tac_toe.game import Player, Game, Performance
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.bruteforce_agent import BruteForceAgent
from tic_tac_toe.agents.alpha_beta_agent import AlphaBetaAgent
from tic_tac_toe.agents.suboptimal_agent import SuboptimalAgent

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent),
    ("Bruteforce Agent", BruteForceAgent),
    ("Alpha-Beta Agent", AlphaBetaAgent),
    ("Suboptimal Agent", SuboptimalAgent)
]


def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = ", ".join(
                map(lambda x: "{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: {}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent

        except ValueError:
            return None


    agent = _try_pick()

    while agent is None:
        print("Incorect selection, try again.")
        agent = _try_pick()

    return AGENTS[agent][1](player)

'''
def main():
    #prompts for board size, winning sequence length, and starting at a random state
    board_size = int(input("Enter N for an NxN board: "))
    k = int(input("Enter the winning sequence length K: "))
    random_state = str(input("Start the game at a random state? y/n: "))
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"
    num_simulations = 1
    num_times = 1
    performance = Performance()

    num_x_wins = 0
    num_o_wins = 0
    num_draws = 0
    player_x_total_time = 0
    player_o_total_time = 0

    while play == "y":
        for i in range(num_times):
            game = Game(player_x, player_o)
            performance = game.play(board_size, k, random_state)

            num_x_wins += performance.num_x_wins
            num_o_wins += performance.num_o_wins
            num_draws += performance.num_draws
            player_x_total_time += performance.player_x_total_time
            player_o_total_time += performance.player_o_total_time


        player_x_average_runtime = player_x_total_time / num_simulations
        player_o_average_runtime = player_o_total_time / num_simulations

        #outputs for relevant stats, including average runtime for each player, number of draws, number of wins for each player, and the state space
        print("Player X's average runtime over " + str(num_simulations) + " simulations was " + str(player_x_average_runtime) + " seconds")
        print("Player O's average runtime over " + str(num_simulations) + " simulations was " + str(player_o_average_runtime) + " seconds")
        print("The number of draws was " + str(num_draws))
        print("The number of wins by Player X was " + str(num_x_wins))
        print("The number of wins by Player O was " + str(num_o_wins))

        play = input("Play again? y/[n]: ")
        if play == "y":
            num_times = int(input("How many simulations?: "))
            num_simulations += num_times

if __name__ == "__main__":
    main()
'''
#prompts for board size, winning sequence length, and starting at a random state
board_size = int(input("Enter N for an NxN board: "))
k = int(input("Enter the winning sequence length K: "))
random_state = str(input("Start the game at a random state? y/n: "))
print("Choosing player X...")
player_x = _pick_agent(Player.X)

print("Choosing player O...")
player_o = _pick_agent(Player.O)
play = "y"
num_simulations = 1
num_times = 1
performance = Performance()

num_x_wins = 0
num_o_wins = 0
num_draws = 0
player_x_total_time = 0
player_o_total_time = 0

while play == "y":
    for i in range(num_times):
        game = Game(player_x, player_o)
        performance = game.play(board_size, k, random_state)

        num_x_wins += performance.num_x_wins
        num_o_wins += performance.num_o_wins
        num_draws += performance.num_draws
        player_x_total_time += performance.player_x_total_time
        player_o_total_time += performance.player_o_total_time


    player_x_average_runtime = player_x_total_time / num_simulations
    player_o_average_runtime = player_o_total_time / num_simulations

    #outputs for relevant stats, including average runtime for each player, number of draws, number of wins for each player, and the state space
    print("Player X's average runtime over " + str(num_simulations) + " simulations was " + str(player_x_average_runtime) + " seconds")
    print("Player O's average runtime over " + str(num_simulations) + " simulations was " + str(player_o_average_runtime) + " seconds")
    print("The number of draws was " + str(num_draws))
    print("The number of wins by Player X was " + str(num_x_wins))
    print("The number of wins by Player O was " + str(num_o_wins))

    play = input("Play again? y/[n]: ")
    if play == "y":
        num_times = int(input("How many simulations?: "))
        num_simulations += num_times

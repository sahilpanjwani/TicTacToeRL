from game import Game
from human_player import HumanPlayer
from rl_player import RLPlayer
# from q_learner import QLearner


play_another_one = 'y'
player_x = RLPlayer("test_02", 0.1, 0.1)
player_o = HumanPlayer()
while play_another_one == 'y':
    g = Game(player_x, player_o)
    g.run_game()
    player_x, player_o = player_o, player_x
    play_another_one = input("Play another one? (y/n)-")

# q = QLearner("test_01", 0.1)
# print("here")

# player_x = RLPlayer("test_02", 0.1, 0.1)
# player_o = RLPlayer("test_03", 0.1, 0.1)
# for i in range(10000):
#     print("game number- ", i+1)
#     g = Game(player_x, player_o)
#     g.run_game()
#     player_x, player_o = player_o, player_x

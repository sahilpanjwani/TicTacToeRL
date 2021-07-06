from game import Game
from human_player import HumanPlayer

g = Game(HumanPlayer(), HumanPlayer())
winner = g.run_game()
print(winner)
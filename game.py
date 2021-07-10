from board import Board


class Game:
    def __init__(self, player_x, player_o):
        self._board = Board()
        self._player_x = player_x
        self._player_o = player_o
        self._current_player = player_x

    def run_game(self):
        # print("Starting a new game.")
        is_game_complete = False
        winner_symbol = None
        while not is_game_complete:
            self._board.print_board()
            move_tuple = ()
            current_player_symbol = self.__get_player_symbol(self._current_player)
            non_current_player_symbol = self.__get_player_symbol(self.__get_non_current_player())
            while not self._board.make_move(move_tuple, current_player_symbol):
                move_tuple = self._current_player.move(self._board, current_player_symbol, non_current_player_symbol)
            self.__get_non_current_player().update_opponent_move(self._board, non_current_player_symbol, current_player_symbol)
            is_game_complete, winner_symbol = self._board.check_game_complete_and_get_winner_symbol()
            self.__switch_player()
        self.__forward_match_winner_results(winner_symbol)
        if winner_symbol:
            print("Player {player_symbol} won.".format(player_symbol=winner_symbol))
        else:
            print("It's a draw.")

    def __get_non_current_player(self):
        return self._player_x if self._current_player == self._player_o else self._player_o

    def __forward_match_winner_results(self, winner_symbol):
        self._player_x.receive_game_results('x', winner_symbol)
        self._player_o.receive_game_results('o', winner_symbol)

    def __get_player_symbol(self, player):
        if player == self._player_x:
            return "x"
        elif player == self._player_o:
            return "o"

    def __switch_player(self):
        self._current_player = self._player_o if (self._current_player == self._player_x) else self._player_x

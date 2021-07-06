from board import Board


class Game:
    def __init__(self, player_x, player_o):
        self._board = Board()
        self._player_x = player_x
        self._player_o = player_o
        self._current_player = player_x
        self._winning_player = None

    def run_game(self, verbose=True):
        if verbose:
            print("Starting a new game.")
        is_game_complete = False
        winner_symbol = None
        while not is_game_complete:
            self._board.print_board()
            move_tuple = ()
            player_symbol = self.__get_player_symbol(self._current_player)
            while not self._board.make_move(move_tuple, player_symbol):
                if verbose:
                    print("Player {player_symbol}'s turn to enter a valid move.".format(player_symbol=player_symbol))
                move_tuple = self._current_player.move()
            is_game_complete, winner_symbol = self._board.check_game_complete_and_get_winner_symbol()
            self.__switch_player()
        self.__update_winning_player(winner_symbol)
        if verbose:
            if self._winning_player:
                print("Player {player_symbol} won.".format(player_symbol=self.__get_player_symbol(self._winning_player)))
            else:
                print("It's a draw.")
        return self._winning_player

    def __update_winning_player(self, winner_symbol):
        if winner_symbol == "x":
            self._winning_player = self._player_x
        elif winner_symbol == "o":
            self._winning_player = self._player_o

    def __get_player_symbol(self, player):
        if player == self._player_x:
            return "x"
        elif player == self._player_o:
            return "o"
        return ""

    def __switch_player(self):
        self._current_player = self._player_o if (self._current_player == self._player_x) else self._player_x
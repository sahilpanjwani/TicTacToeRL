class Board:
    def __init__(self):
        self._board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_board(self):
        print(self.__prettify_board_row(self._board[0]))
        print('-' * 11)
        print(self.__prettify_board_row(self._board[1]))
        print('-' * 11)
        print(self.__prettify_board_row(self._board[2]))

    def get_cell_values(self):
        cell_values = []
        for row in range(0, 3):
            for col in range(0, 3):
                cell_values.append(self._board[row][col])
        return cell_values

    def make_move(self, move_tuple, player_symbol):
        if self.__check_move_validity(move_tuple) and player_symbol in ['x', 'o']:
            self._board[move_tuple[0]][move_tuple[1]] = player_symbol
            return True
        return False

    def check_game_complete_and_get_winner_symbol(self):
        for row in range(0, 3):
            if self.__check_all_x_or_o(self._board[row]):
                return True, self._board[row][0]

        for col in range(0, 3):
            if self.__check_all_x_or_o([self._board[i][col] for i in range(0, 3)]):
                return True, self._board[0][col]

        if self.__check_all_x_or_o([self._board[i][i] for i in range(0, 3)]):
            return True, self._board[0][0]

        if self.__check_all_x_or_o([self._board[i][2 - i] for i in range(0, 3)]):
            return True, self._board[0][2]

        if self.__check_all_cells_full():
            return True, None

        return False, None

    def __check_all_x_or_o(self, list_of_symbols):
        if len(set(list_of_symbols)) == 1 and list_of_symbols[0] != '-':
            return True
        return False

    def __check_all_cells_full(self):
        if '-' not in self._board[0] and '-' not in self._board[1] and '-' not in self._board[2]:
            return True
        return False

    def __check_move_validity(self, move_tuple):
        if len(move_tuple) == 2 and 0 <= move_tuple[0] <= 2 and 0 <= move_tuple[1] <= 2 and self._board[move_tuple[0]][move_tuple[1]] == '-':
            return True
        return False

    def __prettify_board_row(self, row):
        return '|'.join(row).replace('-', '   ').replace('x', ' x ').replace('o', ' o ')
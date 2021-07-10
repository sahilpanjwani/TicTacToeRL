from random import choice
from q_learner import QLearner


class RLPlayer:
    _epsilon_granularity = 10000

    def __init__(self, agent_name, epsilon, alpha):
        self._q_learner = QLearner(agent_name, alpha)
        self._epsilon = int(epsilon * self._epsilon_granularity)
        self._history_of_moves = []
        return

    def move(self, board, player_symbol, opponent_symbol):
        personalized_cell_values = self.__get_personalized_board_cell_values(board, player_symbol, opponent_symbol)
        available_moves_representations = self.__get_available_moves_representations(personalized_cell_values, 's')
        next_move_representation = self.__get_next_move_representation(available_moves_representations)
        self._history_of_moves.append(next_move_representation)
        move_tuple = self.__get_move_tuple(next_move_representation, personalized_cell_values)
        future_board_representations = self.__get_available_moves_representations(list(next_move_representation), 'o')
        self._q_learner.update_current_move_q_values(next_move_representation, future_board_representations)
        return move_tuple

    def update_opponent_move(self, board, player_symbol, opponent_symbol):
        personalized_cell_values = self.__get_personalized_board_cell_values(board, player_symbol, opponent_symbol)
        self._history_of_moves.append(tuple(personalized_cell_values))
        future_board_representations = self.__get_available_moves_representations(personalized_cell_values, 's')
        self._q_learner.update_current_move_q_values(tuple(personalized_cell_values), future_board_representations)

    def receive_game_results(self, player_symbol, winner_symbol):
        if winner_symbol == player_symbol:
            self._q_learner.update_terminal_q_values(self._history_of_moves, 10)
        elif winner_symbol:
            self._q_learner.update_terminal_q_values(self._history_of_moves, -10)
        return

    def __get_next_move_representation(self, available_moves_representations):
        q_values = [self._q_learner.get_q_value(representation) for representation in available_moves_representations]
        if self.__should_select_max_q_value():
            print("exploiting")
            max_q_val = max(q_values)
            indexes = [i for i, x in enumerate(q_values) if x == max_q_val]
            selected_index = choice(indexes)
            return available_moves_representations[selected_index]
        print("exploring")
        return choice(available_moves_representations)

    def __should_select_max_q_value(self):
        pos = ['random'] * self._epsilon + ['max_q_val'] * (self._epsilon_granularity - self._epsilon)
        return True if choice(pos) == 'max_q_val' else False

    def __get_personalized_board_cell_values(self, board, player_symbol, opponent_symbol):
        cell_values = board.get_cell_values()
        personalized_values = []
        for val in cell_values:
            if val == player_symbol:
                personalized_values.append("s")
            elif val == opponent_symbol:
                personalized_values.append("o")
            else:
                personalized_values.append("-")
        return personalized_values

    def __get_available_moves_representations(self, personalized_cell_values, symbol):
        available_moves_representations = []
        for i in range(0, 9):
            if personalized_cell_values[i] == '-':
                available_moves_representations.append(tuple(personalized_cell_values[:i] + [symbol] + personalized_cell_values[i+1:]))
        return available_moves_representations

    def __get_move_tuple(self, next_move_representation, personalized_cell_values):
        for i in range(0, 9):
            if personalized_cell_values[i] != next_move_representation[i]:
                row = int(i / 3)
                col = int(i % 3)
                return row, col

# from os import listdir
# from os.path import isfile, join, isdir
import os
import pickle

class QLearner:
    _q_table_files_dir = "./q_table_files/"

    def __init__(self, agent_name, alpha):
        self._agent_name = agent_name
        self._q_table = self.__load_or_create_q_table()
        self._q_table = self._q_table if self._q_table else {}
        self._alpha = alpha

    def get_q_value(self, representation):
        return self._q_table.get(representation, 0)

    def update_current_move_q_values(self, current_move_representation, future_board_representations):
        if len(future_board_representations) == 0:
            return
        future_moves_q_values = [self.get_q_value(r) for r in future_board_representations]
        max_future_q_val = max(future_moves_q_values)
        cur_q_val = self.get_q_value(current_move_representation)
        cur_q_val = cur_q_val + self._alpha * (max_future_q_val - cur_q_val)
        self._q_table[current_move_representation] = cur_q_val
        return

    def update_terminal_q_values(self, history_of_moves_representations, score):
        move_representation = history_of_moves_representations.pop()
        self._q_table[move_representation] = score
        while len(history_of_moves_representations) > 0:
            move_representation = history_of_moves_representations.pop()
            cur_q_val = self.get_q_value(move_representation)
            score = cur_q_val + self._alpha * (score - cur_q_val)
            self._q_table[move_representation] = score
        self.__write_q_table_file()
        return

    def __load_or_create_q_table(self):
        try:
            filename = self._q_table_files_dir + self._agent_name + '.pickle'
            with open(filename, 'rb') as handle:
                q_dict = pickle.load(handle)
            return q_dict
        except:
            return None

    def __write_q_table_file(self):
        if not os.path.exists(self._q_table_files_dir):
            os.makedirs(self._q_table_files_dir)
        filename = self._q_table_files_dir + self._agent_name + '.pickle'
        with open(filename, 'wb') as handle:
            pickle.dump(self._q_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return

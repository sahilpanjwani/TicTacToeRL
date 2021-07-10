class HumanPlayer:
    def move(self, board, player_symbol, opponent_symbol):
        cell_num = int(input("Enter cell number (between 1 to 9)-"))
        cell_num -= 1
        row = int(cell_num / 3)
        col = int(cell_num % 3)
        return row, col

    def update_opponent_move(self, board, player_symbol, opponent_symbol):
        return

    def receive_game_results(self, player_symbol, winner_symbol):
        return

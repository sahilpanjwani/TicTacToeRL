class HumanPlayer:
    def move(self):
        cell_num = int(input("Enter cell number (between 1 to 9)-"))
        cell_num -= 1
        row = int(cell_num / 3)
        col = int(cell_num % 3)
        return row, col
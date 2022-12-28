from states import X_WIN, O_WIN, DRAW, GAME_CONTINUES


class Game:
    def __init__(self):
        self.field = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.moves_count = 0
        self.state = GAME_CONTINUES

    def is_empty(self, x, y):
        return True if self.field[y][x] == '' else False

    def update_state(self):
        if self.field[0][0] == self.field[0][1] == self.field[0][2] == 'X' \
                or self.field[1][0] == self.field[1][1] == self.field[1][2] == 'X' \
                or self.field[2][0] == self.field[2][1] == self.field[2][2] == 'X' \
                or self.field[0][0] == self.field[1][0] == self.field[2][0] == 'X' \
                or self.field[0][1] == self.field[1][1] == self.field[2][1] == 'X' \
                or self.field[0][2] == self.field[1][2] == self.field[2][2] == 'X' \
                or self.field[0][0] == self.field[1][1] == self.field[2][2] == 'X' \
                or self.field[0][2] == self.field[1][1] == self.field[2][0] == 'X':
            self.state = X_WIN

        elif self.field[0][0] == self.field[0][1] == self.field[0][2] == 'O' \
                or self.field[1][0] == self.field[1][1] == self.field[1][2] == 'O' \
                or self.field[2][0] == self.field[2][1] == self.field[2][2] == 'O' \
                or self.field[0][0] == self.field[1][0] == self.field[2][0] == 'O' \
                or self.field[0][1] == self.field[1][1] == self.field[2][1] == 'O' \
                or self.field[0][2] == self.field[1][2] == self.field[2][2] == 'O' \
                or self.field[0][0] == self.field[1][1] == self.field[2][2] == 'O' \
                or self.field[0][2] == self.field[1][1] == self.field[2][0] == 'O':
            self.state = O_WIN

        elif all((all(self.field[0]), all(self.field[1]), all(self.field[2]))):
            self.state = DRAW

        else:
            self.state = GAME_CONTINUES

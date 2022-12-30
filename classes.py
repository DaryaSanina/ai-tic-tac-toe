from states import X_WIN, O_WIN, DRAW, GAME_CONTINUES


class Action:
    def __init__(self, player='X', cell_x=0, cell_y=0):
        self.player = player
        self.cell_x = cell_x
        self.cell_y = cell_y


class Game:
    def __init__(self):
        self.field = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.moves_count = 0
        self.state = GAME_CONTINUES

    def actions(self) -> list[Action]:
        """
        :return: list of possible actions in current game state (player, cell x coordinate, cell y coordinate)
        """
        if self.state != GAME_CONTINUES:
            return list()

        result = list()
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    result.append(Action(self.player(), i, j))
        return result

    def is_empty(self, x: int, y: int) -> bool:
        """
        :param x: cell x coordinate
        :param y: cell y coordinate
        :return: whether the cell is empty
        """

        return True if self.field[x][y] == '' else False

    def player(self) -> str:
        """
        :return: who's turn it is
        """
        if self.moves_count % 2 == 0:
            return 'X'
        else:
            return 'O'

    def update_state(self) -> None:
        """
        Updates the state of the game: crosses win, zeroes win, draw or the game continues
        """
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

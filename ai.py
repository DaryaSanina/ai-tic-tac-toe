from classes import Game, Action
from states import GAME_CONTINUES
import copy

MAX_DEPTH = 3


def max_value(game: Game, depth: int) -> tuple[int, Action]:
    """
    Calculates the best possible move for X in current situation
    :param game: the game in its current state
    :param depth: current prediction depth
    :return: the maximum possible value of the game (with 1 as X win, 0 as draw and -1 as O win) and the best
    possible action to be able to reach this value
    """
    if game.state != GAME_CONTINUES:
        return game.state, Action()

    if depth >= MAX_DEPTH:
        return 0, game.actions()[0]

    max_ = -1
    action_ = Action()
    for action in game.actions():
        cur_min, cur_action = min_value(result(game, action), depth + 1)
        if cur_min > max_:
            max_ = cur_min
            action_ = action
        if max_ == 1:
            break
    return max_, action_


def min_value(game: Game, depth: int) -> tuple[int, Action]:
    """
        Calculates the best possible move for O in current situation
        :param game: the game in its current state
        :param depth: current prediction depth
        :return: the minimum possible value of the game (with 1 as X win, 0 as draw and -1 as O win) and the best
        possible action to be able to reach this value
        """
    if game.state != GAME_CONTINUES:
        return game.state, Action()

    if depth >= MAX_DEPTH:
        return 0, game.actions()[0]

    min_ = 1
    action_ = Action()
    t = 0
    for action in game.actions():
        cur_max, cur_action = max_value(result(game, action), depth + 1)
        if cur_max < min_:
            min_ = cur_max
            action_ = action
        if min_ == -1:
            break
        t += 1
    return min_, action_


def result(game: Game, action: Action) -> Game:
    """
    Returns the field after the action
    :param game: the game with the field the action is taken on
    :param action: player, cell x coordinate, cell y coordinate
    """
    if game.state != GAME_CONTINUES:
        return game

    new_game = Game()
    new_game.field = copy.deepcopy(game.field)
    new_game.moves_count = copy.deepcopy(game.moves_count)
    new_game.state = copy.deepcopy(game.state)

    if new_game.is_empty(action.cell_x, action.cell_y):
        new_game.field[action.cell_x][action.cell_y] = action.player
        new_game.moves_count += 1
    new_game.update_state()
    return new_game

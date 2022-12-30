import pygame
from states import X_WIN, O_WIN, DRAW, GAME_CONTINUES
from classes import Game
from ai import min_value

pygame.init()

SIZE = (600, 600)
BLUE_COLOR = (3, 165, 252)
WHITE_COLOR = (255, 255, 255)
GREY_COLOR = (150, 150, 150)
pygame.font.init()
FONT = pygame.font.SysFont('Consolas', 64)
game = Game()


def draw_grid(surface: pygame.surface) -> None:
    line_width = 5
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3, 0), (SIZE[0] // 3, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3 * 2, 0), (SIZE[0] // 3 * 2, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3), (SIZE[0], SIZE[1] // 3), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3 * 2), (SIZE[0], SIZE[1] // 3 * 2), line_width)


def draw_x(surface: pygame.surface, cell_x_: int, cell_y_: int) -> None:
    line_width = 10
    x0 = cell_x_ * (SIZE[0] // 3) + line_width
    y0 = cell_y_ * (SIZE[1] // 3) + line_width
    x1 = (cell_x_ + 1) * (SIZE[0] // 3) - line_width
    y1 = (cell_y_ + 1) * (SIZE[1] // 3) - line_width
    pygame.draw.line(surface, WHITE_COLOR, (x0, y0), (x1, y1), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (x1, y0), (x0, y1), line_width)


def draw_o(surface: pygame.surface, cell_x_: int, cell_y_: int) -> None:
    line_width = 10
    x0 = cell_x_ * (SIZE[0] // 3) + 2 * line_width
    y0 = cell_y_ * (SIZE[1] // 3) + 2 * line_width
    x1 = (cell_x_ + 1) * (SIZE[0] // 3) - 2 * line_width
    y1 = (cell_y_ + 1) * (SIZE[1] // 3) - 2 * line_width
    pygame.draw.circle(surface, WHITE_COLOR, ((x0 + x1) // 2, (y0 + y1) // 2), SIZE[0] // 3 // 2, line_width)


def make_move(player: str, x: int, y: int) -> None:
    if game.is_empty(x, y):  # The cell is empty
        if player == 'X':  # It's X's turn
            draw_x(screen, x, y)
        else:  # It's O's turn
            draw_o(screen, x, y)

        game.field[x][y] = player
        game.moves_count += 1


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BLUE_COLOR)
draw_grid(screen)

running = True
while running:
    # Iterate through user actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user clicks the exit button
            running = False
        if event.type == pygame.MOUSEBUTTONUP and game.state == GAME_CONTINUES:
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] // (SIZE[0] // 3)
            cell_y = pos[1] // (SIZE[1] // 3)
            make_move('X', cell_x, cell_y)

    game.update_state()
    if game.state != GAME_CONTINUES:
        screen.fill(GREY_COLOR)
        if game.state == X_WIN:
            text = FONT.render('X wins', True, WHITE_COLOR)
        elif game.state == O_WIN:
            text = FONT.render('O wins', True, WHITE_COLOR)
        elif game.state == DRAW:
            text = FONT.render('Draw', True, WHITE_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (SIZE[0] // 2, SIZE[1] // 2)
        screen.blit(text, text_rect)

    if game.moves_count % 2 != 0:  # It's O's move
        min_value_, action = min_value(game, 1)
        make_move(action.player, action.cell_x, action.cell_y)

    pygame.display.flip()

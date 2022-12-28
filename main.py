import pygame
from states import X_WIN, O_WIN, DRAW, GAME_CONTINUES
from classes import Game

pygame.init()

SIZE = (600, 600)
BLUE_COLOR = (3, 165, 252)
WHITE_COLOR = (255, 255, 255)
GREY_COLOR = (150, 150, 150)
pygame.font.init()
FONT = pygame.font.SysFont('Consolas', 64)
game = Game()


def draw_grid(surface):
    line_width = 5
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3, 0), (SIZE[0] // 3, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3 * 2, 0), (SIZE[0] // 3 * 2, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3), (SIZE[0], SIZE[1] // 3), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3 * 2), (SIZE[0], SIZE[1] // 3 * 2), line_width)


def draw_x(surface, cell_x_, cell_y_):
    line_width = 10
    x0 = cell_x_ * (SIZE[0] // 3) + line_width
    y0 = cell_y_ * (SIZE[1] // 3) + line_width
    x1 = (cell_x_ + 1) * (SIZE[0] // 3) - line_width
    y1 = (cell_y_ + 1) * (SIZE[1] // 3) - line_width
    pygame.draw.line(surface, WHITE_COLOR, (x0, y0), (x1, y1), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (x1, y0), (x0, y1), line_width)


def draw_o(surface, cell_x_, cell_y_):
    line_width = 10
    x0 = cell_x_ * (SIZE[0] // 3) + 2 * line_width
    y0 = cell_y_ * (SIZE[1] // 3) + 2 * line_width
    x1 = (cell_x_ + 1) * (SIZE[0] // 3) - 2 * line_width
    y1 = (cell_y_ + 1) * (SIZE[1] // 3) - 2 * line_width
    pygame.draw.circle(surface, WHITE_COLOR, ((x0 + x1) // 2, (y0 + y1) // 2), SIZE[0] // 3 // 2, line_width)


def make_move(x, y):
    if game.is_empty(x, y):
        if game.moves_count % 2 == 0:  # X turn
            game.field[y][x] = 'X'
            draw_x(screen, x, y)
        else:  # O turn
            game.field[y][x] = 'O'
            draw_o(screen, x, y)
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
        if event.type == pygame.MOUSEBUTTONUP and game.state == "Game continues":
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] // (SIZE[0] // 3)
            cell_y = pos[1] // (SIZE[1] // 3)
            make_move(cell_x, cell_y)

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

    pygame.display.flip()

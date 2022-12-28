import pygame

SIZE = (600, 600)
BLUE_COLOR = (3, 165, 252)
WHITE_COLOR = (255, 255, 255)


def draw_grid(surface):
    line_width = 5
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3, 0), (SIZE[0] // 3, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (SIZE[0] // 3 * 2, 0), (SIZE[0] // 3 * 2, SIZE[1]), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3), (SIZE[0], SIZE[1] // 3), line_width)
    pygame.draw.line(surface, WHITE_COLOR, (0, SIZE[1] // 3 * 2), (SIZE[0], SIZE[1] // 3 * 2), line_width)


pygame.init()

screen = pygame.display.set_mode(SIZE)

running = True
while running:
    # Iterate through user actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user clicks the exit button
            running = False

    screen.fill(BLUE_COLOR)
    draw_grid(screen)

    pygame.display.flip()

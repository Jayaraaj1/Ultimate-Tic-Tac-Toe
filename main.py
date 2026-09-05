import pygame
from ui.renderer import draw_grid, window_size

pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw_grid(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
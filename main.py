import pygame
from game.state import GameState, X, O
from ui.renderer import draw_grid, draw_pieces, window_size

pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

clock = pygame.time.Clock()
running = True
state = GameState()
state.board[0][0] = X
state.board[0][4] = O
state.board[4][4] = X
state.board[8][8] = O

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw_grid(screen)
    draw_pieces(screen, state)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
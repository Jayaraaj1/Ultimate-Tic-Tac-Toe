import pygame
from game.state import GameState, X, O
from ui.renderer import draw_grid, draw_pieces, draw_board_backgrounds, draw_completed_boards, window_size
from ui.input_handler import handle_click

pygame.init()

screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

clock = pygame.time.Clock()
running = True
state = GameState()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_click(state, event.pos)

    screen.fill("white")
    draw_board_backgrounds(screen, state)
    draw_grid(screen)
    draw_pieces(screen, state)
    draw_completed_boards(screen, state)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
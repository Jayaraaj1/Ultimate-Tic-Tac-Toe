import pygame

window_size = 900
cell_size = 100

thin_line_width = 2
thick_line_width = 6

line_colour = "purple"

def draw_grid(screen):
    for i in range(1, 9):
        position = i * cell_size
        if i % 3 == 0:
            pygame.draw.line(screen, line_colour, (0, position), (window_size, position), thick_line_width)
            pygame.draw.line(screen, line_colour, (position, 0), (position, window_size), thick_line_width)
        else:
            pygame.draw.line(screen, line_colour, (0, position), (window_size, position), thin_line_width)
            pygame.draw.line(screen, line_colour, (position, 0), (position, window_size), thin_line_width)
    
    pygame.draw.rect(screen, line_colour, (0, 0, window_size, window_size), thick_line_width)
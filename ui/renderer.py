import pygame
from game.state import X, O

window_size = 900
cell_size = 100
padding = 20

thin_line_width = 2
thick_line_width = 6

line_colour = "black"

piece_width = 6
piece_x_colour = "plum3"
piece_o_colour = "gold3"

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

def draw_pieces(screen, state):
    for board_index in range(9):
        for cell_index in range(9):
            board_row = board_index // 3
            board_column = board_index % 3
            cell_row = cell_index // 3
            cell_column = cell_index % 3
            global_row = board_row * 3 + cell_row
            global_column = board_column * 3 + cell_column
            x = global_column * cell_size
            y = global_row * cell_size
            centre_x = x + cell_size // 2
            centre_y = y + cell_size // 2
            radius = cell_size // 2 - padding
            value = state.board[board_index][cell_index]
            
            if value == X:
                pygame.draw.line(screen, piece_x_colour, (x + padding, y + padding), (x + cell_size - padding, y + cell_size - padding), piece_width)
                pygame.draw.line(screen, piece_x_colour, (x + padding, y + cell_size - padding), (x + cell_size - padding, y + padding), piece_width)
            
            if value == O:
                pygame.draw.circle(screen, piece_o_colour, (centre_x, centre_y), radius, piece_width)
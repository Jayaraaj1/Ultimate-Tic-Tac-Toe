import pygame
from game.state import X, O, draw, ongoing
from pathlib import Path

window_size = 900
cell_size = 100
board_size = cell_size * 3
panel_width = 500
panel_height = 200
padding = 20
completed_padding = 40

thin_line_width = 2
thick_line_width = 6
completed_piece_width = 12

line_colour = "black"

piece_width = 6
piece_x_colour = "plum3"
piece_o_colour = "gold3"

playable_colour = "lavenderblush1"
unplayable_colour = "ivory4"

font_path = str(Path(__file__).resolve().parent.parent / "fonts" / "monocraft" / "Monocraft.ttf")

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
            
def draw_board_backgrounds(screen, state):
    for board_index in range(9):
        board_row = board_index // 3
        board_column = board_index % 3
        x = board_column * board_size
        y = board_row * board_size
        rectangle = pygame.Rect(x, y, board_size, board_size)

        if state.active_board is not None:
            if state.active_board == board_index:
                pygame.draw.rect(screen, playable_colour, rectangle)
        elif state.local_status[board_index] == ongoing:
            pygame.draw.rect(screen, playable_colour, rectangle)
    
def draw_completed_boards(screen, state):
    for board_index in range(9):
        board_row = board_index // 3
        board_column = board_index % 3
        x = board_column * board_size
        y = board_row * board_size
        centre_x = x + board_size // 2
        centre_y = y + board_size // 2
        radius = board_size // 2 - completed_padding
        value = state.local_status[board_index]
        rectangle = pygame.Rect(x + thick_line_width // 2, y + thick_line_width // 2, board_size - thick_line_width, board_size - thick_line_width)
        
        if value == X:
            pygame.draw.rect(screen, unplayable_colour, rectangle)
            pygame.draw.line(screen, piece_x_colour, (x + completed_padding, y + completed_padding), (x + board_size - completed_padding, y + board_size - completed_padding), completed_piece_width)
            pygame.draw.line(screen, piece_x_colour, (x + completed_padding, y + board_size - completed_padding), (x + board_size - completed_padding, y + completed_padding), completed_piece_width)
            
        if value == O:
            pygame.draw.rect(screen, unplayable_colour, rectangle)
            pygame.draw.circle(screen, piece_o_colour, (centre_x, centre_y), radius, completed_piece_width)
            
        if value == draw:
            pygame.draw.rect(screen, unplayable_colour, rectangle)

def draw_game_over(screen, state):
    if state.game_status == ongoing:
        return
    winner_font = pygame.font.Font(font_path, 72)
    restart_font = pygame.font.Font(font_path, 32)
    
    panel_x = (window_size - panel_width) // 2
    panel_y = (window_size - panel_height) // 2
    panel = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
    pygame.draw.rect(screen, "white", panel)
    pygame.draw.rect(screen, "black", panel, 4)
    text_restart_surface = restart_font.render("Press R to Restart", True, "black")
    text_restart_rectangle = text_restart_surface.get_rect(center=(window_size // 2, window_size // 2 + completed_padding))
    screen.blit(text_restart_surface, text_restart_rectangle)
    
    if state.game_status == X:
        text_surface = winner_font.render("X Wins!", True, "black")
        text_rectangle = text_surface.get_rect(center=(window_size // 2, window_size // 2 - completed_padding))
        screen.blit(text_surface, text_rectangle)
    elif state.game_status == O:
        text_surface = winner_font.render("O Wins!", True, "black")
        text_rectangle = text_surface.get_rect(center=(window_size // 2, window_size // 2 - completed_padding))
        screen.blit(text_surface, text_rectangle)
    elif state.game_status == draw:
        text_surface = winner_font.render("Draw", True, "black")
        text_rectangle = text_surface.get_rect(center=(window_size // 2, window_size // 2 - completed_padding))
        screen.blit(text_surface, text_rectangle)
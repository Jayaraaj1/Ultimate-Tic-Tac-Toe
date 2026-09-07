from ui.renderer import window_size, cell_size

def position_to_move(position):
    mouse_x, mouse_y = position
    
    if not((0 <= mouse_x < window_size) and (0 <= mouse_y < window_size)):
        return None
    
    global_column = mouse_x // cell_size
    global_row = mouse_y // cell_size
    board_row = global_row // 3
    board_column = global_column // 3
    board_index = board_row * 3 + board_column
    cell_row = global_row % 3
    cell_column = global_column % 3
    cell_index = cell_row * 3 + cell_column
    
    return (board_index, cell_index)


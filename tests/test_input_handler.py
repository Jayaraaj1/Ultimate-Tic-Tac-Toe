from game.state import GameState, X, O, empty
from ui.input_handler import position_to_move, handle_click

def test_top_left():
    assert position_to_move((0, 0)) == (0, 0)
    assert position_to_move((99, 99)) == (0, 0)

def test_different_cells_in_zero():
    assert position_to_move((100, 0)) == (0, 1)
    assert position_to_move((299, 299)) == (0, 8)
    
def test_into_board_one():
    assert position_to_move((300, 0)) == (1, 0)

def test_centre():
    assert position_to_move((450, 450)) == (4, 4)

def test_random_square():
    assert position_to_move((750, 550)) == (5, 7)
    
def test_bottom_right():
    assert position_to_move((899, 899)) == (8, 8)

def test_outside_the_board():
    assert position_to_move((-1, 0)) is None
    assert position_to_move((0, -1)) is None
    assert position_to_move((900, 0)) is None
    assert position_to_move((0, 900)) is None

def test_click_makes_move():
    state = GameState()

    result = handle_click(state, (50, 50))

    assert result
    assert state.board[0][0] == X
    assert state.current_player == O
    assert state.active_board == 0

def test_illegal_click():
    state = GameState()
    
    handle_click(state, (50, 50))
    
    result = handle_click(state, (450, 450))
    
    assert not result
    assert state.board[4][4] == empty
    assert state.current_player == O
    assert state.active_board == 0

def test_valid_turn():
    state = GameState()
    
    handle_click(state, (50, 50))
    
    result = handle_click(state, (150, 150))
    
    assert result
    assert state.board[0][4] == O
    assert state.current_player == X
    assert state.active_board == 4
    
def test_occupied_cell():
    state = GameState()

    handle_click(state, (50, 50))
    result = handle_click(state, (50, 50))

    assert not result
    assert state.board[0][0] == X
    assert state.current_player == O
    assert state.active_board == 0
    
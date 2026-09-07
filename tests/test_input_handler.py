from ui.input_handler import position_to_move

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

from game.state import GameState, empty, ongoing, X, O, draw

def test_initial_state():
    state = GameState()

    assert state.current_player == X
    assert state.active_board is None
    assert state.game_status == ongoing
    assert state.local_status == [ongoing for x in range(9)]
    
    for board in state.board:
        for cell in board:
            assert cell == empty

def test_opening_move_is_valid():
    state = GameState()

    assert state.is_valid_move(0, 0)
    
def test_invalid_indexes_are_rejected():
    state = GameState()

    assert not state.is_valid_move(9, 0)
    assert not state.is_valid_move(0, 9)
    assert not state.is_valid_move(-1, 0)
    
def test_occupied_cells_are_rejected():
    state = GameState()
    
    state.board[0][1] = X
    
    assert not state.is_valid_move(0, 1)

def test_wrong_active_board():
    state = GameState()
    
    state.make_move(0, 1)
    
    assert state.active_board == 1
    assert not state.is_valid_move(2, 0)
    
def test_completed_local_board():
    state = GameState()
    
    state.make_move(0, 1)
    state.make_move(1, 0)
    state.make_move(0, 2)
    state.make_move(2, 0)
    state.make_move(0, 0)
    
    assert state.local_status[0] == X

def test_completed_overall_game():
    state = GameState()
    
    state.make_move(0, 1)
    state.make_move(1, 0)
    state.make_move(0, 2)
    state.make_move(2, 0)
    state.make_move(0, 0)
    state.make_move(1, 3)
    state.make_move(3, 0)
    state.make_move(2, 3)
    state.make_move(3, 6)
    state.make_move(6, 3)
    state.make_move(3, 3)
    state.make_move(1, 6)
    state.make_move(6, 0)
    state.make_move(2, 6)
    state.make_move(6, 1)
    state.make_move(4, 6)
    state.make_move(6, 2)
    
    assert state.game_status == X
    
def test_make_move_places_x():
    state = GameState()

    result = state.make_move(4, 7)

    assert result
    assert state.board[4][7] == X
    assert state.current_player == O
    assert state.active_board == 7
    
def test_invalid_move():
    state = GameState()
    
    state.active_board = 5
    result = state.make_move(3, 1)
    
    assert not result
    assert state.board[3][1] == empty
    assert state.current_player == X
    assert state.active_board == 5   

def test_x_wins_local_board_row():
    state = GameState()

    state.board[0] = [X, X, X, empty, O, empty, O, empty, empty]

    assert state.check_local_board(0) == X

def test_new_game_has_81_moves():
    state = GameState()
    
    assert len(state.get_legal_moves()) == 81

def test_local_board_draw():
    state = GameState()

    state.board[0] = [X, O, O, O, X, X, O, X, O]

    assert state.check_local_board(0) == draw

def test_overall_game_draw():
    state = GameState()
    
    state.local_status = [X, draw, O, O, X, draw, draw, draw, draw]
    
    assert state.check_game_status() == draw

def test_forced_legal_moves():
    state = GameState()

    state.active_board = 4
    moves = state.get_legal_moves()

    assert len(moves) == 9

    for board_index, cell_index in moves:
        assert board_index == 4
        
def test_destination_board_free_choice():
    state = GameState()
    
    state.local_status[1] = draw
    result = state.make_move(0, 1)
    
    assert result
    assert state.active_board is None
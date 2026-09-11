from game.state import GameState, X, empty
from ai.random_agent import RandomAgent

def test_random_agent_returns_legal_move():
    state = GameState()
    agent = RandomAgent()

    move = agent.choose_move(state)

    assert move in state.get_legal_moves()

def test_respect_active_board():
    state = GameState()
    agent = RandomAgent()
    
    state.active_board = 4
    move = agent.choose_move(state)
    board_index, cell_index = move
    
    assert board_index == state.active_board
    
def test_respect_occupied_cells():
    state = GameState()
    agent = RandomAgent()
    
    state.active_board = 4
    state.board[4] = [X, X, X, X, X, X, X, X, empty]
    move = agent.choose_move(state)
    board_index, cell_index = move
    
    assert board_index == state.active_board
    assert cell_index == 8
    
def test_finished_game():
    state = GameState()
    agent = RandomAgent()
    
    state.game_status = X
    move = agent.choose_move(state)
    
    assert move is None
    
def test_random_agent_changes_no_state():
    state = GameState()
    agent = RandomAgent()

    move = agent.choose_move(state)
    
    assert state.current_player == X
    assert state.active_board is None
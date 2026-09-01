empty = ongoing = 0
X = 1
O = -1
draw = 2

class GameState():
    def __init__(self):
        self.board = [[empty for x in range(9)] for y in range(9)]
        self.local_status = [ongoing for x in range(9)]
        self.current_player = X
        self.active_board = None
        self.game_status = ongoing
    
    def is_valid_move(self, board_index, cell_index):
        if((self.game_status == ongoing) and (0 <= board_index <= 8) and (0 <= cell_index <= 8) and (self.local_status[board_index] == ongoing)):
            if(not((self.active_board is not None) and (self.active_board != board_index))):
                if(self.board[board_index][cell_index] == empty):
                    return True
        
        return False
            

state = GameState()
if True:
    print("Test 1 - Normal opening move")
    state = GameState()
    print(state.is_valid_move(0, 0))  # Expected: True

    print("\nTest 2 - Invalid indexes")
    state = GameState()
    print(state.is_valid_move(9, 0))   # Expected: False
    print(state.is_valid_move(0, 9))   # Expected: False
    print(state.is_valid_move(-1, 0))  # Expected: False

    print("\nTest 3 - Occupied cell")
    state = GameState()
    state.board[0][0] = X
    print(state.is_valid_move(0, 0))  # Expected: False

    print("\nTest 4 - Forced local board")
    state = GameState()
    state.active_board = 4
    print(state.is_valid_move(4, 3))  # Expected: True
    print(state.is_valid_move(3, 3))  # Expected: False

    print("\nTest 5 - Completed local board")
    state = GameState()
    state.local_status[6] = X
    print(state.is_valid_move(6, 2))  # Expected: False

    print("\nTest 6 - Finished overall game")
    state = GameState()
    state.game_status = X
    print(state.is_valid_move(2, 5))  # Expected: False
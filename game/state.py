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
    
    def make_move(self, board_index, cell_index):
        if(not(self.is_valid_move(board_index, cell_index))):
            return False
        self.board[board_index][cell_index] = self.current_player
        if(self.local_status[cell_index] == ongoing):
            self.active_board = cell_index
        else:
            self.active_board = None
        self.current_player = -self.current_player
        return True
            

state = GameState()
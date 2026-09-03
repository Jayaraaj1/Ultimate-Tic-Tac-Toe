empty = ongoing = 0
X = 1
O = -1
draw = 2
winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

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
        self.local_status[board_index] = self.check_local_board(board_index)
        self.game_status = self.check_game_status()
        if self.game_status != ongoing:
            self.active_board = None
        elif(self.local_status[cell_index] == ongoing):
            self.active_board = cell_index
        else:
            self.active_board = None
        self.current_player = -self.current_player
        return True
    
    def check_local_board(self, board_index):
        for line in winning_lines:
            a, b, c = line
            if((self.board[board_index][a] != empty) and (self.board[board_index][a] == self.board[board_index][b] == self.board[board_index][c])):
                return self.board[board_index][a]
        if empty not in self.board[board_index]:
            return draw
        return ongoing
    
    def check_game_status(self):
        for line in winning_lines:
            a, b, c = line
            if((self.local_status[a] in (X, O)) and (self.local_status[a] == self.local_status[b] == self.local_status[c])):
                return self.local_status[a]
        if ongoing not in self.local_status:
            return draw
        return ongoing
    
    def get_legal_moves(self):
        legal_moves = []
        for board_index in range(9):
            for cell_index in range(9):
                if self.is_valid_move(board_index, cell_index):
                    legal_moves.append((board_index, cell_index))
        return legal_moves
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

state = GameState()

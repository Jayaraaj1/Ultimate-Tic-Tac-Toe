import random

class RandomAgent():
    def choose_move(self, state):
        legal_moves = state.get_legal_moves()
        if len(legal_moves) == 0:
            return None
        random_move = random.choice(legal_moves)
        return random_move
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score_to_add):
        self.score += score_to_add

    def get_score(self):
        return self.score

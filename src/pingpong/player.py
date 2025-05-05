class Player():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.score = 0
        self.piece_width = 20
        self.piece_height = 100
        self.increments = 10

    def move(self, key_input, screen_height):
        if(key_input == "UP" and self.pos_y - self.increments >= 0):
            self.pos_y -= self.increments
        if(key_input == "DOWN" and self.pos_y + self.piece_height + self.increments <= screen_height):
            self.pos_y += self.increments
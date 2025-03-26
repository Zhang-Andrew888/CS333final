class Agent():
    def __init__(self, screen_height, screen_width, difficulty = 0.7):
        self.piece_width = 20
        self.piece_height = 100
        self.pos_x = screen_width - self.piece_width
        self.pos_y = screen_height - self.piece_height
        self.score = 0
        self.increments = 10

        # random agent
        self.direction = 1

    def move(self, screen_height):
        if(self.pos_y <= 0 or self.pos_y + self.piece_height >= screen_height):
            self.direction *= -1
        
        self.pos_y += self.direction * self.increments
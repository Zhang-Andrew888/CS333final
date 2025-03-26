class Ball():
    def __init__(self, screen_height, screen_width, speed = 3.5, direction = [1,1]):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.coordinates = [screen_width / 2, screen_height / 2]
        self.speed = speed
        self.direction = direction
        self.radius = 10

    def move(self):
        self.coordinates[0] += self.speed * self.direction[0]
        self.coordinates[1] += self.speed * self.direction[1]
    
    def hitWall(self):
        if(self.coordinates[0] <= 0):
            return -1
        elif(self.coordinates[0] >= self.screen_width):
            return 1
        elif((self.coordinates[1] - self.radius <= 0) or (self.coordinates[1] + self.radius >= self.screen_height)):
            self.direction[1] *= -1
        return 0
    
    def hitPlayer(self, player):
        if (player.pos_x + player.piece_width - player.increments < self.coordinates[0] <= player.pos_x + player.piece_width) and \
        (player.pos_y <= self.coordinates[1] <= player.pos_y + player.piece_height):
            self.direction[0] *= -1

        elif (player.pos_y <= self.coordinates[1] < player.pos_y + player.increments) and \
            (player.pos_x <= self.coordinates[0] <= player.pos_x + player.piece_width):
            self.direction[1] *= -1

        elif (player.pos_y + player.piece_height - player.increments <= self.coordinates[1] < player.pos_y + player.piece_height) and \
            (player.pos_x <= self.coordinates[0] <= player.pos_x + player.piece_width):
            self.direction[1] *= -1

    def hitAgent(self, agent):
        if (agent.pos_x <= self.coordinates[0] < agent.pos_x + agent.increments) and \
        (agent.pos_y <= self.coordinates[1] <= agent.pos_y + agent.piece_height):
            self.direction[0] *= -1

        elif (agent.pos_y <= self.coordinates[1] < agent.pos_y + agent.increments) and \
            (agent.pos_x <= self.coordinates[0] <= agent.pos_x + agent.piece_width):
            self.direction[1] *= -1

        elif (agent.pos_y + agent.piece_height - agent.increments <= self.coordinates[1] < agent.pos_y + agent.piece_height) and \
            (agent.pos_x <= self.coordinates[0] <= agent.pos_x + agent.piece_width):
            self.direction[1] *= -1
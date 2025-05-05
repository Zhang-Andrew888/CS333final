from .player import Player
from .agent import Agent

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
        if(self.coordinates[0] - self.radius<= 0):
            return -1
        elif(self.coordinates[0] + self.radius>= self.screen_width):
            return 1
        elif((self.coordinates[1] - self.radius <= 0) or (self.coordinates[1] + self.radius >= self.screen_height)):
            self.direction[1] *= -1
        return 0
    
    def hitPlayer(self, player: Player):
        if (self.radius + player.piece_width >= self.coordinates[0]):
            if (player.pos_y + player.piece_height) >= (self.coordinates[1] - self.radius) and \
            player.pos_y <= (self.coordinates[1] + self.radius):
                self.direction[0] *= -1

    def hitAgent(self, agent: Agent):
        if (agent.pos_x + agent.piece_width >= self.coordinates[0] - self.radius and
        agent.pos_x <= self.coordinates[0] + self.radius):
        
            if (agent.pos_y + agent.piece_height >= self.coordinates[1] - self.radius and
            agent.pos_y <= self.coordinates[1] + self.radius):
            
                self.direction[0] *= -1
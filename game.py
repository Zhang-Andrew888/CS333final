from agent import Agent
from ball import Ball
from player import Player

class Game:
    def __init__(self, screen_height, screen_width):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.player = Player()
        self.agent = Agent(screen_height, screen_width)
        self.ball = Ball(screen_height, screen_width)
        self.gameActive = False
    
    def update(self, key_input):
        if self.gameActive:
            self.player.move(key_input, self.screen_height)
            self.agent.move(self.screen_height)
            self.ball.move()

            self.ball.hitAgent(self.agent)
            self.ball.hitPlayer(self.player)
            result = self.ball.hitWall()

            if(result == 1):
                self.player.score += 1
                self.reset_ball()
            elif(result == -1):
                self.agent.score += 1
                self.reset_ball()
    
    def reset_ball(self):
        self.ball = Ball(self.screen_height, self.screen_width)
        self.gameActive = False

    def start_Game(self):
        self.gameActive = True

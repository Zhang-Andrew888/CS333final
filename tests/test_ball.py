import unittest
from src.pingpong.ball import Ball
from src.pingpong.player import Player
from src.pingpong.agent import Agent

class testBall(unittest.TestCase):
    def test_Var(self):
        ball = Ball(800, 800, direction=[1,1])
        
        self.assertEqual(ball.coordinates[0], 400)
        self.assertEqual(ball.coordinates[1], 400)
        self.assertEqual(ball.radius, 10)
        self.assertEqual(ball.direction, [1,1])
    
    def test_Move(self):
        ball = Ball(800,800, direction=[1,1])
        x0 = ball.coordinates[0]
        y0 = ball.coordinates[1]
        ball.move()

        self.assertEqual(ball.coordinates[0], x0 + ball.speed)
        self.assertEqual(ball.coordinates[1], y0 + ball.speed)
    
    def test_NotHitWall(self):
        ball = Ball(800, 800, direction=[1,1])
        ball.coordinates = [300,400]
        hit = ball.hitWall()

        self.assertEqual(hit, 0)
    
    def test_TopHitWall(self):
        ball = Ball(800, 800, direction=[1,1])
        ball.coordinates = [200, 790]
        directionY = ball.direction[1]
        hit = ball.hitWall()

        self.assertEqual(hit, 0)
        self.assertEqual(directionY * -1, ball.direction[1])
    
    def test_BottomHitWall(self):
        ball = Ball(800, 800, direction=[1,1])
        ball.coordinates = [200, 10]
        directionY = ball.direction[1]
        hit = ball.hitWall()

        self.assertEqual(hit, 0)
        self.assertEqual(directionY * -1, ball.direction[1])
    
    def test_HitPlayerWall(self):
        ball = Ball(800, 800, direction=[1,1])
        ball.coordinates = [10, 200]
        hit = ball.hitWall()

        self.assertEqual(hit, -1)

    def test_HitAgentWall(self):
        ball = Ball(800, 800, direction=[1,1])
        ball.coordinates = [790, 200]
        hit = ball.hitWall()

        self.assertEqual(hit, 1)
    
    def test_NotHitPlayer(self):
        ball = Ball(800, 800, direction=[1,1])
        player = Player()
        direction = ball.direction
        ball.hitPlayer(player)

        self.assertEqual(ball.direction, direction)
    
    def test_WithinXNotHitPlayer(self):
        ball = Ball(800, 800, direction=[1,1])
        player = Player()
        ball.coordinates = [20,500]
        direction = ball.direction
        ball.hitPlayer(player)

        self.assertEqual(ball.direction, direction)
    
    def test_HitPlayer(self):
        ball = Ball(800, 800, direction=[1,1])
        direction = [1,1]
        ball.coordinates = [20,510]

        player = Player()
        player.pos_y = 510

        ball.hitPlayer(player)

        self.assertEqual(ball.direction[0], direction[0] * -1)
    
    def test_NotHitAgent(self):
        ball = Ball(800, 800, direction=[1,1])
        agent = Agent(800, 800)
        direction = ball.direction
        ball.hitAgent(agent)

        self.assertEqual(ball.direction, direction)

    def test_WithinXNotHitAgent(self):
        ball = Ball(800, 800, direction=[1,1])
        agent = Agent(800, 800)
        ball.coordinates = [780,500]
        direction = ball.direction
        ball.hitAgent(agent)

        self.assertEqual(ball.direction, direction)
    
    def test_HitAgent(self):
        ball = Ball(800, 800, direction=[1,1])
        agent = Agent(800, 800)
        agent.pos_y = 510
        ball.coordinates = [780,500]
        direction = ball.direction
        ball.hitAgent(agent)

        self.assertEqual(ball.direction, direction)


    

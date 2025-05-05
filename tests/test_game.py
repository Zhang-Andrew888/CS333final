import unittest
from src.pingpong.agent import Agent
from src.pingpong.player import Player
from src.pingpong.ball import Ball
from src.pingpong.game import Game

class testGame(unittest.TestCase):
    def test_Vars(self):
        game = Game(800, 800)

        self.assertFalse(game.gameActive)
        self.assertEqual(game.screen_height, 800)
        self.assertEqual(game.screen_width, 800)
    
    def test_UpdateInactive(self):
        game = Game(800, 800)
        ball = Ball(800, 800)
        game.update("")

        self.assertFalse(game.gameActive)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updatePlayerMoveNoUp(self):
        game = Game(800, 800)
        player = Player()
        player.move("UP", 800)
        agent = Agent(800, 800)
        agent.move(800)
        ball = Ball(800, 800)
        ball.move()

        game.start_Game()
        game.update("UP")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_updatePlayerMoveUp(self):
        game = Game(800, 800)
        player = Player()
        player.pos_y = 400
        player.move("UP", 800)
        game.player.pos_y = 400
        agent = Agent(800, 800)
        agent.move(800)
        ball = Ball(800, 800)
        ball.move()

        game.start_Game()
        game.update("UP")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_updatePlayerMoveNoDown(self):
        game = Game(800, 800)
        player = Player()
        player.pos_y = 800
        player.move("DOWN", 800)
        game.player.pos_y = 800
        agent = Agent(800, 800)
        agent.move(800)
        ball = Ball(800, 800)
        ball.move()

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_uupdatePlayerMoveDown(self):
        game = Game(800, 800)
        player = Player()
        player.move("DOWN", 800)
        agent = Agent(800, 800)
        agent.move(800)
        ball = Ball(800, 800)
        ball.move()

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updateNoInput(self):
        game = Game(800, 800)
        player = Player()
        player.move("", 800)
        agent = Agent(800, 800)
        agent.move(800)
        ball = Ball(800, 800)
        ball.move()

        game.start_Game()
        game.update("")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updatePlayerWin(self):
        game = Game(800, 800)
        game.ball.coordinates = [800, 10]
        ball = Ball(800, 800)

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.score, 1)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
        self.assertFalse(game.gameActive)
    
    def test_updatePlayerLoss(self):
        game = Game(800, 800)
        game.ball.coordinates = [0, 500]
        ball = Ball(800, 800)

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.agent.score, 1)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
        self.assertFalse(game.gameActive)  

    def test_reset_ball(self):
        game = Game(800, 800)
        game.start_Game()
        game.ball.coordinates = [100, 200]
        ball = Ball(800, 800)
        game.reset_ball()

        self.assertEqual(ball.coordinates, game.ball.coordinates)
        self.assertFalse(game.gameActive)
    
    def test_start_Game(self):
        game = Game(800, 800)
        game.start_Game()

        self.assertTrue(game.gameActive)
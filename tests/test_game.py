import unittest
from src.pingpong.agent import Agent
from src.pingpong.player import Player
from src.pingpong.ball import Ball
from src.pingpong.game import Game
from src.configs.settings import HEIGHT, WIDTH

class testGame(unittest.TestCase):
    def test_Vars(self):
        game = Game(HEIGHT, WIDTH)

        self.assertFalse(game.gameActive)
        self.assertEqual(game.screen_height, HEIGHT)
        self.assertEqual(game.screen_width, WIDTH)
    
    def test_UpdateInactive(self):
        game = Game(HEIGHT, WIDTH)
        ball = Ball(HEIGHT, WIDTH)
        game.update("")

        self.assertFalse(game.gameActive)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updatePlayerMoveNoUp(self):
        game = Game(HEIGHT, WIDTH)
        player = Player()
        player.move("UP", HEIGHT)
        agent = Agent(HEIGHT, WIDTH)
        agent.move(HEIGHT)
        ball = Ball(HEIGHT, WIDTH)
        ball.move()

        game.start_Game()
        game.update("UP")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_updatePlayerMoveUp(self):
        game = Game(HEIGHT, WIDTH)
        player = Player()
        player.pos_y = 400
        player.move("UP", HEIGHT)
        game.player.pos_y = 400
        agent = Agent(HEIGHT, WIDTH)
        agent.move(HEIGHT)
        ball = Ball(HEIGHT, WIDTH)
        ball.move()

        game.start_Game()
        game.update("UP")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_updatePlayerMoveNoDown(self):
        game = Game(HEIGHT, WIDTH)
        player = Player()
        player.pos_y = HEIGHT
        player.move("DOWN", HEIGHT)
        game.player.pos_y = HEIGHT
        agent = Agent(HEIGHT, WIDTH)
        agent.move(HEIGHT)
        ball = Ball(HEIGHT, WIDTH)
        ball.move()

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)

    def test_updatePlayerMoveDown(self):
        game = Game(HEIGHT, WIDTH)
        player = Player()
        player.move("DOWN", HEIGHT)
        agent = Agent(HEIGHT, WIDTH)
        agent.move(HEIGHT)
        ball = Ball(HEIGHT, WIDTH)
        ball.move()

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updateNoInput(self):
        game = Game(HEIGHT, WIDTH)
        player = Player()
        player.move("", HEIGHT)
        agent = Agent(HEIGHT, WIDTH)
        agent.move(HEIGHT)
        ball = Ball(HEIGHT, WIDTH)
        ball.move()

        game.start_Game()
        game.update("")

        self.assertEqual(game.player.pos_y, player.pos_y)
        self.assertEqual(game.agent.pos_y, agent.pos_y)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
    
    def test_updatePlayerWin(self):
        game = Game(HEIGHT, WIDTH)
        game.ball.coordinates = [800, 10]
        ball = Ball(HEIGHT, WIDTH)

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.player.score, 1)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
        self.assertFalse(game.gameActive)
    
    def test_updatePlayerLoss(self):
        game = Game(HEIGHT, WIDTH)
        game.ball.coordinates = [0, 500]
        ball = Ball(HEIGHT, WIDTH)

        game.start_Game()
        game.update("DOWN")

        self.assertEqual(game.agent.score, 1)
        self.assertEqual(game.ball.coordinates, ball.coordinates)
        self.assertFalse(game.gameActive)  

    def test_reset_ball(self):
        game = Game(HEIGHT, WIDTH)
        game.start_Game()
        game.ball.coordinates = [100, 200]
        ball = Ball(HEIGHT, WIDTH)
        game.reset_ball()

        self.assertEqual(ball.coordinates, game.ball.coordinates)
        self.assertFalse(game.gameActive)
    
    def test_start_Game(self):
        game = Game(HEIGHT, WIDTH)
        game.start_Game()

        self.assertTrue(game.gameActive)
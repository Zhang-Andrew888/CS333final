from src.pingpong.player import Player
import unittest
from src.configs.settings import HEIGHT

class testPlayer(unittest.TestCase):
    def test_Vars(self):
        player = Player()

        self.assertEqual(player.pos_x, 0)
        self.assertEqual(player.pos_y, 0)
        self.assertEqual(player.score, 0)
    
    def test_MoveNullInput(self):
        player = Player()
        y0 = player.pos_y
        key_input = ""
        player.move(key_input, HEIGHT)

        self.assertEqual(player.pos_y, y0)

    def test_MoveInvalidUp(self):
        player = Player()
        y0 = player.pos_y
        key_input = "UP"
        player.move(key_input, HEIGHT)

        self.assertEqual(player.pos_y, y0)
    
    def test_MoveInvalidDown(self):
        player = Player()
        player.pos_y = 799
        key_input = "DOWN"
        player.move(key_input, HEIGHT)

        self.assertEqual(player.pos_y, 799)
    
    def test_MoveValidDown(self):
        player = Player()
        y0 = player.pos_y + player.increments
        key_input = "DOWN"
        player.move(key_input, HEIGHT)

        self.assertEqual(player.pos_y, y0)

    def test_MoveValidUp(self):
        player = Player()
        player.pos_y = 799
        y0 = player.pos_y - player.increments
        key_input = "UP"
        player.move(key_input, HEIGHT)

        self.assertEqual(player.pos_y, y0)


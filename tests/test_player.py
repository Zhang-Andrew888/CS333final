from src.pingpong.player import Player
import unittest

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
        screen_height = 800
        player.move(key_input, screen_height)

        self.assertEqual(player.pos_y, y0)

    def test_MoveInvalidUp(self):
        player = Player()
        y0 = player.pos_y
        key_input = "UP"
        screen_height = 800
        player.move(key_input, screen_height)

        self.assertEqual(player.pos_y, y0)
    
    def test_MoveInvalidDown(self):
        player = Player()
        player.pos_y = 799
        key_input = "DOWN"
        screen_height = 800
        player.move(key_input, screen_height)

        self.assertEqual(player.pos_y, 799)
    
    def test_MoveValidDown(self):
        player = Player()
        y0 = player.pos_y + player.increments
        key_input = "DOWN"
        screen_height = 800
        player.move(key_input, screen_height)

        self.assertEqual(player.pos_y, y0)

    def test_MoveValidUp(self):
        player = Player()
        player.pos_y = 799
        y0 = player.pos_y - player.increments
        key_input = "UP"
        screen_height = 800
        player.move(key_input, screen_height)

        self.assertEqual(player.pos_y, y0)


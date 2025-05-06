import unittest
from src.pingpong.agent import Agent
from src.configs.settings import HEIGHT, WIDTH

class testAgent(unittest.TestCase):
    def test_Vars(self):
        agent = Agent(HEIGHT, WIDTH)

        self.assertEqual(agent.pos_x, WIDTH - agent.piece_width)
        self.assertEqual(agent.pos_y, HEIGHT - agent.piece_height)
        self.assertEqual(agent.score, 0)
    
    def test_AgentChangeDirectionLow(self):
        agent = Agent(HEIGHT, WIDTH)
        agent.pos_y = 0
        agent.direction = -1
        agent.move(HEIGHT)

        self.assertEqual(agent.pos_y, agent.increments)
        self.assertEqual(agent.direction, 1)

    def test_AgentChangeDirectionHigh(self):
        agent = Agent(HEIGHT, WIDTH)
        agent.pos_y = 800
        agent.direction = 1
        agent.move(HEIGHT)

        self.assertEqual(agent.pos_y, HEIGHT - agent.increments)
        self.assertEqual(agent.direction, -1)


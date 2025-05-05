import unittest
from src.pingpong.agent import Agent

class testAgent(unittest.TestCase):
    def test_Vars(self):
        agent = Agent(800, 800)

        self.assertEqual(agent.pos_x, 800 - agent.piece_width)
        self.assertEqual(agent.pos_y, 800 - agent.piece_height)
        self.assertEqual(agent.score, 0)
    
    def test_AgentChangeDirectionLow(self):
        agent = Agent(800, 800)
        agent.pos_y = 0
        agent.direction = -1
        agent.move(800)

        self.assertEqual(agent.pos_y, agent.increments)
        self.assertEqual(agent.direction, 1)

    def test_AgentChangeDirectionHigh(self):
        agent = Agent(800, 800)
        agent.pos_y = 800
        agent.direction = 1
        agent.move(800)

        self.assertEqual(agent.pos_y, 800 - agent.increments)
        self.assertEqual(agent.direction, -1)


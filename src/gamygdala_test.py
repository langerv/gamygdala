import unittest
from gamygdala import Gamygdala

'''
Reminder:
Goal utility: the value the NPC attributes to this goal becoming True ([-1,1]) where a negative value means the NPC does not want this to happen.
Belief likelihood: the likelihood that this information is true ([0, 1]) where 0 means the belief is disconfirmed and 1 means it is confirmed.
Congruence : a number ([-1,1]) where negative values mean this belief is blocking the goal and positive values means this belief facilitates the goal.
'''
class TestEmotionEngine(unittest.TestCase):

    def test_relief(self):
        em = Gamygdala(True)
        agent = em.create_agent('agent-zero')

        goal = em.create_goal_for_agent(agent.name, 'village destroyed', -0.9)
        self.assertIsNotNone(goal)

        print()
        em.appraise_belief(0.6, agent.name, [goal.name], [1.0])

        print()
        em.appraise_belief(0.0, agent.name, [goal.name], [-1.0])

if __name__ == "__main__":
    unittest.main()
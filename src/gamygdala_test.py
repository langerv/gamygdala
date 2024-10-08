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

        #em.start_decay(100)
        em.set_decay(0.4, em.exponential_decay)

        print()
        em.appraise_belief(0.6, agent.name, [goal.name], [1.0])

        em.decay_all()
        em.decay_all()
        em.decay_all()
        em.decay_all()
        em.decay_all()

        # If the likelihood of en event = 0, then it will have no effect. 
        # Here we configure an event to be very likely (e.g. 1 = definite), with congruence to the goal of -1.
        # That way, the goal likelyhood will be updated towards the goal not being met, and as the goal has a utility of -0.9, that should generate relief.
        print()
        em.appraise_belief(1.0, agent.name, [goal.name], [-1.0])

if __name__ == "__main__":
    unittest.main()
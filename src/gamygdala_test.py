import unittest
import time
from gamygdala import Gamygdala

class TestEmotionEngine(unittest.TestCase):

    def test_1_rpg_relief(self):
        # A villager fears his village will be destroyed, then feels relief when he realises this will not gonna happen.
        # Test internal emotions.
        em = Gamygdala()
        em.debug = True

        agent = em.create_agent('villager')

        # Goal creation: agent do not want the village to be destroyed 
        # Goal utility: the value the NPC attributes to this goal becoming True ([-1,1]) where a negative value means the NPC does not want this to happen.
        # Utility negative but > -1 (more important that losing life for example)
        goal = em.create_goal_for_agent(agent.name, 'village destroyed', -0.9)
        self.assertIsNotNone(goal)

        # Test decay for 2s
        em.set_decay(0.1, em.exponential_decay)
        #em.set_decay(0.1, em.linear_decay)

        # Test gain
        em.set_gain(10)

        # Create first belief event
        # Belief likelihood: the likelihood that this information is true ([0, 1]) where 0 means the belief is disconfirmed and 1 means it is confirmed.
        # Congruence : a number ([-1,1]) where negative values mean this belief is blocking the goal and positive values means this belief facilitates the goal.
        print()
        em.appraise_belief(0.6, agent.name, [goal.name], [1.0])

        # Decay emotion and test deletion
        print("\nProcessing decay for 3s... ")
        for _ in range(0, 30):
            em.start_decay(100) # decay every 100ms
            time.sleep(0.1)
        else:
            print()

        # Create second belief event
        # Here the villager has the belief that the destruction of the village is not gonna to happen (Belief is set to 1 and Congruence to goal = -1, blocking the goal)
        # If the likelihood of en event = 0, then it will have no effect. 
        # Here we configure an event to be very likely (e.g. 1 = definite), with congruence to the goal of -1.
        # That way, the goal likelyhood will be updated towards the goal not being met, and as the goal has a utility of -0.9, that should generate relief.
        print()
        em.appraise_belief(1.0, agent.name, [goal.name], [-1.0])

    def test_2_rpg_pride(self):
        # The blacksmith was proud of saving the village by providing it with weapons.
        # Test social emotions.
        pass

if __name__ == "__main__":
    unittest.main()
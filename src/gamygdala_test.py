import unittest
import time
from gamygdala import Gamygdala

class TestEmotionEngine(unittest.TestCase):

    def assert_emotion(self, agent, name, intensity=0.7, is_in=True):
        self.assertEqual(any(emo.name == name and emo.intensity >= intensity for emo in agent.internal_state), is_in)

    def assert_relation(self, agent, name, intensity):
        emotions = [emotion for relation in agent.current_relations for emotion in relation.emotion_list]
        self.assertTrue(any(emo.name == name and emo.intensity >= intensity for emo in emotions))

    def do_something(self, em, secs):
        print(f"\nProcessing decay for {secs}s...")
        for _ in range(0, secs * 10):
            em.start_decay(100) # decay every 100ms
            time.sleep(0.1)
        else:
            print()

    '''
    Test 1 : test internal emotions.
    '''
    def test_1_rpg_relief(self):
        print("\nTEST 1: A villager fears his village will be destroyed, then feels relief when he realises this will not gonna happen.")

        em = Gamygdala()
        em.debug = True

        agent = em.create_agent('Villager')

        # Goal creation: agent do not want the village to be destroyed 
        # Goal utility: the value the NPC attributes to this goal becoming True ([-1,1]) where a negative value means the NPC does not want this to happen.
        # Utility negative but > -1 (more important that losing life for example)
        goal = em.create_goal_for_agent(agent.name, 'village destroyed', -0.9)
        self.assertIsNotNone(goal)

        # Test decay for 2s
        em.set_decay(0.1, em.exponential_decay)
        #em.set_decay(0.1, em.linear_decay)

        # Test gain
        em.set_gain(5)

        # Create first belief event
        # Belief likelihood: the likelihood that this information is true ([0, 1]) where 0 means the belief is disconfirmed and 1 means it is confirmed.
        # Congruence : a number ([-1,1]) where negative values mean this belief is blocking the goal and positive values means this belief facilitates the goal.
        print()
        em.appraise_belief(0.6, agent.name, [goal.name], [1.0])
        self.assert_emotion(agent, 'fear')

        # Decay emotion and test deletion
        self.do_something(em, 3)

        # Create second belief event
        # Here the villager has the belief that the destruction of the village is not gonna to happen (Belief is set to 1 and Congruence to goal = -1, blocking the goal)
        # If the likelihood of en event = 0, then it will have no effect. 
        # Here we configure an event to be very likely (e.g. 1 = definite), with congruence to the goal of -1.
        # That way, the goal likelyhood will be updated towards the goal not being met, and as the goal has a utility of -0.9, that should generate relief.
        print()
        em.appraise_belief(1.0, agent.name, [goal.name], [-1.0])
        self.assert_emotion(agent, 'relief')
        self.assert_emotion(agent, 'fear', 0, False)

    '''
    Test 2 : test social emotions.
    '''
    def test_2_rpg_pride(self):
        print("\nTEST 2: The blacksmith was proud of saving the village by providing it with weapons.")

        em = Gamygdala()
        em.debug = True

        village = em.create_agent('Village')
        blacksmith = em.create_agent('Blacksmith')
        em.create_relation(blacksmith.name, village.name, 1.0)

        # Initial step: Blacksmith happy to live in village with gratitude
        goal_live = em.create_goal_for_agent(blacksmith.name, 'to live', 0.7)
        self.assertIsNotNone(goal_live)
        em.set_decay(0.1, em.exponential_decay)
        em.set_gain(5)
        print()
        em.appraise_belief(1.0, village.name, [goal_live.name], [1.0])
        self.assert_emotion(blacksmith, 'gratitude')
        self.assert_relation(blacksmith, 'happy-for', 0.7)
        self.assert_relation(blacksmith, 'gratitude', 0.7)

        self.do_something(em, 3)

        # Second step: brings the belief that the village is in great danger
        goal_destroyed = em.create_goal_for_agent(blacksmith.name, 'village destroyed', -1.0)
        self.assertIsNotNone(goal_destroyed)
        print()
        em.appraise_belief(0.7, blacksmith.name, [goal_destroyed.name], [1.0])
        self.assert_emotion(blacksmith, 'pity')
        self.do_something(em, 3)
 
        # Third Step: Blacksmith is able to help the village providing weapons
        print()
        em.appraise_belief(1.0, blacksmith.name, [goal_destroyed.name], [-1.0])
        self.assert_emotion(blacksmith, 'happy-for')
        self.assert_emotion(blacksmith, 'gratification')
        self.assert_relation(blacksmith, 'happy-for', 0.8)
        self.assert_relation(blacksmith, 'gratification', 0.8)

if __name__ == "__main__":
    unittest.main()
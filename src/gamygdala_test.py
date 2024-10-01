from gamygdala import Gamygdala

if __name__ == "__main__":
    em = Gamygdala(True)
    agent = em.create_agent('agent-zero')
    goal = em.create_goal_for_agent(agent.name, 'village destroyed', -0.9)

    if goal is not None:
        print()
        em.appraise_belief(0.6, agent.name, [goal.name], [1.0])
        em.print_all_emotions(False)

        print()
        em.appraise_belief(0.0, agent.name, [goal.name], [-1.0])
        em.print_all_emotions(False)

import math

'''
Class Belief
This class is a data structure to store one Belief for an agent
A belief is created and fed into a Gamygdala instance (method Gamygdala.appraise()) for evaluation
Params:
* likelihood: The likelihood of this belief to be true.
* causal_agent_name: The agent's name of the causal agent of this belief.
* affected_goal_names An array of affected goals' names.
* goal_congruences An array of the affected goals' congruences (i.e., the extend to which this event is good or bad for a goal [-1,1]).
* is_incremental: Incremental evidence enforces gamygdala to see this event as incremental evidence for (or against) the list of goals provided, 
                i.e, it will add or subtract this belief's likelihood*congruence from the goal likelihood instead of using the belief as "state" defining the absolute likelihood
'''

class Belief:
    def __init__(self, likelihood, causal_agent_name, affected_goal_names, goal_congruences, is_incremental=False):
        self.is_incremental = is_incremental  # incremental evidence enforces gamygdala to use the likelihood as delta, i.e., it will add or subtract this belief's likelihood from the goal likelihood instead of using the belief as "state" defining the absolute likelihood
        self.likelihood = max(-1, min(1, likelihood))
        self.causal_agent_name = causal_agent_name
        self.affected_goal_names = []
        self.goal_congruences = []
        
        # Copy affected_goal_names
        for name in affected_goal_names:
            self.affected_goal_names.append(name)
        
        # Copy and clamp goal_congruences
        for congruence in goal_congruences:
            self.goal_congruences.append(max(-1, min(1, congruence)))



'''
Original Code:

TUDelft.Gamygdala.Belief = function(likelihood, causalAgentName, affectedGoalNames, goalCongruences, isIncremental) {
	if (isIncremental)
		this.isIncremental=isIncremental;//incremental evidence enforces gamygdala to use the likelihood as delta, i.e, it will add or subtract this belief's likelihood from the goal likelihood instead of using the belief as "state" defining the absolute likelihood
    else
		this.isIncremental=false;
	this.likelihood = Math.min(1,Math.max(-1,likelihood));
    this.causalAgentName = causalAgentName;
    this.affectedGoalNames = [];
    this.goalCongruences = [];
	
	//copy on keep
    for(var i = 0; i < affectedGoalNames.length; i++){
        this.affectedGoalNames.push(affectedGoalNames[i]);   
    }
    for(var i = 0; i < goalCongruences.length; i++){
        this.goalCongruences.push(Math.min(1,Math.max(-1,goalCongruences[i])));   
    }
};
'''
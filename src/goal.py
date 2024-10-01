'''
Class Goal
This class is mainly a data structure to store a goal with it's utility and likelihood of being achieved
This is used as basis for interpreting Beliefs
Params:
* name: The name of the goal
* utility: The utility of the goal, or the value the NPC attributes to this goal becoming True; utility = [-1, 1] where a negative value means the NPC does not want this to happen.
* isMaintenanceGoal: Defines if the goal is a maintenance goal or not. The default is that the goal is an achievement goal, i.e., a goal that once it's likelihood reaches true (1) or false (-1) stays that way.
'''
class Goal:
    def __init__(self, name, utility, is_maintenance_goal=False):
        self.name = name
        self.utility = utility
        self.likelihood = 0.5
        self.calculate_likelihood = False
        self.is_maintenance_goal = is_maintenance_goal


'''
Original Code:

TUDelft.Gamygdala.Goal = function(name, utility, isMaintenanceGoal){
    this.name = name;
    this.utility = utility;
    this.likelihood = 0.5; //The likelihood is unknown at the start so it starts in the middle between disconfirmed (0) and confirmed (1)
	this.calculateLikelyhood=false; //This is set to false, in which case gamygdala assumes beliefs (events) will be used to calculate the goal likelyhood by calculateDeltaLikelihood method. If set to true, instead gamygdala assumes this property is function that calculates the likelyhood, so you can bind this as follows
									//yourGoal.calculateLikelyhood=yourGoalLikelyhoodFunction.bind(yourGoal, [param1, param2, etc...]); This results in yourGoal's calculateLikelyhood property to set to a function that is bound to both this goal object AND the params you need, enabling it to be evaluated by a param free call. (in fact you make your function a method of this goal instance)
	if (isMaintenanceGoal)
		this.isMaintenanceGoal=isMaintenanceGoal; //There are maintenance and achievement goals. When an achievement goal is reached (or not), this is definite (e.g., to a the promotion or not). A maintenance goal can become true/false indefinitely (e.g., to be well-fed)
	else
		this.isMaintenanceGoal=false;
	
}
'''
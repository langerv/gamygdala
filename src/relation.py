from emotion import Emotion

'''
Class Relation
This is the class that represents a relation one agent has with other agents.
It's main role is to store and manage the emotions felt for a target agent (e.g angry at, or pity for).
Each agent maintains a list of relations, one relation for each target agent.
Params:
* target_name: The agent who is the target of the relation.
* like: the relation [-1 and 1].
'''

class Relation:
    def __init__(self, target_name, like):
        self.agent_name = target_name
        self.like = like
        self.emotion_list = []

    def add_emotion(self, emotion):
        added = False
        for existing_emotion in self.emotion_list:
            if existing_emotion.name == emotion.name:
                existing_emotion.intensity += emotion.intensity
                added = True
                break
        
        if not added:
            # Copy on keep, we need to maintain a list of current emotions for the relation,
            # not a list of refs to the appraisal engine
            self.emotion_list.append(Emotion(emotion.name, emotion.intensity))

    def decay(self, gamygdala_instance):
        i = 0
        while i < len(self.emotion_list):
            new_intensity = gamygdala_instance.decay_function(self.emotion_list[i].intensity)
            
            if new_intensity < 0:
                # This emotion has decayed below zero, we need to remove it
                del self.emotion_list[i]
            else:
                self.emotion_list[i].intensity = new_intensity
                i += 1






'''
    Original code:

    /**
    * This is the class that represents a relation one agent has with other agents.
    * It's main role is to store and manage the emotions felt for a target agent (e.g angry at, or pity for).
    * Each agent maintains a list of relations, one relation for each target agent.
    * @class TUDelft.Gamygdala.Relation
    * @constructor 
    * @param {String} targetName The agent who is the target of the relation.
    * @param {double} relation The relation [-1 and 1].
    */
    TUDelft.Gamygdala.Relation = function (targetName, like) {
        this.agentName = targetName ;
        this.like = like;
        this.emotionList = [];
    };

    TUDelft.Gamygdala.Relation.prototype.addEmotion = function(emotion) {
        var added = false;
        for (var i = 0; i < this.emotionList.length; i++){
            if (this.emotionList[i].name === emotion.name){
                /*
                
                if (this.emotionList[i].intensity < emotion.intensity){
                    this.emotionList[i].intensity = emotion.intensity;
                }*/
                this.emotionList[i].intensity += emotion.intensity;
                added = true;
            }    
        }
        if(added === false){
            //copy on keep, we need to maintain a list of current emotions for the relation, not a list refs to the appraisal engine
            this.emotionList.push(new TUDelft.Gamygdala.Emotion(emotion.name, emotion.intensity));   
        }
    };

    TUDelft.Gamygdala.Relation.prototype.decay = function(gamygdalaInstance){
        for (var i = 0; i < this.emotionList.length; i++){
            var newIntensity=gamygdalaInstance.decayFunction(this.emotionList[i].intensity);
            
            if (newIntensity < 0){
                //This emotion has decayed below zero, we need to remove it.
                this.emotionList.splice(i, 1);
            } 
            else {
                this.emotionList[i].intensity = newIntensity;   
            }
        }   
    };
'''

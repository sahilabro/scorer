import numpy as np
import os, json, math

class ALL_scores():
    def __init__(self, json_filename):
        self.filename = json_filename

    def load(self):
        if not os.path.exists(str(self.filename)): 
            return {}
        with open(self.filename, 'r') as f:
            return json.load(f)

    def write(self):        
        with open(self.filename, 'w') as f:
            return (json.dump(self.allScores, f)) 

    def avg(self):
        allScores = self.load()       
        return math.floor(np.mean([np.mean(allScores[uid]) for uid in allScores])*100)/100





class UID_scores(ALL_scores):
    def __init__(self, uid, json_filename):
        self.filename = json_filename
        self.uid = uid                 
        super().__init__(self.filename)
        self.allScores = super().load()   #This would not work for large files. Would iterate through file or use a managed DB for large data sets.       
        if not self.allScores or uid not in self.allScores:
            self.allScores[uid] = []            
    
    def avg(self):
        '''Returns mean of all scores under the uid key'''
        if self.allScores[self.uid] == []: raise Exception('No scores available for this UID.')
        return math.floor(np.mean(self.allScores[self.uid])*100)/100

    def get_all_values(self):
        '''Returns list of all scores under the uid key'''
        return self.allScores[self.uid]

    def append(self, score):
        '''Adds new score under the uid instance'''        
        return self.allScores[self.uid].append(score)

    def __repr__(self):
        return ('UID_Score("%s", "%s")'%(self.uid, self.filename))

    def __str__(self):
        return ('scores: %s    uid: %s    current average: %f'%(str(self.allScores[self.uid]), self.uid, self.avg()))


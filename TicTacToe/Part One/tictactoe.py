import random

class AI():

    def __init__(self, player):
        self.actionValues = dict()#maps (state, action) to (success rate, times)
        self.newValue = 0.1#what a new action starts with
        self.player = player#O, X
    

    def updateActionVal(self, outcome, state, action):
        self.actionValues[(state, action)][0] = (self.actionValues[(state, action)][0] * self.actionValues[(state, action)][1] + outcome)/(self.actionValues[(state, action)][1]+1)
        self.actionValues[(state, action)][1] += 1

    def chooseAction(self, state):
        actions = []#list of (action, value)

        for action in self.actionValues.keys():
            if action[0][0] == state:
                actions.append(action)
            if self.rotate(action)[0] == state:
                actions.append(self.rotate(action))
            if self.rotate(self.rotate(action))[0] == state:
                actions.append(self.rotate(self.rotate(action)))
            if self.rotate(self.rotate(self.rotate(action)))[0] == state:
                actions.append(self.rotate(self.rotate(self.rotate(action))))
        

        for row in range(0, 2):
            for box in range(0, 2):
                if state[box] == "-":
                    act = (row, box)
                    if not(act in actions or self.rotate((state, act)) or self.rotate(self.rotate((state, act))) or self.rotate(self.rotate(self.rotate((state, act))))):
                        actions.append((act, self.newValue))
        
        total = 0
        for a in actions:
            total += a[1]
        
        num = random.randrange(0, total)

        for a in actions:
            num -= a[1]
            if(num <= 0):
                return a[0]

    def rotate(self, stateaction):
        state = stateaction[0]
        action = stateaction[1]

        newBoard = []
        newBoard[0] = [state[2][0], state[1][0], state[0][0]]
        newBoard[1] = [state[2][1], state[1][1], state[0][1]]
        newBoard[2] = [state[2][2], state[1][2], state[0][2]]

        newAct = tuple()
        if action[0] == 0:
            newAct[1] == 2

        if action[0] == 1:
            newAct[1] == 1
        
        if action[0] == 2:
            newAct[1] == 0


        if action[1] == 0:
            newAct[0] == 0

        if action[1] == 1:
            newAct[0] == 1
        
        if action[1] == 2:
            newAct[0] == 2


        return (newBoard, newAct)
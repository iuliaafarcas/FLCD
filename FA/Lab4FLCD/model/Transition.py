class Transition:
    def __init__(self, initialState, value, finalState):
        self.initialState = initialState
        self.value = value
        self.finalState = finalState

    def getStartSate(self):
        return self.initialState

    def setStartSate(self, initialState):
        self.initialState = initialState

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getfinalState(self):
        return self.finalState

    def setfinalState(self, finalState):
        self.finalState = finalState

    def __str__(self):
        return str(self.initialState) + str(self.value) + str(self.finalState)

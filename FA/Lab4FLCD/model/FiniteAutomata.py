from model.Transition import Transition


class FiniteAutomata:

    def __init__(self):
        self.alphabet = []
        self.states = []
        self.finalStates = []
        self.initialState = []
        self.transitions = []

    def get_next_state(self, current_state, value):
        for transition in self.transitions:
            if (current_state == transition.initialState) & (transition.value == value):
                return transition.finalState
        return None

    def is_accepted(self, variable):
        current_state = self.initialState
        for character in variable:
            current_state = self.get_next_state(current_state, character)
            if current_state is None:
                return
        return current_state in self.finalStates

    def writeAlphabet(self):
        str = ""
        str += "Alphabet: "
        for i in self.alphabet:
            str += i
            str += " "
        return str

    def writeStates(self):
        str = ""
        str += "States: "
        for i in self.states:
            str += i
            str += " "
        return str

    def writeFinalStates(self):
        str = ""
        str += "Final states: "
        for i in self.finalStates:
            str += i
            str += " "
        return str

    def writeInitialState(self):
        str = ""
        str += "Initial states: "
        for i in self.initialState:
            str += i
            str += " "
        return str

    def writeTransition(self):
        to_print = "Transition: "
        for elem in self.transitions:
            to_print += str(elem) + " \n"
        return to_print


    def __str__(self):
        return "FiniteAutomaton{ " + "alphabet= " + self.alphabet.__str__() + ", states=" + self.states.__str__() + \
               ", finalStates=" + self.finalStates.__str__() + ", initialState='" + self.initialState + '\'' + \
               ", transitions=" + self.transitions.__str__() + '}'

    def readFromFile(self):
        with open("fa.in", 'r') as file:
            lineNo = 0
            for line in file:
                if lineNo == 0:
                    self.states = line.split("\n")[0].split(" ")
                    lineNo += 1
                elif lineNo == 1:
                    self.alphabet = line.split("\n")[0].split(" ")
                    lineNo += 1
                elif lineNo == 2:
                    self.initialState = line.split("\n")[0]
                    lineNo += 1
                elif lineNo == 3:
                    self.finalStates = line.split("\n")[0]
                    lineNo += 1
                else:
                    transitions_parts = line.split("\n")[0].split(" ")
                    transition = Transition(transitions_parts[0], transitions_parts[1], transitions_parts[2])
                    self.transitions.append(transition)

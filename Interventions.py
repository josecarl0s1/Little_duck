
class Interventions:

    globalVariables = []
    globalCount = 0

    def __init__(self) -> None:
        pass

    def addVariable(self, id, line):
        self.isDefinedAlready(id, line)
        self.globalVariables.append([id, ''])
        self.globalCount += 1

    def setTypes(self, type):
        for num in range(len(self.globalVariables) - self.globalCount, len(self.globalVariables)):
            self.globalVariables[num][1] = type
        self.globalCount = 0

    def printGlobal(self):
        print(self.globalVariables)

    def isDefinedAlready(self, newId, line):
        for var in self.globalVariables:
            if var[0] == newId:
                raise Exception(f"Cannot declare {newId} again, error at line {line}")
    
    def isNotDefined(self, currId, line):
        for var in self.globalVariables:
            if var[0] == currId:
                return
        raise Exception(f"{currId} was not declared, error at line {line}")


inter = Interventions()
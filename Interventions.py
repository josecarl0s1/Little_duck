
class Interventions:

    

    def __init__(self) -> None:
        pass

    #functions for adding to the register variables and setting their types

    #variable registry variables
    variables = {}
    variablesCount = {}
    scope = ''

    def addVariable(self, id, line):
        self.isDefinedAlready(id, line)
        self.variables[self.scope].append([id, '', None]) # id, type, value
        self.variablesCount[self.scope] += 1

    def addValueToVariable (self, id, value): #currently unused
        for elem in self.variables[self.scope]:
            if(elem[0] == id):
                elem[2] = value
            

    def setTypes(self, type): #set type after declaration
        for num in range(len(self.variables[self.scope]) - self.variablesCount[self.scope], len(self.variables[self.scope])):
            self.variables[self.scope][num][1] = type
        self.variablesCount[self.scope] = 0

    
    def setVariableScope(self, scope): #set scope variablles will be saved at
        if scope not in self.variables:
            self.variables[scope] = []
            self.variablesCount[scope] = 0
        self.scope = scope

    def isDefinedAlready(self, newId, line): # at decaration checks if it has been declared already
        for var in self.variables[self.scope]:
            if var[0] == newId:
                raise Exception(f"Cannot declare {newId} in {self.scope} scope again, error at line {line}")
        for var in self.variables['global']:
            if var[0] == newId:
                raise Exception(f"The variable {newId} is already declared in global scope, error at line {line}")
    
    def isNotDefined(self, currId, line): #checks if variable used outside definition is declared
        for var in self.variables[self.scope]:
            if var[0] == currId:
                return
        for var in self.variables['global']:
            if var[0] == currId:
                return
        raise Exception(f"{currId} was not declared in {self.scope} scope, error at line {line}")
    
    
    #prtnt @ end for debug puprposes
    def printGlobal(self): #utilityFunction
        print(self.variables)


inter = Interventions()
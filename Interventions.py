
class Interventions:

    

    def __init__(self) -> None:
        pass

    #Functions for adding to the Variable Registerand setting their types

    #variable registry variables
    variables = {}
    variablesCount = {}
    scope = ''

    def addVariable(self, id, line):
        self.isDefinedAlready(id, line)
        self.variables[self.scope].append([id, '', None]) # id, type, value
        self.variablesCount[self.scope] += 1


    def addValueToVariable (self, id, value): #currently unused
        for var in self.variables[self.scope]:
            if(var[0] == id):
                var[2] = value
            

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
    
    def existsInCurrentScope(self, id): #NOTE: variables exist either in currrent scope or global or don't at all
        for var in self.variables[self.scope]: 
            if var[0] == id:
                return True
        return False
    
    def getVariable(self, id, scope):
        for var in self.variables[scope]:
            if var[0] == id:
                return var
        return None
    #Function for Quadruple Generation

    #variables for Quadruple Generation

    #STACKS 
    '''
    NOTE: 
    .append is Push
    [-1] is Peek
    .Pop is Pop
    '''
    POper = [] #pending operators
    PilaO = [] #pending operands
    #QUEUE
    Quad = [] #l_operand, r_operand, operator, result, jumptoIndex
    #semantic cube
    '''
         0 1 2 3
       0 int string float bool
       1
       2
       3 
    '''
    sCube = {
        '+' : [['int', 'string', 'float', None],['string', 'string', 'string', 'string'], ['float', 'string', 'float', None], [None, 'string', None, 'bool']],
        '-': [['int', None, 'float', None],[None, None, None, None],['float', None, 'float', None],[None, None, None, None]],
        '*': [['int', None, 'float', None], [None, None, None, None], [None, None, 'float', None], [None, None, None, 'bool']],
        '/': [['int', None, 'float', None],[None, None, None, None],['float', None, 'float', None],[None, None, None, 'bool']],
        '<': [['bool', None, 'bool', None],[None, 'bool', None, None],['bool', None, 'bool', None],[None, None, None, None]],
        '>': [['bool', None, 'bool', None],[None, 'bool', None, None],['bool', None, 'bool', None],[None, None, None, None]],
        '!=': [['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool']]
    }

    translationDict = {
        'int': 0,
        'string': 1,
        'float': 2,
        'bool': 3
    }

    tempVars = 0

    def addTempVar(self, var):
        self.variables['temp'].append(var)

    def getTempVar(self, id, type):
        return [id, type, None]

    def keyPoint_1(self, id): 
        print("keyPoint_1")
        if not isinstance(id, str):
            self.PilaO.append(id)
            return 
        elif self.existsInCurrentScope(id): #NOTE: if you got here the variable exists either in the current scope or global
            self.PilaO.append(self.getVariable(id, self.scope)) 
        else:
            self.PilaO.append(self.getVariable(id, 'global'))  

    def keyPoint_OperationPush(self, operator): #NOTE: in the diagram this function corresponds to both key point 2, 3 & 8
        print("keyPoint_OperationPush")
        self.POper.append(operator)

    def keyPoint_CreateQuad(self, switch): #takes in line to indicate where an error is found NOTE: 0 corresponds to key point 4, 1 corresponds to key point 5, 2 corresponds to key point 9
        print("keyPoint_CreateQuad ", switch)
        opEval = [['+', '-'], ['*', '/'], ['<', '>', '!=']] #NOTE: we need a case for !=
        print("BEFORE IF ", self.POper, " Operands ", self.PilaO)
        if not self.POper:
            return 
        print("Before POper ", self.POper[-1], ' ', opEval[switch])
        if self.POper[-1] in opEval[switch]:
            #l_operand, r_operand, operator, result, jumptoIndex
            print("ENTERS HERE")
            r_operand = self.PilaO.pop()
            l_operand = self.PilaO.pop()
            operator = self.POper.pop()
            result_Type = self.sCube[operator][self.translationDict[l_operand[1]]][self.translationDict[r_operand[1]]]
            print("RESUL>T TYPE IS: ", result_Type)
            if result_Type is not None: 
                #result <- AVAIL.next()
                print("ENTERS IF")
                quadLine = [operator, l_operand, r_operand, self.tempVars] #tempVars is an address
                self.Quad.append(quadLine)
                self.PilaO.append(self.getTempVar(self.tempVars, result_Type))
                #self.addTempVar(self.getTempVar(result_Type)) NOTE: IMPLEMENT ID NECESSARY
                self.tempVars += 1
                #NOTE: if we weare to clear the temporary variables here is where we would do it
            else:
                raise Exception('Type Mismatch at line')
        print("Man")
            
    def keyPoint_PushBottom(self): 
        print("keyPoint_PushBottom")
        self.POper.append('(')

    def keyPoint_PopFalse(self):
        print("keyPoint_PopFalse")
        self.POper.pop()
    
    #prtnt @ end for debug puprposes
    def printGlobal(self): #utilityFunction
        #print(self.variables)
        print(self.Quad)
    


inter = Interventions()
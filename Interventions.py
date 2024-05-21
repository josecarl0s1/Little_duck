
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
    
    def getVariable(self, id, scope): #returns variable with an address in the place of where value would be in its normal directory
        for index, var in enumerate(self.variables[scope]):
            if var[0] == id:
                return [var[0], var[1], [scope, index]]
        return None
    #Functions for Quadruple Generation

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
    Quad = [] #l_operand, r_operand, operator, resultIndex NOTE: results are saved in the variables dictionary with the 'temp' key
    minusOne = False #important if there is a negative one
    #semantic cube
    '''
        0   1      2     3
        int string float bool        
    '''
    sCube = {
        '+' : [['int', 'string', 'float', None],['string', 'string', 'string', 'string'], ['float', 'string', 'float', None], [None, 'string', None, 'bool']],
        '-': [['int', None, 'float', None],[None, None, None, None],['float', None, 'float', None],[None, None, None, None]],
        '*': [['int', None, 'float', None], [None, None, None, None], ['float', None, 'float', None], [None, None, None, 'bool']],
        '/': [['int', None, 'float', None],[None, None, None, None],['float', None, 'float', None],[None, None, None, 'bool']],
        '<': [['bool', None, 'bool', None],[None, 'bool', None, None],['bool', None, 'bool', None],[None, None, None, None]],
        '>': [['bool', None, 'bool', None],[None, 'bool', None, None],['bool', None, 'bool', None],[None, None, None, None]],
        '!=': [['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool'],['bool', 'bool', 'bool', 'bool']],
        '=': [['int', 'string', 'float', None],['string', 'string', 'string', None], ['float', 'string', 'float', None], [None, 'string', None, 'bool']],
        ',': [['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string']],
        'PRINT': [['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string'], ['string', 'string', 'string', 'string']]
    }

    translationDict = {
        'int': 0,
        'string': 1,
        'float': 2,
        'bool': 3
    }

    tempVars = 0

    def addTempVar(self, var):
        if 'temp' not in self.variables: 
            self.variables['temp'] = []
            self.variables['temp'].append(var)
            return
        self.variables['temp'].append(var)

    def getTempVar(self, id, type):
        tempVarId = '$tempVar'+ str(id)
        return [tempVarId, type, ['temp', id]], [tempVarId, type, None]

    def keyPoint_1(self, id, fi=None): 
        #32 is INT, 33 is FLOAT
        if fi is not None:
            if fi == 32: #INT
                self.PilaO.append(['CTE', 'int', int(id)]) #CTE can be named that because in this language variables must begin in lowercase
            elif fi == 33:#FLOAT
                self.PilaO.append(['CTE', 'float', float(id)])
        elif self.existsInCurrentScope(id): #NOTE: if you got here the variable exists either in the current scope or global
            self.PilaO.append(self.getVariable(id, self.scope)) 
        else:
            self.PilaO.append(self.getVariable(id, 'global'))  
        if self.minusOne: 
            self.timesMinusOne()

    def keyPoint_OperationPush(self, operator): #NOTE: in the diagram this function corresponds to both key point 2, 3 & 8
        self.POper.append(operator)

    def keyPoint_CreateQuad(self, switch): #NOTE: 0 corresponds to key point 4, 1 corresponds to key point 5, 2 corresponds to key point 9, 3 corresponds to assignation
        opEval = [['+', '-'], ['*', '/'], ['<', '>', '!='], ['=', ','], ['PRINT']] 
        if not self.POper: #if stack is empty
            return 
        if self.POper[-1] in opEval[switch]:    
            
            #operator, l_operand, r_operand, result
            r_operand = self.PilaO.pop()
            operator = self.POper.pop()
            #special case for 'PRINT'
            if operator == 'PRINT':
                quadLine = [operator, r_operand, None, None]
                self.Quad.append(quadLine)
                return
            
            l_operand = self.PilaO.pop()
            
            
            result_Type = self.sCube[operator][self.translationDict[l_operand[1]]][self.translationDict[r_operand[1]]]
            print("RESULT TYPE", result_Type, " OPERATOR: ", operator)
            print("L OPERAND: ", l_operand[1], " translation dict: ", self.translationDict[l_operand[1]])
            print("R OPERAND: ", r_operand[1], " translation dict: ", self.translationDict[r_operand[1]])
            if result_Type is not None: 

                #special case for =
                if operator == '=':
                    quadLine = [operator, r_operand, None, l_operand] #['=', operator value to be saved, _, memorySpace to save]
                    self.Quad.append(quadLine)
                    return

                tempVar_address, tempVar = self.getTempVar(self.tempVars, result_Type) #get variable address and variable
                self.PilaO.append(tempVar_address)
                self.addTempVar(tempVar) 
                
                quadLine = [operator, l_operand, r_operand, tempVar_address] #create quad line
                self.Quad.append(quadLine)

                self.tempVars += 1
                
                #NOTE: if we weare to clear the temporary variables here is where we would do it
            else:
                raise Exception('Type Mismatch at line')
            
    def timesMinusOne(self):
        l_operand = self.PilaO.pop()
        if l_operand[1] != 'int' and l_operand[1] != 'float':
            raise Exception(f"{l_operand[1]} variable type cannot be negative")
        tempVar_address, tempVar =self.getTempVar(self.tempVars, l_operand[1])
        self.PilaO.append(tempVar_address)
        self.addTempVar(tempVar)
        quadLine = ['*-1', l_operand, None, tempVar_address]
        self.Quad.append(quadLine)
        self.tempVars += 1
        self.minusOne = False

    def setMinusOne(self):
        self.minusOne = True

    def keyPoint_PushBottom(self): 
        self.POper.append('(')

    def keyPoint_PopFalse(self):
        self.POper.pop()

    #Non-Linear Quad

    PJumps = []
    
    
    def createGoToF(self): #this corresponds to the key point 1 on both id versins and key point 2 for the while
       if self.PilaO[-1][1] != 'bool':
        raise Exception(f'if statement must be evaluated against a bool type')
       else:
        result = self.PilaO.pop()
        quad = ['GotoF', result, None, None] #result is variable against which the if will be checked
        self.Quad.append(quad)
        self.PJumps.append(len(self.Quad) - 1)

    def if_Fill(self):
        indexQuadIf = self.PJumps.pop()
        self.Quad[indexQuadIf][3] = len(self.Quad)#assign Goto index in quad

    def else_Fill(self):
        quad = ['Goto', None, None, None]
        self.Quad.append(quad)

        indexQuadElse = self.PJumps.pop()
        self.PJumps.append(len(self.Quad) - 1) #append index to jump to later
        self.Quad[indexQuadElse][3] = len(self.Quad) #assign GotoF index in quad

    def whileKeyOne(self): 
        self.PJumps.append(len(self.Quad))

    def endWhile(self):
        whileExp = self.PilaO.pop()
        if whileExp[1] != 'bool':
            raise Exception("do-while condition must be bool")
        loopBack = self.PJumps.pop()
        quad = ['GOTO', whileExp, None, loopBack] #whileExp is variable against which the while should be eval, loopBack is the index to return to
        self.Quad.append(quad)

    
    #print @ end for debug puprposes
    def printGlobal(self): #utilityFunction
        for quad in self.Quad:
         print(quad, '\n')
        # for dic in self.variables: 
        #     print('Dictionary: ', dic)
        #     for var in self.variables[dic]: 
        #         print("Variable: ", var)

inter = Interventions()
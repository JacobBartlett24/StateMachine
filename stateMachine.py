from operator import indexOf
import re

class stateMachine:

    def __init__(self,paths,userInputs,machineInputs,machineStates,finalStates) -> None:
        self.paths = paths
        self.userInputs = userInputs
        self.machineInputs = machineInputs
        self.machineStates = machineStates
        self.finalStates = finalStates
    
    def printStateMachineInfo(self):
        print('paths:',paths)
        print('userInputs:',userInputs)
        print('machineInputs:',machineInputs)
        print('machineStates:',machineStates)
        print('finalStates:',finalStates)

file = open('proj-1-machine.txt','r')

nestedStrings = set()
listOfSentences = file.readlines()
machineString = ''
paths = []
userInputs = []
machineInputs = []
finalStates = []
machineStates = []

for elm in listOfSentences:
    machineString += elm

for start in range(len(listOfSentences)):
    string = machineString[start:]
    nestedStrings.update(re.findall('\(.*?\)', string))

def breakdownTuple(elm):
    elm = elm.replace('(','')
    elm = elm.replace(')','')
    elm = elm.replace(',','')
    return elm

for elm in nestedStrings:

    elm = breakdownTuple(elm)
    splitElm = elm.split()

    if len(splitElm) == 3 and not splitElm[0].isdigit() and splitElm[1].isdigit() and not splitElm[2].isdigit():
        paths.append(elm)
    elif len(splitElm) == 3 and splitElm[0].isdigit() and splitElm[1].isdigit() and splitElm[2].isdigit():
        userInputs.append(elm)
    elif len(splitElm) == 2:
        machineInputs.append(elm)
    elif len(splitElm) == 1:
        finalStates.append(elm)
    elif len(splitElm) == 3 and not splitElm[0].isdigit() and not splitElm[1].isdigit() and not splitElm[2].isdigit():
        machineStates.append(elm)
        
stateMachine0 = stateMachine(paths,userInputs,machineInputs,machineStates,finalStates)
stateMachine0.printStateMachineInfo()




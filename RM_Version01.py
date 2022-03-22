from operator import indexOf
import re

class stateMachine:

    #get the user input for file name
    def userInput():
        #Get file input
        fileName = input("Please input the file name: ")
        openFile = (fileName, 'r');
        #Whatever tf this does
        listOfSentences = fileName.readlines()
        
        #Get string and check if it meets req
        #For now it checks if the string is empty, otherwise print accepted
        str = ""
        userString1 = input("Please input a string: ")
        if(len(userString1) == 0):
            print("The string is empty, try again.")
        else: 
            print("Accepted")

        #Same for second string
        userString2 = input("Please input another string: ")
        if(len(userString1) == 0):
            print("The string is empty, try again.")
        else: 
            print("Accepted")

        #Exit
        print("Bye bye.")


    #elements of a state machine
    def __init__(self,paths,userInputs,machineInputs,machineStates,finalStates) -> None:
        self.paths = paths
        self.userInputs = userInputs
        self.machineInputs = machineInputs
        self.machineStates = machineStates
        self.finalStates = finalStates

    def setPaths(self,paths):
        self.paths = paths
    
    def __init__(self) -> None:
        pass
    
    #state machine info
    def printStateMachineInfo(self):
        initialState = 'q0'
        print('paths:',paths)
        print('userInputs:',userInputs)
        print('machineInputs:',machineInputs)
        print('machineStates:',machineStates)
        print('finalStates:',finalStates)
        print('initialState:', initialState)

    #removes unneeded chars from tuple
    def breakdownTuple(self,elm):
        elm = elm.replace('(','')
        elm = elm.replace(')','')
        elm = elm.replace(',','')
        return elm

    #WIP
    def fixList(self,unfixedList):
        fixedList = unfixedList[0].split()
        print(fixedList)

    def initializeMachine(self,nestedStrings):
        for elm in nestedStrings:
            elm = self.breakdownTuple(elm)
            splitElm = elm.split()

            #turns machine paths into a list
            if len(splitElm) == 3 and not splitElm[0].isdigit() and splitElm[1].isdigit() and not splitElm[2].isdigit():
                paths.append(splitElm)

            #turns user inputs into a list
            elif len(splitElm) == 3 and splitElm[0].isdigit() and splitElm[1].isdigit() and splitElm[2].isdigit():
                for var in splitElm:
                    userInputs.append(var)

            #turns machine inputs into a list
            elif len(splitElm) == 2:
                for var in splitElm:
                    machineInputs.append(var)

            #turns final states into a list
            elif len(splitElm) == 1:
                finalStates.append(elm)

            #turns machine states into a list
            elif len(splitElm) == 3 and not splitElm[0].isdigit() and not splitElm[1].isdigit() and not splitElm[2].isdigit():
                for var in splitElm:
                    machineStates.append(var)

    #Finds best path 
    def traverseMachine(self):
        currState = 'q0'
        possiblePaths = []
        for elm in userInputs[0]:

            if elm not in machineInputs:
                print('Error: input not in machine inputs')

            
            for innerList in paths:
                for item in innerList:
                    if elm == item:
                        possiblePaths.append(innerList)

            print(possiblePaths)

            for i in range(len(possiblePaths)):
                print('current state:',currState)
                if possiblePaths[i][0] == currState:
                    currState = possiblePaths[i][2]
                    print(possiblePaths[i])
                    
            
            possiblePaths.clear()
        
#script that needs to be refactored into functions

nestedStrings = set()
listOfSentences = file.readlines()
machineString = ''
paths = []
userInputs = []
machineInputs = []
finalStates = []
machineStates = []

#string of entire machine
for elm in listOfSentences:
    machineString += elm

#nest strings into a set
for start in range(len(listOfSentences)):
    string = machineString[start:]
    nestedStrings.update(re.findall('\(.*?\)', string))

#script that needs to be put in state machine init
stateMachine0 = stateMachine()
stateMachine0.initializeMachine(nestedStrings)
stateMachine0.traverseMachine()




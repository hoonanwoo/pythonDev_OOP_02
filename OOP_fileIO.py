import sys
from time import asctime

timeLog = asctime()
#logFile = "C:\Users\Public\pythonCode\logFile"
logFile = "/home/hoonanwoo/Desktop/logFile"

class TEST():                                                                                   #move to external file
    'Base class for ClassTest Functional Flow'
    def __init__(self):
        print(TEST.__doc__)
   

class DMT(TEST):                                                                               #move to external file
    'DMT class for DMT_Test Functional Flow'
    def __init__(self,op_Number):
        self.op_Number = op_Number
         

def initTest(fp):
    testObj_opVal = DMT(0000)
    flexSi = {0:0}
    val = 0
    goWhile = 1
    print('\n\t' + DMT.__doc__ + '\n')
    print('\nModule_\t' + DMT.__name__ + '\n')
    print(DMT.__dict__)

    print('\nFunctionCalledIn_\t' + DMT.__module__ + '\n')
    testObj_opVal.op_Number= raw_input("\nENTER FLEX_BOM: ")

    while(goWhile):
        flexSi[val] = testObj_opVal.op_Number
        goWhile = input("Enter Additional Record? (Use '0' to Quit):  ")
        if(goWhile != 0):
           val = val + 1                                              
           testObj_opVal.op_Number = raw_input("ENTER FLEX_BOM: ") 
           fp.writelines( flexSi.values())                                       
        else:
           print(timeLog , flexSi.items())

    fp.close()

def main():
    fp = open(logFile,'a')
    initTest(fp)


if __name__ == '__main__':
    main()

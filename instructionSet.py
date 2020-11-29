#!/usr/bin/env python
# -*- coding: utf-8 -*-

#babbage analytical machine simulator
#base 10 single digit adder 

#babbage adder func
def addInstruction(addend, accumulator):
    #loops till addend is 0, if accumulator > 9 then carry = 1 
    carry = [0]
    addendReturnArray = []
    accumulatorReturnArray = []
    #0 to addend length. 
    
    for x in range(len(addend)-1,-1,-1):  
        currentAddend = int(addend[x])
        currentAccumulator = int(accumulator[x])
        print("This is addend #",x," = ", currentAddend)
        print("This is accumulator #",x," = ",currentAccumulator)
        while(currentAddend != 0):
            currentAddend = currentAddend - 1
            currentAccumulator = currentAccumulator + 1
            if currentAccumulator > 9:
               carry.append(1)
               currentAccumulator = 0
        
        accumulatorReturnArray.append(currentAccumulator)
    
    print("Addend retrun array: ", addendReturnArray)
    print("Accumulator return array: ", accumulatorReturnArray)
    print("Carry array: ", carry)       

 
#TEST main func
if __name__ == '__main__':
    inputAddend = int(input("Addend: "))
    addendArray = list(str(inputAddend))
    inputAccumulator = int(input("Accumulator: "))
    accumulatorArray = list(str(inputAccumulator))
    
    addInstruction(addendArray,accumulatorArray)
    #addedArray = addInstruction(inputAddend,inputAccumulator)
    #for x in addedArray:
    #print(x)
#TEST INPUT
#1+0 = 0, 1, 0
#0+1 = 0, 1, 0
#1+1 = 0, 2, 0
#9+9 = 0, 8, 1 
#50+50 = 0, 0, 99 
#60+60 = 0, 20, 100
#150+100 = 0, 50, 200

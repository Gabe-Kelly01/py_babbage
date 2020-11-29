#!/usr/bin/env python
# -*- coding: utf-8 -*-

#babbage analytical machine simulator
#base 10 single digit adder 

#babbage adder func
def babbageAdder(addend, accumulator):
    #loops till addend is 0, if accumulator > 9 then carry = 1 
    carry = 0
    while(addend != 0):
        accumulator = accumulator + 1
        addend = addend - 1
        if accumulator > 9:
            carry = 1
            accumulator = 0
    returnArray = [addend, accumulator, carry]
    return returnArray 
 
#TEST main func
if __name__ == '__main__':
    inputAddend = int(input("Addend [0-9]: "))
    inputAccumulator = int(input("Accumulator [0-9]: "))
    addedArray = babbageAdder(inputAddend,inputAccumulator)
    for x in addedArray:
        print(x)
#TEST INPUT
#0+0 = a1: 0, a2: 0, c: 0
#0+1 = a1: 0, a2: 1, c: 0
#1+0 = a1: 0, a2: 1, c: 0
#1+1 = a1: 0, a2: 2, c: 0
#9+9 = a1: 0, a2: 8, c: 1 

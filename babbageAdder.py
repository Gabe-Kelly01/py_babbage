#!/usr/bin/env python
# -*- coding: utf-8 -*-

#babbage analytical machine simulator
#base 10 single digit adder 

#babbage adder func
def babbageAdder(addend, accumulator):
    #loops till addend is 0, if accumulator > 9 then carry = 0
    carry = 0
    while(addend != 0):
        accumulator = accumulator + 1
        addend = addend - 1
        if accumulator > 9:
            carry = 1
            accumulator = 0

    print("addend: ", addend)
    print("accumulator: ", accumulator)
    print("carry: ", carry)
 
#main func
if __name__ == '__main__':
    try:
        inputAddend = int(input("Addend [0-9]: "))
        inputAccumulator = int(input("Accumulator [0-9]: "))
        babbageAdder(inputAddend,inputAccumulator)
    except:
        print("Invalid input ya fucking piece of shit")

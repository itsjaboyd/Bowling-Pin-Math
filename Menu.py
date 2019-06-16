#!/usr/bin/python

# Author: Jason Boyd
# Date: June 16, 2019
# File: BowlingPinMath.py


# This array is used to quicken the computation time as well as complete option 1.
# Much like a hash table, index of list is the base # and value is total pins for perfect triangle.
referenceList = [0, 0, 3, 6]

print("This is the bowling pin math simulator, enter integer.")

menuRunning = True
while menuRunning:
    print("(0) Calculate # of pins on a base")
    print("(1) Will # make a perfect triangle?")
    print("(2) Print the reference list")
    print("(3) Exit program")
    userInput = int(input("Enter a menu item: "))

    if userInput == 0:
        baseInput = int(input("Enter a base number: "))
        total = 0

        # the base wanted is already in the list
        if len(referenceList) > baseInput:
            print("With base " + str(baseInput) + ", it takes " + str(referenceList[baseInput]) + " pins.\n")
        else:
            # figure out pin numbers up until the inputted base
            largestRef = len(referenceList)
            for b in range(largestRef, baseInput + 1, 1):
                total = b + referenceList[b - 1]
                referenceList.append(total)
            print("With base " + str(baseInput) + ", it will take " + str(referenceList[baseInput]) + " pins.\n")

    elif userInput == 1:
        totalInput = int(input("Enter a total pin number: "))
        # at some point in referenceList, the max is exceeded
        if totalInput <= max(referenceList):
            switch = 1
            # Using switch, compare each item in the list to inputted pin total.
            for x in referenceList:
                if x == totalInput:
                    switch = 0
            if switch == 1:
                print("False\n")
            else:
                print("True\n")

        else:

            lookingForBigger = True
            while lookingForBigger:
                # I figured 5 indexes ahead should be a good starting point
                for b in range(len(referenceList), len(referenceList) + 5):
                    total = b + referenceList[b - 1]
                    referenceList.append(total)
                if max(referenceList) > totalInput:
                    lookingForBigger = False
            switch = 1
            for x in referenceList:
                if x == totalInput:
                    switch = 0
            if switch == 1:
                print("False\n")
            else:
                print("True\n")

    elif userInput == 2:
        print("--------------")
        print(referenceList)
        print("--------------\n")

    else:
        menuRunning = False

print("Program exited successfully.")

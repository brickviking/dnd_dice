#!/usr/bin/env python3
# Origin: https://github.com/zwilliamsdev/dnd_dice/blob/master/dnd.py
# Modifications: https://github.com/brickviking/dnd_dice/dnd.py

import sys
import random

# Check provided user input
def verifyNumArgs(check):
    # Need a way to convert a string like 3d6 instead of the separate two integers
    if len(check) == 3:
       # Only two arguments provided, we can proceed
       convertStringToInt(check)
    else:
        usageString

def usageString():
        print("Invalid arguments. Use: dnd.py 'numDice' 'numSides' (dnd.py 3 12)")
        # Return immediately stopping code
        return
    
# Ensure correct values for arguments
def convertStringToInt(check):
    # Verify conversion
    try:
        # Convert arg to int
        argNumDice = int(check[1])
        argNumSides = int(check[2])
        # Verify argument was able to be made an int
        # If this fails exception code runs
        isinstance(argNumDice, int)
        isinstance(argNumSides, int)
    except:
        # Print error message
        print("Arguments must be numbers. Please try again!")
        # Return stopping the code immediately
        return
    # Check to make sure user provided logical numbers
    # for number of dice and number of sides
    verifyRollAmounts(argNumDice, argNumSides)

# Check that user values make sense
def verifyRollAmounts(numDice, numSides):
    maxDice = 100
    # Cannot roll 0 dice or dice with 0 sides
    if(numDice == 0 or numSides == 0):
        # Print message to user
        print("Number of dice or sides cannot be zero.")
        # Return stopping code immediately
        return
    # Cannot roll more than maxDice at once
    if(numDice > maxDice):
        # No real reason why there's an arbitrary limit, let's leave it to 100 dice
        # Print message to user
        print("You can roll a maximum of " + str(maxDice) + " dice.")
        # Return stopping code immediately
        return
    # Sides must be the following: 2, 4, 6, 8, 10, 12, 20,100
    if(numSides % 2 != 0 or numSides < 2 or (numSides > 12 and numSides < 20) or (numSides > 20 and numSides != 100)):
        # Print message to user
        print("Allowed dice sides: 2, 4, 6, 8, 10, 12, 20 and 100.")
        # Return stopping code immediately
        return
    # All tests have passed we can now safely roll the dice!
    rollDice(numDice, numSides)
    
def rollDice(numDice, numSides):
    rolls = 0
    minNumSides = 2
    value = 0
    # need an empty string in here
    out = ""
    out = str(numDice) + "d" + str(numSides) + ": "
    while rolls < numDice:
        roll = random.randint(minNumSides, numSides)
        value += roll
#        print(str(roll))
        rolls += 1
        out = out + str(rolls) + ":" + str(roll) + " "
    out = out + "Total of " + str(value) + "/" + str(numSides*numDice)
    print(out)


class DND:
    ###
    # TODO: Allow multiple pairs of arguments to roll multiple times
    #       Example: dnd.py 1 6 2 12
    # TODO: Allow string inputs like dnd.py 3d6 1d20
    # TODO: Create a help command to tell user how to use program
    # TODO: Create global rules for number of dice, number of sides (nearly done)
    ### 

    # Grab arguments
    userInput = sys.argv
    # Kick off program
    verifyNumArgs(userInput)

    

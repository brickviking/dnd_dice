import sys
import random

# Check provided user input
def verifyNumArgs(check):
    if len(check) == 3:
       # Only two arguments provided, we can proceed
       convertStringToInt(check)
    else:
        print("Invalid arguments. Use: dnd.py 'numDice' 'numSides' (dnd.py 3 12)")
        # Return immeidatly stopping code
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
    maxDice = 5
    # Cannot roll 0 dice or dice with 0 sides
    if(numDice == 0 or numSides == 0):
        # Print message to user
        print("Number of dice or sides cannot be zero.")
        # Return stopping code immediately
        return
    # Cannot roll more than 5 dice at once
    if(numDice > maxDice):
        # Print message to user
        print("You can roll a maximum of " + maxDice + " dice.")
        # Return stopping code immediately
        return
    # Sides must be divisible by 2, at least 2, and at most 12
    if(numSides % 2 != 0 or numSides < 2 or numSides > 12):
        # Print message to user
        print("Allowed dice sides: 2, 4, 6, 8, 10, and 12.")
        # Return stopping code immediately
        return
    # All tests have passed we can now safely roll the dice!
    rollDice(numDice, numSides)
    
def rollDice(numDice, numSides):
    rolls = 0
    minNumSides = 2
    value = 0
    while rolls < numDice:
        roll = random.randint(minNumSides, numSides)
        value += roll
        print("You roll " + str(roll))
        rolls += 1
    print("You rolled a total of " + str(value))

class DND:
    ###
    # TODO: Allow multiple pairs of arguments to roll multiple times
    #       Example: dnd.py 1 6 2 12
    # TODO: Create a help command to tell user how to use program
    ### 

    # Grab arguments
    userInput = sys.argv
    # Kick off program
    verifyNumArgs(userInput)
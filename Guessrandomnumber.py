
#Return where the user is right or wrong

import sys
from random import randint

guess = randint(1,100)

#check if input is integer
def checkInput():
    try:
        userguess = int(raw_input("Guess a number: "))
    except:
        print "Err: Input should be integer"
        
        

    if userguess > guess:
        print "Too high"
    elif userguess < guess:
        print "Too low"
    elif userguess == guess:
        print "Correct guess"

        
while True:
    try:
        checkInput()
    except:
        break

    
        

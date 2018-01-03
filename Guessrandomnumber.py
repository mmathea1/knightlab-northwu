
#Return where the user is right or wrong

import sys
from random import randint


def guess():
    print ("-------------------------------------")
    print "Guess a number between 1 and 500"
    print ("-------------------------------------")


#check if input is integer
def check_input():
    guess = randint(1,50)
    userguess = int(raw_input("Guess: "))
    try:
        if userguess > guess:
            print "Too high"
        elif userguess < guess:
            print "Too low"
        elif userguess == guess:
            print "Correct guess"
    except:
        print "Err: Input should be integer"

    

guess()        
while True:
        check_input()


    
        

import sys
from random import randint

def dice():
        print "Rolling dice..."
        random = randint(1,6)
        print random 
        
while True:       
        roll = raw_input("Roll the dice? Type Y or N: ")
        if roll == "Y":
                dice()
                

        else:
                print("Cannot proceed")
                break

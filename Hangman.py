####guess the word
##user makes input letter guesses
##TODO: set a limit to how many guesses they can use
##TODO: prepare a list of words to use for guesses
##check if the user has inputed a single letter
##check for all instances of the input letter in the hidden word
##print the letters if the they are

##get a list of 10 random wordsX
##pick a random word from the listX
##loop through the word and print dashesX
##guess limit depends on the length of the wordX
##if user is wrong guesses -1
import random

def get_words(filename="../words.txt"):
    with open(filename) as gamewords:
        guessword = [line for line in gamewords]
    return random.choice(guessword).rstrip('\n')

def print_dash():
    word = get_words()
    print word
    print (' _ ' * len(word))

    ##get user input
    for i in word:
        userguess = raw_input("Guess: ")
        ##validation
        if len(userguess) == 1:
            if userguess in word:
                   print "true"
        else:
            print "error"

        
print_dash()


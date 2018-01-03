
##check for all instances of the input letter in the hidden word
##print the letters if the they are

import random

def get_words(filename="../words.txt"):
    with open(filename) as gamewords:
        guessword = [line for line in gamewords]
    return random.choice(guessword).rstrip('\n')

def get_input():
    word = get_words()
    word = list(word)
    usedguess = list()
    guesses = len(word)
    print word
    print (' _ ' * len(word))   

    ##get user input
    for i in word:
        userguess = raw_input("Guess: ").lower()
        ##validation
        if len(userguess) == 1:
            guessed = ''.join(letter if letter in userguess else ' _ ' for letter in word)
            print guessed
        else:
            print "error"


get_input()


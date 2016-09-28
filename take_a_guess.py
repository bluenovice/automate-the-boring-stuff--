import random
import sys
def guess():
    print("I am thinking of a no between 1 to 20")
    compare = 0
    guesses = 0
    no = random.randint(1,20)
    while compare != no:
        print("take a guess")
        campare = input()
        guesses = guesses + 1
        if campare < no:
            print(" YOUR GUESS IS TO LOW")
        elif campare > no:
            print("your guess is too high")
        else:
            print("you are write\n")
            print("no of guesses are " +str(guesses))
            sys.exit()
guess()
        

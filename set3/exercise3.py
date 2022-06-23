"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

from numpy import number


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("Welcome to the guessing game!")
    print("A number between 0 and 50 ?")
    print("OK then, a number between 0 and 50 ?")
    upperBound = int(50)
    lowerBound = int(0)
    guess=0
    actualNumber = random.randint(lowerBound, upperBound)
    while True and guess<20:
            user_input = input(f"Give me a number between {lowerBound} and {upperBound} please: ")
            guess +=1
            #print(guess)
            try:
                  user_input = int(user_input)
                  if(actualNumber == user_input):
                        print(f"You guessed correctly,")
                        return "You got it!"
                  elif lowerBound > user_input or user_input > upperBound: 
                        print("Outside the bounds, try again :'(")
                  elif (user_input < actualNumber):
                        print("Too low, try again")
                  else:
                        print("Too big, try again")
            except:
                  print(f"{user_input} isn't an integer. Enter an integer please") 
    # the tests are looking for the exact string "You got it!". Don't modify that!
            return "You got it!"
if __name__ == "__main__":
      print(advancedGuessingGame())

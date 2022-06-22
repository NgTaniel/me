"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


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
    print("Welcome to my guessing game!")
    print("An integer between 1 and 50 ?")
    upperBound = input("Enter an upper bound: ")
    print(f"OK then, a integer between {1} and {50} ?")
    upperBound = int(50)

    guessing_correct = random.randint(0, 50)

    guessed = False

    while not guessed:
        user_guess = int(input("Guess an integer: "))
        print(f"You guessed {user_guess},")
        if user_guess == guessing_correct:
            print(f"You got it! It was {guessing_correct}")
            guessed = True
        elif user_guess < guessing_correct:
            print("Too low or below the lower bound, try again :(")
        else:
            print("Too high or above the upper bound, try again :(")
    return "You got it!"


    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

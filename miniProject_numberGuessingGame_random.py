import random

import time

print("Welcome to the guessing game. Please guess a number between 1 and 100.")

time.sleep(3)
print("Picking a number ... ")
time.sleep(2)

# ------miniProject3 number Guesser

guess = int(input("What is your guess? :  "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    # -----Add new code here
    if guess < correct_number:
        guess = int(input("Wrong!. you need to guess Higher. What is your guess? : "))
    else:
        guess = int(input("Wrong!. you need to guess Lower. What is your guess? : "))

    # ----------------------

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")

"""
--------1.Expected Result:-Before import random-------
What is your guess? :  1
Wrong!. you need to guess Higher. What is your guess? : 7
Wrong!. you need to guess Lower. What is your guess? : 9
Wrong!. you need to guess Lower. What is your guess? : 6
Wrong!. you need to guess Lower. What is your guess? : 0
Wrong!. you need to guess Higher. What is your guess? : 2
Wrong!. you need to guess Higher. What is your guess? : 4
Wrong!. you need to guess Higher. What is your guess? : 5
YCongrats! The right answer was 5. It took you 8 guesses.

"""

# ------import Random module above: result will be random with range in correct_number (1,100)

"""

--------2.Expected Result:-Before import random-----
#--------------> coding
import random

print("Welcome to the guessing game. Please guess a number between 1 and 100.")

guess = int(input("What is your guess? :  "))
correct_number = random.randint(1,100)
guess_count = 1
#---------------->
What is your guess? :  1
Wrong!. you need to guess Higher. What is your guess? : 7
Wrong!. you need to guess Lower. What is your guess? : 9
Wrong!. you need to guess Lower. What is your guess? : 6
Wrong!. you need to guess Lower. What is your guess? : 0
Wrong!. you need to guess Higher. What is your guess? : 2
Wrong!. you need to guess Higher. What is your guess? : 4
Wrong!. you need to guess Higher. What is your guess? : 5
YCongrats! The right answer was 5. It took you 8 guesses.

"""

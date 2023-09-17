#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
attemps = 0
number_to_guess = random.randint(1, 100)

def check_guess(attemps, number_to_guess):
    while attemps > 0:
        print(f"You have {attemps} remaining to guess the number.")
        attemp_guess = int(input("Make a guess: "))
        if attemp_guess == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}.")
            attemps = 0
        elif attemp_guess > number_to_guess:
            print(f"Too high.")
            attemps -= 1
        else:
            print(f"Too low.")
            attemps -= 1

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    check_guess(10, number_to_guess)
else:
    check_guess(5, number_to_guess)
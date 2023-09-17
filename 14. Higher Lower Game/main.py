'''
FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). 
Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) 
and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of 
the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B 
for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. 
Hope that makes sense :-)
'''
from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Format account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make game repeatable.
while game_should_continue:
    # Generate a random account from the game data.

    # Make B become the next A.
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear screen between rounds.
    os.system('cls')
    # Add art.
    print(logo)

    # Give user Feedback on their guess.
    # Score Keeping.
    if is_correct:
        score += 1
        print(f"You're right!. Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
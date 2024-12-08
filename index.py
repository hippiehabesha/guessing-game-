import random

secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3

print("Welcome to the Number Guessing Game! you have 3 chance to guess correctly.")

while guess_count < guess_limit:
    
    guess = int(input("guess a number from 1 to 10: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number :
        print("Too high! Try again.")
    elif guess < secret_number :
        print("Too low! Try again.")
        
    if guess_count == guess_limit:
        print(f"Sorry, you've run out of guesses. The correct number was {secret_number}.")

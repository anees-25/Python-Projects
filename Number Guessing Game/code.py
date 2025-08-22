import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    # Step 1: Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Step 2: Take user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 3: Compare
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Correct! You guessed the number in {attempts} attempts.")
            break

# Run the game
number_guessing_game()

##EXAMPLE WALKTHROUGH
"""Welcome to the Number Guessing Game!
I have selected a number between 1 and 100.
Enter your guess: 40
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 62
🎉 Correct! You guessed the number in 3 attempts."""
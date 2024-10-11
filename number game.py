import random

def number_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize number of attempts
    attempts = 0
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        # Get user's guess
        user_guess = input("Enter your guess: ")
        
        # Check if input is a valid number
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Increment attempts
        attempts += 1
        
        # Check if guess is correct
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
print()
#How to Play:_

#1. Run the code.
#2. The computer will think of a random number between 1 and 100.
#3. Enter your guess.
#4. The computer will tell you if your guess is too high or too low.
#5. Keep guessing until you get the correct number.



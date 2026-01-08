import random

def play_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} tries.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    print(f"Game over! The number was {number_to_guess}.")

if __name__ == "__main__":
    play_guessing_game()

from replit import clear
from random import randint
from art import logo

def compare_number(guess, secret_number, lives):
  """Compares the guess with the answer and returns the remaining lives."""
  if lives == 1:
    return 
  elif guess > secret_number:
    print(f"Your guess {guess} is too high. You have now {lives - 1} attempts to guess the number.")
  elif guess < secret_number:
    print(f"Your guess {guess} is too low. You have now {lives - 1} attempts to guess the number.")
  else:
    print(f"Awesome! Your guess {guess} is correct!")

def game():

  print(logo)
  print("\nWelcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")

  secret_number = randint(1, 100)

  if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
  else:
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")

  guess = 0
  while guess != secret_number:

    guess = int(input("Make a guess: "))

    compare_number(guess, secret_number, lives)

    lives -= 1
    if lives == 0:
      print(f"You lose. The number was {secret_number}.")

  if input("Do you want to play again? 'y' or 'n': ") == "y":
    clear()
    game()
  else:
    clear()

game()
#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
actual_number = random.randint(0, 100)
difficulty_level = input("Type 'hard' for hard mode (5 chances) or 'easy' for easy mode (10 chances) \n ----> ")
chances = 5 if difficulty_level == 'hard' else 10
while chances > 0:
  user_number = int(input("Enter number b/w 1 and 100 /n ----> "))
  if user_number == actual_number:
    print(f"You Won!!!! Actual Number is {actual_number}")
    break
  else:
    if user_number < actual_number:
      print("You guessed too low.")
    else:
      print('You guessed too high.')
    chances -= 1
  print(f'Total number of chances you have : {chances}')

if chances == 0:
  print(f'You Lose!!!! Actual Number is {actual_number}. You have {chances} to continue the game.')

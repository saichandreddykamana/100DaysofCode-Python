
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

display = ['_' for i in chosen_word]
lives = 6
while True:
  print(f"Number of lives: {lives}")
  if lives == 0:
    print(f'The chosen word is {chosen_word}')
    print("You have no lives. Game Over")
    break
  else:
    if '_' in display:
      print(stages[lives])
      guess = input("Guess a letter: ").lower()
      if guess in chosen_word:
        for i in range(0, len(chosen_word)):
          if chosen_word[i] == guess:
            display[i] = guess
      else:
        print("Guessed wrong")
        lives -= 1
    else:
      print("You guessed all letters. Man is saved. You win")
      break
    print(' '.join(display))

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_continue = True
game_items = [rock, scissors, paper]
win_probabilities = {0:1, 1:2, 2:0}
user_won = False
while game_continue:
    user_input = int(input('Type 0 - rock, 1 - scissor, 2 - paper : \n'))
    if user_input not in range(0, 3):
        print("Enter right option.")
        continue
    else:
        print("You choose : \n", game_items[user_input])
        computer_input = random.randint(0, 2)
        print("Computer Choose : \n", game_items[computer_input])
        if computer_input != user_input:
            game_continue = False
            for (key, value) in win_probabilities.items():
                if key == user_input and value == computer_input:
                    user_won = True
            print("You win!") if user_won else print("Computer Wins!")
        else:
            print("Game Tied. Try one more time.")
            continue

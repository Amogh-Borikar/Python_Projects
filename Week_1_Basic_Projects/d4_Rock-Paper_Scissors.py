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

import random

print("Welcome to the Rock, Paper, Scissors game!")

game_images = [rock, paper, scissors]

user_choice = int(input("Choose 0 for Rock,1 for Paper and 3 for Scissors: "))
system_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("you chose: ")
    print(game_images[user_choice])
    print("system chose: ")
    print(game_images[system_choice])


if user_choice == 0:
    if system_choice == 0:
        print("its a draw")
    elif system_choice == 1:
        print("You lose")
    elif system_choice == 2:
        print("You win")
        
elif user_choice == 1:
    if system_choice == 0:
        print("You win")
    elif system_choice == 1:
        print("its a draw")
    elif system_choice == 2:
        print("You lose")
        
elif user_choice == 2:
    if system_choice == 0:
        print("You lose")
    elif system_choice == 1:
        print("You win")
    elif system_choice == 2:
        print("its a draw")
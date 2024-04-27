import art
from game_data import data
import random
import os
import time

game_continue = True
score = 0

def clear_screen():
    # Clear the terminal in Windows
    if os.name == 'nt':
      os.system('cls')
    # Clear the terminal in Linux and macOS
    else:
      os.system('clear') 

def random_generator():
        for i in range(2):
            var1 = data[random.randint(0, 49)]
            var2 = data[random.randint(0, 49)]
        while var1 == var2:
            var2 = data[random.randint(0, 49)]

        print(f"{var1['name']} is {var1['description']} from {var1['country']}")
        print(art.vs)
        print(f"{var2['name']} is {var2['description']} from {var2['country']}")
        
        return var1, var2

def compare():
    global game_continue
    global score
    if int(var2['follower_count']) >= int(var1['follower_count']) and guess == "high":
        clear_screen()
        score += 1
        print(f"You are correct, your score is now {score}. onto next!")
        time.sleep(3)
    
    elif int(var2['follower_count']) < int(var1['follower_count']) and guess == "low":
        clear_screen()
        score += 1
        print(f"You are correct, your score is now {score}. onto next!")
        time.sleep(3)
    
    elif int(var2['follower_count']) >= int(var1['follower_count']) and guess == "low":
        game_continue = False
        print("That's wrong! Game over!")
        print(var2['name'] + " has " + str(var2['follower_count'])+ "M followers and " + var1['name'] + " has " + str(var1['follower_count'])+ "M followers.")
        print(f"Your final score is {score}.")

    elif int(var2['follower_count']) <= int(var1['follower_count']) and guess == "high":
        game_continue = False
        print("That's wrong! Game over!")
        print(var2['name'] + " has " + str(var2['follower_count'])+ "M followers and " + var1['name'] + " has " + str(var1['follower_count'])+ "M followers.")
        print(f"Your final score is {score}.")
    else:
        return

while game_continue:
    clear_screen()
    print(art.logo)
    print(f"Your current score is {score}.")

    var1, var2 = random_generator()

    guess = input("Guess if the Instagram followers for " + var2['name'] + " are 'high' or 'low' than " + var1['name'] + ": ")

    compare()

    
    
        

    


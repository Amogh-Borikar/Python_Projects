print('''
****************************************
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888
****************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("left is well lit path, right is dark jungle, where do you go?")
direction = input("left or right? ").lower()
if direction == "left":
          print("you came across a lake, do you swim or wait for boat?")
          action = input("swim or wait? ").lower()
          if action == "wait":
                    print("Good choice! after you crossed the lake, you came across 3 doors, Blue, yellow and red. Choose one")
                    door = input("blue, yellow or red? ").lower()
                    if door == "yellow":
                              print("you win, treasure is all yours!")
                    elif door == "blue":
                              print("you fell into river and drowned, Game over!")
                    elif door == "red":
                              print("you fell into fire and burned, Game over!")
                    else:
                              print("You chose a door that doesn't exist, Game over!")
          else:
                    print("you were eaten by crocodiles, Game over!")
else:
          print("you fell into a hole, Game over!")
import random

print("Welcome to the number guessing game!")
print("You have to guess a number between 1 to 100")

def guess_game(attempts):
    number = random.randint(1,100) 
    guess = 0
    attempts_left = attempts
    while guess != number or attempts_left != 0:
        guess = int(input("What is your guess? : "))
        if guess == number:
            print("You win!")
            break
        elif guess > number:
            print("Too High!")
            print(f"you have {attempts_left - 1} attempts left!")
        elif guess < number:
            print("Too Low")
            print(f"you have {attempts_left - 1} attempts left!")
        attempts_left -= 1
        if attempts_left == 0:
            break

game_level = input("Choose your difficulty level from 'easy' and 'hard': ")

while game_level != 'easy' and game_level != 'hard':
    print("wrong input!!")
    game_level = input("Choose again from 'easy' and 'hard': ")

if game_level == "easy":
    attempts = 10
    guess_game(attempts)
elif game_level == 'hard':
    attempts = 5
    guess_game(attempts)
else:
    print("wrong input!!")
    print("enter again between 'easy' or 'hard': ")
import random
import hangman_art
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
#print(f'solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
# if user is correct...
    if guess in display:
        print(f"You've already guessed {guess}, choose another letter.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            print(f"letter {guess} is in the word, good choice, Keep going!")

# if user is wrong...
    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word, you lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

# if user has got all letters...
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
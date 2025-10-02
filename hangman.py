import random
import re
#Using word.txt as a list of words for hangman
with open("words.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]
chosen_word = random.choice(words)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
print("You have 6 lives")
secret = "_"*word_length
print(f'Guess the word {secret} The word is {word_length} long.')
while len(chosen_word) < int(3):
    chosen_word = random.choice(words)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print("You have already guessed this letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if the user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Incorrect Letters: {guess}")
        lives -= 1
        print(f"You have {lives} left")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}" )

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if the user has got all the letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

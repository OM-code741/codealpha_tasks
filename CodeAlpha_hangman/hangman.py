import random

words = ["python", "apple", "school", "computer"]
word = random.choice(words)

guessed = ""
chances = 6

print("Welcome to Hangman!")

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed += guess
        print("Correct!")
    else:
        chances -= 1
        print("Wrong! Chances left:", chances)

if chances == 0:
    print("Game Over! The word was:", word)
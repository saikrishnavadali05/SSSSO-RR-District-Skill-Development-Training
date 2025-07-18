import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai']
    word = random.choice(words)
    guessed = set()
    wrong_guesses = set()
    lives = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while lives > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed or guess in wrong_guesses:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            wrong_guesses.add(guess)
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        # Display current progress
        display_word = [letter if letter in guessed else '_' for letter in word]
        print(' '.join(display_word))

        # Check if the user has guessed all letters
        if all(letter in guessed for letter in word):
            print(f"Congratulations! You guessed the word '{word}'!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
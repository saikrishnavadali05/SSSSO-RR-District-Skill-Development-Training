
import random
words = ["apple", "banana", "cherry", "date", "elderberry"]
def scramble_word(word):
    scrambled_word = list(word)
    random.shuffle(scrambled_word)
    return "".join(scrambled_word)
def play_game():
    word = random.choice(words)
    scrambled_word = scramble_word(word)
    print(f"Unscramble the word: {scrambled_word}")
    answer = input("Enter your answer: ")
    if answer.lower() == word:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {word}.")
def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
if __name__ == "__main__":
    main()

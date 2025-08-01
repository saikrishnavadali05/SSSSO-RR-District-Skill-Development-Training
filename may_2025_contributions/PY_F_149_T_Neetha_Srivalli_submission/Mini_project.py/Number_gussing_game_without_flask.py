#Number Guessing Game without flask
import random     #random module generates random numbers

print("🎮 Welcome to the Number Guessing Game!")

def choose_difficulty():       # Function to choose difficulty level
    print("Difficulty levels:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    while True:
        choice = input("Choose your difficulty level (1,2, or 3): ")
        if choice == "1":
            return 1, 50, 10  # max 10 attempts
        elif choice == "2":
            return 1, 100, 7  # max 7 attempts
        elif choice == "3":
            return 1, 200, 5  # max 5 attempts
        else:
            print("Invalid choice. Try another number.")

def guessing_game():   #Main function to run the guessing game
    low, high, max_attempts = choose_difficulty()  #Get difficulty level

    number_to_guess = random.randint(low, high)  #Randomly select a number to guess
    attempts = 0    #Initially set attempts to 0

    print(f"\nA number is picked between {low} and {high}.")  # Inform the user about the range
    print(f"You have {max_attempts} attempts. Good luck champ!\n")

    while attempts < max_attempts:  #Loop until the user runs out of attempts
    
    #Try and except block to handle invalid inputs
        try:  
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts = attempts + 1

            if guess == number_to_guess:
                print(f"Hurray!! Correct! You guessed it in {attempts} attempt(s).")
                break
            elif abs(guess - number_to_guess) == 1:
                print("Huhh!! Very close!")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Ohh! Please enter a valid number.")

    else:
        print(f"\nHey!!You've used all {max_attempts} attempts. The number was: {number_to_guess}")
        print("Better luck next time champ!")

    print("\nThanks for playing!") #End of the game message

# Run the game
if __name__ == "__main__":
    guessing_game()


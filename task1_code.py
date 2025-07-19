import random

def hangman():
    # Predefined words
    words = ['programming', 'queue', 'python', 'algorithm', 'graphs']
    
    # Word selection from list
    word_to_guess = random.choice(words)
    guessed_letters = []
    max_guesses = 6
    guess_no = 0
    
    print("Welcome to Hangman!")
    print("Let's start HangMan!!\n")

    # Main game code
    while guess_no < max_guesses:
        
        current_state = ''.join(letter if letter in guessed_letters else '_' for letter in word_to_guess)
        print(f"Current word: {current_state}")
        
        # Check for win condition
        if '_' not in current_state:
            print("Congratulations! You've guessed the word!")
            break
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            print("Choose another letter!")
            continue
        
        # Add the guessed letter to the list
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word_to_guess:
            print("Good guess!")
        else:
            guess_no += 1
            print("OOPS!! Wrong guess!")
            print(f"You have {max_guesses - guess_no} guesses left.")
    
    # End of game
    if guess_no == max_guesses:
        print("Your guesses are over!!")
        print(f"The word was '{word_to_guess}'.")

# Run the game
if __name__ == "__main__":
    hangman()

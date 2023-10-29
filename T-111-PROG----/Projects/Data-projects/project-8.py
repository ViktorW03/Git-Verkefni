def read_file(file_name, index):
    """
    Reads file, returns word from user input index 1-12.
    """
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if 1 <= index <= len(lines):
                return lines[index - 1].strip()
            else:
                return None
    except Exception as e:
        return None

def track_guess(guess, secret_word, guessed_word):
    """
    Keeps track on guesses and prints if player inputs correct, incorrect letter
    """
    if guess in secret_word:
        if guess not in guessed_word:
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
            print(f"Correct letter {guess}!")
        else:
            print(f"Correct letter {guess}!")
    else:
        print(f"Incorrect letter {guess}!")

    return guessed_word

def hangman(read_file):
    """
    The main game using the logic from track guesses func and readfile func
    prints the outcome of the game. (win or loss)
    """
    file_name = input()
    word_in_file = int(input())
    secret_word = read_file(file_name, word_in_file)

    if not secret_word:
        print()
        return None

    guessed_word = ["-"] * len(secret_word)
    word_guessed = False

    for _ in range(12):
        print(f"Secret word: {' '.join(guessed_word)}")
        print(f"Guess {_+1}/12")
        guess = input().strip()

        guessed_word = track_guess(guess, secret_word, guessed_word)
    
        if "".join(guessed_word) == secret_word:
            word_guessed = True

        if word_guessed:
            break

    print(f"Secret word: {' '.join(guessed_word)}")
    if word_guessed:
        print("You won!")
    else:
        print(f"You lost! The secret word was {secret_word}")

def main():
    hangman(read_file)

if __name__ == "__main__":
    main()

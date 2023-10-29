
def read_file(file_name, index):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if 1 <= index <= len(lines):
            return lines[index -1].strip()
        else:
            return None



def hangman(read_file):
    file_name = input()
    word_in_file = int(input())
    secret_word = read_file(file_name, word_in_file)

    if not secret_word:
        print()
        return None

    guessed_word = ["Secret word: _"] * len(secret_word)
    incorrect_guesses = 0

    for _ in range(12):
        guess = input()
        for index, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[index] = guess
        if "".join(guessed_word) == secret_word:
            print("You won!")
        print(' '.join(guessed_word))
    else:
        incorrect_guesses += 1
        print(f"Incorrect letter {guess}!")
    return None



    # TODO: Implement a loop where the player can guess letters
    # 1. Display the current guessed word (e.g., - - - - or c - t -)
    # 2. Take the player's guess
    # 3. Update the guessed word if the guess is correct, otherwise increase incorrect guesses count
    # 4. Check for game termination conditions (either word is guessed or too many incorrect guesses)

    # TODO: Implement the endgame feedback
    # 1. Display a win message if they've guessed the word
    # 2. Display a lose message and reveal the word if they didn't guess it in time


    pass

def main():
    hangman(read_file)

if __name__ == "__main__":
    main()
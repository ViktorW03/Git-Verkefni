class Hangman:
    def __init__(self, word: str):
        self.word = word.upper()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.dashes = ["_" for x in range(len(word))]

    def guess_letter(self, letter: str) -> bool:
        if letter.upper() not in self.guessed_letters:
            if letter.upper() not in self.word:
                
                self.incorrect_guesses += 1
            self.guessed_letters.append(letter.upper())
        if letter.upper() in self.word:
            for x, char in enumerate(self.word):
                if letter.upper() == char:
                    self.dashes[x] = letter.upper()

        return letter.upper() in self.word
    
    
    def __str__(self) -> str:
        the_dashes = " ".join(self.dashes)
        incorr_guess = f"Number of incorrect guesses: {self.incorrect_guesses}"
        return the_dashes + "\n" + incorr_guess
"""      
hangword = Hangman("Testing")
print(hangword)
print(hangword.guess_letter("i"))
print(hangword.guess_letter("I"))
print(hangword.guess_letter("a"))
hangword.guess_letter("t")
print(hangword)
hangword.guess_letter("E")
hangword.guess_letter("s")
print(hangword)
hangword.guess_letter("i")
hangword.guess_letter("N")
hangword.guess_letter("g")
print(hangword)



Example usage:
hangword = Hangman("Testing")
print(hangword)
print(hangword.guess_letter("i"))
print(hangword.guess_letter("I"))
print(hangword.guess_letter("a"))
hangword.guess_letter("t")
print(hangword)
hangword.guess_letter("E")
hangword.guess_letter("s")
print(hangword)
hangword.guess_letter("i")
hangword.guess_letter("N")
hangword.guess_letter("g")
print(hangword)
Expected output:
_ _ _ _ _ _ _
Number of incorrect guesses: 0
True
True
False
T _ _ T I _ _
Number of incorrect guesses: 1
T E S T I _ _
Number of incorrect guesses: 1
T E S T I N G
Number of incorrect guesses: 1
"""




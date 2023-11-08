def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""
    word = input()
    meaning = input()
    dictionary[word] = meaning
   

def more() -> bool:
    """Checks if the user wants to add more words."""
    answer = input().lower()
    if answer == "y":
        return True
    else:
        return False

    


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""
    for key, value in sorted(dictionary.items()):
        print()
        print(f"{key}:\n    {value}")


    

 
if __name__ == "__main__":
    main()

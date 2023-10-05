def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)


def get_file():
    """Gets file name from user and returns the open file handle.

    Asks the user repeatedly for file name
    until an existing file name is given.
    """
      
    filename = input()
    file = open_file(filename)
    while file is None:
        print(f"{filename} not found! Please try again.")
        filename = input()
        file = open_file(filename)
    return file

  
    # and implement this function.
    # You can call the following function in your implementation.


def open_file(filename: str):
    try:
        return open(filename)
    except FileNotFoundError:
        return 


def get_numbers_from_file(file) -> list:
    """Returns a list of all numbers in the given file.

    Assumes all numbers appear on their own,
    separated from other text by whitespace.
    """
    numbers = []
    for line in file.read().splitlines():
        for word in line.split():
            if word.isdigit():
                numbers.append(int(word))
    return numbers




def display_numbers(numbers):
    print(sorted(numbers))



if __name__ == "__main__":
    main()

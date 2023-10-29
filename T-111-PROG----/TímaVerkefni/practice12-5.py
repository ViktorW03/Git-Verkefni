def main():
    input_list = get_correct_data()
    
    sorted_list = sorted(input_list)



def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""
    data = get_data()
    while data is None:
        print( print("Incorrect input! Please try again."))
        data = get_data()
    return data
        
    


def get_data():
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """
    data_str = input().split(',')
    data_int = []  # This list will store valid integers


    for string in data_str:
        try:
            num = int(string)
            if num <= 0:
                return None
            data_int.append(num)
        except ValueError:
            return None

    return data_int



# Add as many functions as you think you could use.


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
def main():
    input_list = get_correct_data()
    
    sorted_list = sorted(input_list)
    
    composite_list = sorted(set([num for num in input_list if not is_prime(num)]))
    
    min_val = min(input_list)
    max_val = max(input_list)
    avg_val = sum(input_list) / len(input_list)
    
    print("Input list:", input_list)
    print("Sorted list:", sorted_list)
    print("Composite list:", composite_list)
    print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")

def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""
    while True:
        data = get_data()
        if data is not None:
            return data
        print("Incorrect input! Please try again.")

def get_data():
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """
    data_str = input().split(',')
    try:
        data_int = [int(num) for num in data_str]
        if all(num > 0 for num in data_int):
            return data_int
    except ValueError:
        pass
    return None

# Add as many functions as you think you could use.

def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Improved is_prime function
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()


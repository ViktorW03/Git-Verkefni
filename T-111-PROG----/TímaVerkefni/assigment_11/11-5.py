from typing import List

# Function that returns the sum of all prime numbers in the given list.
def prime_sum(the_given_list_of_numbers: List[int]) -> int:
    """Returns the sum of all prime numbers from the list."""
    # Use list comprehension to filter prime numbers and then sum them up.
    return sum([num for num in the_given_list_of_numbers if is_prime(num)])

# Function that checks if a number is prime.
def is_prime(number_to_check: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""
    if number_to_check < 2:
        return False

    potential_factor = 2
    while potential_factor**2 <= number_to_check:
        if number_to_check % potential_factor == 0:
            return False
        potential_factor += 1

    return True



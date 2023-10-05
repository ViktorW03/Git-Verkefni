from typing import List

def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""
    even = []
    for digit in int_list:
        if digit % 2 == 0:  # Corrected the condition
            even.append(digit)  # Corrected the append operation
    return even

def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""
    int_list[:] = extract_evens(int_list)  # Corrected the assignment

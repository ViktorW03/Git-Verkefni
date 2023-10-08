from copy import deepcopy

def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""
    a_list[:] = without_outliers(a_list)

def without_outliers(a_list: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""
    a_list = deepcopy(a_list)  # Create a copy so the original list isn't modified
    min_index, max_index = find_min_and_max_index(a_list)
    
    # Remove the element with the larger index first
    if min_index > max_index:
        a_list.pop(min_index)
        a_list.pop(max_index)
    else:
        a_list.pop(max_index)
        a_list.pop(min_index)
    
    return a_list

def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""
    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i
        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index


import itertools

values = {
    'a': 10, 'b': 6, 'c': 1, 'd': 12, 'e': 10, 'f': 9, 'g': 3, 'h': 4,
    'i': 7, 'j': 14, 'k': 5, 'l': 11, 'm': 8, 'n': 15, 'o': 13, 'p': 2,
    'q': 10, 'r': 6, 's': 1, 't': 12, 'u': 10, 'v': 9, 'w': 3, 'x': 4,
    'y': 7, 'z': 14, '!': 10, '"': 6, '#': 1, '$': 12, '%': 10, '(': 4,
    ')': 7, ' ': 3, '*': 14, '+': 5, '-': 8, '.': 15, '/': 13, ':': 14,
    ';': 5, '<': 11, ',': 8, '>': 15, '?': 13, '@': 2
}

def find_combination(target_sum, length, start=0, combo=[]):
    if length == 0:
        if sum(values[char] for char in combo) == target_sum:
            return combo
        return None

    result = None
    for i in range(start, len(values)):
        char = list(values.keys())[i]
        new_combo = combo + [char]
        result = find_combination(target_sum, length - 1, i, new_combo)
        if result:
            return result

    return result

target_sum = 53 # Set the target sum to 48
combo_length = 6  # Set the length of the combination to 6
result = find_combination(target_sum, combo_length)

if result:
    print("Combination that sums to", target_sum, ":")
    print(result)
else:
    print("No combination found for the target sum.")
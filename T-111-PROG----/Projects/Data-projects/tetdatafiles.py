def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    if -20 <= number <= 20:
                        numbers.append(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return numbers

def cumulative_sum(numbers):
    result = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        result.append(round(current_sum, 4))
    return result

def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length == 0:
        return None
    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

def main():
    filename = input().strip()
    numbers = read_numbers_from_file(filename)

    if not numbers:
        return

    # 1. Display numbers
    print(" ".join(map(str, [round(num, 4) for num in numbers])))

    # 2. Display cumulative sum
    print(" ".join(map(str, cumulative_sum(numbers))))

    # 3. Display sorted numbers
    print(" ".join(map(str, sorted([round(num, 4) for num in numbers]))))

    # 4. Display median
    print(round(median(numbers), 4))

if __name__ == "__main__":
    main()

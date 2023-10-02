filename = input()
"""
skilar floating point tölum.
Ég ákvað að reikna float inni í read fallinu til að fækka línur
"""
def numbers_in_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:#notum 'r' til að gefa read leyfi
            lines = file.readlines()
            for line in lines:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return numbers
#skilar uppsafnaðri summu talnanna í rununni
def cumulative_sum(numbers):
    sum_of_numbers = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        sum_of_numbers.append(current_sum)
    return sum_of_numbers
#skilar raðaðri útgáfu (í hækkandi röð) af tölunum í rununni
def sorted_numbers(numbers):
    return sorted(numbers)
#skilar miðgildi rununnar
def calculated_median(numbers):
    sorted_for_median = sorted_numbers(numbers)
    length = len(sorted_for_median)
    if length % 2 == 1:
        return sorted_for_median[length // 2]
    else:
        return (sorted_for_median[(length - 1) // 2] + sorted_for_median[length // 2]) / 2

numbers = numbers_in_file(filename)
#main fall sem prenntar út útkomu úr textaskrá sem er slegin inn
def main():
    if not numbers:
        return []
    print(" ".join(map(str, [round(num, 4) for num in numbers])))
    print(" ".join(map(str, [round(num, 4) for num in cumulative_sum(numbers)])))
    print(" ".join(map(str, [round(num, 4) for num in sorted_numbers(numbers)])))
    print(round(calculated_median(numbers), 4))

if __name__ == "__main__":
    main()

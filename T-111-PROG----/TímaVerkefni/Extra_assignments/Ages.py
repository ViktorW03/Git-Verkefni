def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError as e:
            print(f"{e.args[0].split(': ')[1]} is not an integer. Please try again.")

def main():
    n = get_integer_input("")
    names = []
    ages = []

    for _ in range(n):
        name = input()
        age = get_integer_input("")
        names.append(name)
        ages.append(age)

    oldest_index = ages.index(max(ages))
    youngest_index = ages.index(min(ages))

    sorted_ages = sorted(ages)
    if n% 2 == 0:
        median = (sorted_ages[n //2 - 1] + sorted_ages[n // 2]) / 2
    else:
        median = sorted_ages[n // 2]

    average = sum(ages) / n

    print(f"The oldest person is {names[oldest_index]} who is {ages[oldest_index]} years old")
    print(f"The oldest person is {names[youngest_index]} who is {ages[youngest_index]} years old")
    print(f"The median age is {median:.2f}")
    print(f"The average age is {average:.2f}")

if __name__ == "__main__":
    main()
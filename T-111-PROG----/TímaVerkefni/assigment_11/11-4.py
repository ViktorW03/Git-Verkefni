sequence = input().split()

numbers = [float(x) for x in sequence]

if len(numbers) < 3:
    print("At least 3 scores needed!")
else:
    numbers.sort()
    numbers = numbers[3:]
    total_sum = sum(numbers)
    
    formatted_total_sum = f"{total_sum:.1f}" if total_sum != 0 else "0"
    
    print(f"Sum of scores (3 lowest removed): {formatted_total_sum}")

# Your function definitions goes here
def sum_of_divisors(number):
    s = 0

    for i in range(1, number):
        if number % i ==0:
            s += i
    return s
    

def decide(number):
    sum = sum_of_divisors(number)
    if sum == number:
        return f"{number} is a perfect number."
    elif sum > number:
        return f"{number} is abundant."
    elif sum < number:
        return f"{number} is deficient."
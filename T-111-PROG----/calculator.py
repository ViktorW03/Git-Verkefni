import math

def get_choice():
    # Get the operation choice from the user.
    operation = input("Enter operation (add, sub, mul): ")
    return operation

def get_numbers():
    numbers = []
    print("Enter numbers one by one and press '=' when done:")
    while True:
        num = input("Enter a number: ")
        if num == "=":
            break
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number or '=' to finish.")
    return numbers
        
def add(calculator_list):
    # Perform addition.
    return sum(calculator_list)

def sub(calculator_list):
    # Perform subtraction.
    if not calculator_list:
        return 0
    result = calculator_list[0]
    for number in calculator_list[1:]:
        result -= number
    return result

def mul(calculator_list):
    # Perform multiplication.
    return math.prod(calculator_list)

def calculate(operation, calculator_list):
    # Perform the appropriate operation.
    if operation == "add":
        return add(calculator_list)
    elif operation == "sub":
        return sub(calculator_list)
    elif operation == "mul":
        return mul(calculator_list)
    else:
        return "Invalid operation"

# Main program
operation = get_choice()
calculator_list = get_numbers()
result = calculate(operation, calculator_list)
print(f"The result is: {result}")

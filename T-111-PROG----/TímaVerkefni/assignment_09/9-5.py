def main():
    name = get_name()
    age = get_age()
    print(f"Nice to meet you {name}. Congratulations on your {age} years.")


def get_name() -> str:
    try:
        name = input("What's your name? ")

        if name.isnumeric():
            raise ValueError("Please enter a valid name. ")
    
    except ValueError as error:
        return error
    
    else:
        return name


def get_age() -> str:

    is_valid = False

    while not is_valid:
        try:
            age = int(input("How old are you? "))

        except ValueError:
            print("Please enter an integer.")
            continue

        if 0 < age < 126:
            is_valid = True
        else:
            print(f"You seriously expect me to believe you are {age} years old?")

    else:
        return age

def check_if_valid(age:str) -> bool:
    """checs if a string is a valid age"""
    try:
        age = int(age)
    except ValueError:
        return False
    
    if  32 < age < 126:
        return True
    print(f"You seriously expect me to believe you are {age} years old?")
    return False
    




if __name__ == "__main__":
    main()

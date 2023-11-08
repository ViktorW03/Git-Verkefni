def main():
    num1_str = (input())
    num2_str = (input())

    result = divide_safe(num1_str, num2_str)
    print(result)


def divide_safe(num1_str, num2_str):
    try:
        division = float(num1_str) / float(num2_str)
        return round(division,5)
    except ValueError:
        return  
    except ZeroDivisionError:
        return
        



    





    """Returns num1/num2 if the input is valid, else None."""

    raise NotImplementedError  # TODO: Remove this line and implement the function.


if __name__ == "__main__":
    main()

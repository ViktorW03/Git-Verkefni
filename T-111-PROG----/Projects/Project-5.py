#fall til að safna tölum úr streng og skila þeim
def collect_digits(a_str):
    result = ""
    for c in range(len(a_str)):
        if a_str[c].isdigit():
            result += a_str[c]
    return result
#fall fyrir "swapcase" kóðan sem inniheldur ekki swapcase func
def inverse_case(a_str):
    result = ""
    for i in range(len(a_str)):
        if a_str[i].islower():
            result += a_str[i].upper()
        elif a_str[i].isupper():
            result += a_str[i].lower()
        else:
            result += a_str[i]
    return result
#breytum decimal tölum í hexidecimal tölu.
def to_hex(an_int):
    hex_chars = "0123456789ABCDEF"
    hex_value = ""

    if an_int == 0:
        return "0"

    while an_int > 0:
        remainder = an_int % 16
        hex_value = hex_chars[remainder] + hex_value
        an_int = an_int // 16

    return hex_value
#þegar input er q hættir forritið að keyra
while True:
    command = input()
    if command == "q":
        break
    a_str = input()
#köllum í eftirfarandi föll
#notum stafin "c" til ap kalla í fallið (taka tölur úr streng og skila)
# "i" til að kalla í ("swapcase")
# "h" til að kalla í (decimal í hexidecimal)
    if command == "c":
        print(collect_digits(a_str))
    elif command == "i":
        print(inverse_case(a_str))
    elif command == "h":
        an_int = int(a_str)
        print(to_hex(an_int))


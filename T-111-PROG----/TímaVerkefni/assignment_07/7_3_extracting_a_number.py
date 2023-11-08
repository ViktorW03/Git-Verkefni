# extract_first_number_from_string definition goes here

def extract_first_number_from_string(string_to_search):
    digitfound = False
    digit_string = str()
    for char in string_to_search:
        if char.isdigit():
            digit_string += char
            digitfound = True
        if not char.isdigit() and digitfound:
            break
    
    if digitfound:
        return int(digit_string)
    else: return -1




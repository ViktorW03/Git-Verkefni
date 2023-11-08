# Main program starts here


# Write your functions here
#ask for input != q
def get_home_addresses():
    adresses = []
    adress_input = input()
    while adress_input != "q":
        adresses.append(adress_input)
        adress_input = input()
    return adresses

def split_addresses(home_addresses):
    list_of_tuples = []
    for address in home_addresses:
        street, number = address.split()
        list_of_tuples.append((street, number))
    return list_of_tuples



    """
    This function takes a list of home addresses and returns 
    a list of tuples containing the street name and number.
    """
    pass

# Main program starts here
def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = split_addresses(home_addresses)
    print(street_and_number)

if __name__ == "__main__":
    main()
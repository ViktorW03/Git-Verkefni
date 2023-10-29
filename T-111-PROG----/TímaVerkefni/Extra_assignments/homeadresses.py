# Main program starts here
def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


def get_home_addresses():

    adresses = []
    adress_input = input()
    while adress_input != "q":
        adresses.append(adress_input)
        adress_input = input()
    return adresses
    

def get_tuple_from_home_addresses(home_addresses):
    list_of_tuples = []
    for adress in home_addresses:
        house, number = adress.split()
        list_of_tuples.append(street, number)



    pass


if __name__ == "__main__":
    main()

def main():
    while True:
        filename = input()
        countrie_dict = read_file(filename)

        if coutries_list is not None:
            break

        countries_dict = find_length(countries_list)
        print(countries_dict)
def read_file(filename):
    countries = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                countries.append(line.strip())
        return countries
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    
def find_length(countries):
    length_to_countries = {}

    for country in countries:
        country_length = len(country)
        if country_length in length_to_countries:
            length_to_countries[country_length].append(country)
        else:
            length_to_countries[country_length] = [country]
    return length_to_countries
    

if __name__ == "__main__":
    main()


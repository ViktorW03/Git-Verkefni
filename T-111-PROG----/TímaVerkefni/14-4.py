def main():
    while True:
        filename = input()
        countries_list = read_file(filename)

        if countries_list is not None:
            break
  
    countries_dict = find_length(countries_list)
    use_key(countries_dict)

def read_file(filename):
    countries = []
    try:    
        with open(filename, 'r') as file:
            for line in file:
                countries.append(line.strip())
        return countries
    except FileNotFoundError:
        print("File ", filename, "not found!")
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
    

def use_key(countries_dict):
    while True:
        try:
            key = int(input())
            if key in countries_dict:
                print(', '.join(countries_dict[key]))
            else:
                print(f"no country name of length {key} exists.")
    
            answer = input().lower()
            if answer != "y":
                break
        except ValueError:
            print()

if __name__ == "__main__":
    main()
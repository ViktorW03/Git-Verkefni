def main():
    filename = input()
    replacethis = read_file(filename)
    print(replacethis)

def read_file(filename):
    replacelist = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                replacelist.append(line.strip())
        return replacelist
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    
def read_file(filename):
    try:
        with open (filename) as file:
            return list(map(str.strip, file))
    except FileNotFoundError:
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
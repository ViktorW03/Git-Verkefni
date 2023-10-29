import csv

def read_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)
        
        # Debug print statement
        for row in rows:
            print(f"DEBUG READ FILE: {row}")
        
        return rows


def header():
    print("Players by country:")
    print("-------------------")

def find_country(rows):
    chess_dict = {}
    for row in rows:
        country = row[2].strip()
        if country in chess_dict:
            chess_dict[country].append(row)
        else:
            chess_dict[country] = [row]
        
        # Debug print statement
        if "Carlsen" in row[1]:
            print(f"DEBUG FIND COUNTRY: Magnus Carlsen added to {country}. Current data: {chess_dict[country]}")
    
    return chess_dict


def display_by_country(chess_dict):
    for country, players in sorted(chess_dict.items()):
        num_players = len(players)
        avg_rating_val = sum([int(player[3]) for player in players]) / num_players
        print(f"{country} ({num_players}) ({avg_rating_val:.1f}):")
        
        sorted_players = sorted(players, key=lambda x: int(x[3]), reverse=True)
        
        for player in sorted_players:
            name_parts = player[1].strip().split(",")
            if len(name_parts) > 1:
                full_name = name_parts[1].strip() + " " + name_parts[0].strip()
            else:
                full_name = name_parts[0].strip()
            rating = player[3].strip()
            print(f"{full_name:>40} {rating:>10}")
        print()

def main():
    filename = input("Enter filename: ")
    data = read_file(filename)
    header()
    countries = find_country(data[1:])
    display_by_country(countries)

if __name__ == '__main__':
    main()


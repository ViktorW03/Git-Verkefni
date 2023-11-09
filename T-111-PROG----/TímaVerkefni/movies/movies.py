MENU_LETTERS = "123"
MENU = f"""
*******************************
{MENU_LETTERS[0]}. Movies in alphabetical order
{MENU_LETTERS[1]}. Titles in given year
{MENU_LETTERS[2]}. Modify all ratings
*******************************
"""

def get_lines_from_file(filename: str):
    try:
        with open(filename) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return []

def print_title_for_given_year(movies: dict, given_year: int):
    for title, ry in movies.items():
        rating, year = ry
        if year == given_year:
            print(title)


def get_menu_selection(movies):
    print(MENU)
    return input("Enter your selection:\n")

def print_alphabetical(movies: dict):
    for title, (rating, year) in sorted(movies.items()):
        print(f"{title:<50}{rating:>6.2f}{year:>6}")

def modify_ratings(movies: dict, modifier: int):
    for title, (rating, year) in movies.items():
        movies[title] = (rating + modifier, year)

def get_movies_dict(lines):
    movies = dict()

    for line in lines:
        title, rating, year = line.split(";")
        movies[title] = (float(rating), int(year))
    
    return movies
    
def main():
    filename = input("Enter filename:\n")
    lines = get_lines_from_file(filename)

    if not lines: return

    movies = get_movies_dict(lines)

    while (selection := get_menu_selection(movies)) in MENU_LETTERS:
        if selection == MENU_LETTERS[0]:
            print_alphabetical(movies)
        elif selection == MENU_LETTERS[1]:
            year = int(input("Enter year:\n"))
            print_title_for_given_year(movies, year)
        elif selection == MENU_LETTERS[2]:
            modifier = float(input("Enter modifier for ratings:\n"))
            modify_ratings(movies, modifier)

if __name__ == "__main__":
    main()

"""filename = input()
lines = get_lines_from_file(filename)"""
    
#movies-top-20.csv

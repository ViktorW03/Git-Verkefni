filename = input()

def open_file(filename: str):
    try:
        return open(filename)
    except FileNotFoundError:
        return 
    
def read_lines_from_file(filename):
        with open(filename, 'r') as file:
            for line in read_lines_from_file:
                return line




def main():
    filename = input().strip()
    numbers = read_numbers_from_file(filename)

        
    if __name__ == "__main__":
        main()
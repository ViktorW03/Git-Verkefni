def reverse_word_in_place(line):
    words = line.strip().split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def read_file(file_name):
    with open(file_name, "r") as file_object:
        for line in file_object:
            reversed_line = reverse_word_in_place(line.strip()) 
            print(reversed_line)

def main():
    file_name = input()
    read_file(file_name)

if __name__ == "__main__":
    main()

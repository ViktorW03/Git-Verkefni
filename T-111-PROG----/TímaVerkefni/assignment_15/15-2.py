import string
UI = False

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            words = [word.strip(string.punctuation) for line in f for word in line.split()]
            return set(words)
    except FileNotFoundError:
        return None
    
def set_intersection(set1:set, set2:set):
    return set1.intersection(set2)

def get_symmetric_difference(set1:set, set2:set):
    return set1.symmetric_difference(set2)


def set_difference(set1:set, set2:set):
    return set1.difference(set2)

def format_words(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    return ", ".join(words[:-1]) + " and " + words[-1] + "."

def main():
    filename1 = input("Enter the name of the first file:\n" if UI else "")
    filename2 = input("Enter the name of the second file:\n" if UI else "")
    set1 = read_file(filename1)
    set2 = read_file(filename2)

    common_words = set_intersection(set1, set2)
    print(f"The two files have {len(common_words)} words in common.")
    print("These words are as follows:")
    print(format_words(sorted(common_words)))
    print()
    the_symmetric_difference = get_symmetric_difference(set1, set2)
    print(f"There are {len(the_symmetric_difference)} words that are only in either file but not both.")
    print("These words are as follows:")
    print(format_words(sorted(the_symmetric_difference)))
    print()
    difference_1_2 = set_difference(set1, set2)
    print(f"There are {len(difference_1_2)} words that only appear in the first file.")
    print("These words are as follows:")
    print(format_words(sorted(difference_1_2)))
    print()

if __name__ == "__main__":
    main()


#pangram_
""""
def explode():
    print("BOOM!")

0 1 3 

eax = 1

rsp = 0
rbx = 2
while rbx != 6:
    eax = rsp + rbx*4 - 4
    rsp + rbx*4
    if eax == (rsp + rbx*4):
        rbx += 1
    else:
        explode()
"""
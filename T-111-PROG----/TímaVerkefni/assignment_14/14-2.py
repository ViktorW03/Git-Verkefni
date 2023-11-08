import string
def main():
    sentence_1 = input()
    sentence_2 = input()

    if are_anagrams(sentence_1, sentence_2):
        print(f"{sentence_1} is an anagram of {sentence_2}.")
    else:
        print(f"{sentence_1} is not an anagram of {sentence_2}.")


def are_anagrams(sentence_1: str, sentence_2: str) -> bool:
    a_sent_dict = string_to_dict(sentence_1)
    b_sent_dict = string_to_dict(sentence_2)

    if set(a_sent_dict.keys()) != set(b_sent_dict.keys()):
        return False
    for key in a_sent_dict: 
        if a_sent_dict[key] != b_sent_dict[key]:
            return False

    return True


def string_to_dict(sentence: str) -> dict:
    dictionary = {}
    for character in sentence:
        char = character.lower()
        if char not in string.punctuation and char != " ":
            dictionary[char] = dictionary.get(char, 0) + 1
    return dictionary



if __name__ == "__main__":
    main()

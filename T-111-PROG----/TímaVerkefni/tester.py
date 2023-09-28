#!/usr/bin/env python3

def main():
    n = int(input())
    m = list(map(int, input().split()))  # Read the input numbers and convert them to integers directly

    # Your list is already sorted based on the problem constraints
    # Hence, we don't need to sort them again

    first_third_length = n // 3

    first_third = m[:first_third_length]          # The first one-third of the list
    second_third = m[first_third_length:2*first_third_length]  # The second one-third of the list
    third_third = m[2*first_third_length:]       # The last one-third of the list

    new_list = second_third + first_third + third_third  # Concatenate the lists as per the starwars order

    print(' '.join(map(str, new_list)))  # Convert the numbers to strings and print them with spaces in between

if __name__ == "__main__":
    main()

a_str = str(input())
char_to_count = input()

# Complete the program below
for i, char in enumerate(a_str):
    if char == char_to_count:
        print(i)

#for i in range(len(a_str)):
    #if a_str[i] == char_to_count:
     #   print(i)
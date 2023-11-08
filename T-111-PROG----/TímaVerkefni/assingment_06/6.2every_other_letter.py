a_str = input()  # Do not change this line
result = ''
# Complete the program below
for i, char in enumerate(a_str):
    if i  % 2 != 1:
        result += char

print(result)
n = int(input())  # Do not change this line
first = 1
second = 2 
third = 3
for i in range (n):
    print (first)
    sum = first + second + third
    first = second
    second = third
    third = sum



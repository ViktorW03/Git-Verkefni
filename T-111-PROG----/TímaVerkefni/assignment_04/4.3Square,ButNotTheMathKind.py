size = int(input())
# Write your solution here below
for i in range (size):
    for j in range (size):
        if j == size -1:
            print ("*")
        elif i == 0 or j == 0 or i == size -1:
            print ("*", end=" ")
        else:
            print (" ", end = " ")
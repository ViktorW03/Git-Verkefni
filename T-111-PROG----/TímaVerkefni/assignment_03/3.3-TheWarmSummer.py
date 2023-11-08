# Here's something to get you going
# (you might need to add indentation or move it around):
answer = input("You need something doubled? (Y)es? ")
while answer == "Y":
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    print(number * 2)
    answer = input("You need something else doubled? (Y)es? ")

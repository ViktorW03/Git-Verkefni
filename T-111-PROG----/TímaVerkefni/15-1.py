try:
    number_chores = int(input())
except ValueError:
    print()

chores = []
for item in range(number_chores):
    chore = input()
    if chore not in chores:
        chores.append(chore)
        print(chore)



# Do not change the following 4 lines:
budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())



project_cost = project1 + project2 + project3

if budget >= project_cost:

    print("Budget is sufficient.")
else:
    print("Budget is insufficient.")


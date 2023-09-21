mb_per_month = int(input())
n = int(input()) #fjöldi mánuða að nota planið
sum = 0

for i in range (n):
    d = int(input())
    sum += (mb_per_month-d)

print (sum+mb_per_month)

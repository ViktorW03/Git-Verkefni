num1 = int(input()) # Do not change this line
num2 = int(input()) # Do not change this line
num3 = int(input()) # Do not change this line



# if num1 > num2 or num1< num2 or num1>num3 or num1<num3 or num2 > num3 or num2 < num3:

if num1 >= num2 and num1>= num3:
    max_int = num1
elif num2>= num3 and num2>=num1:
    max_int = num2
else: 
    max_int = num3




print(max_int) # Do not change this line

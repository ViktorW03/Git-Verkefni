number = int(input()) # Do not change this line
# Fill in the missing code below
no_7_found_yet = True
while number > 0:
    if number % 10 == 7:
        no_7_found_yet = False
    number = number // 10
if no_7_found_yet: # Hint: does this variable name suggest anything?
    print("The number does not contain 7.")
else:
    print("The number contains 7.")

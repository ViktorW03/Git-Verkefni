
lower_case = False
upper_case = False
numeric = False

password_true = False
password_tries = -1

q_quit = False
valid_count = 0
invalid_count = 0

while True:

    password = str(input())
    password_tries += 1


    if password == "q":
        q_quit = True
        print(f"You tried {password_tries} passwords, {valid_count} valid, {invalid_count} invalid.")
        break

    password_true = False

    if 6 <= len(password) <= 20:

        lower_case = False
        upper_case = False
        numeric = False
        
        has_lowercase = any(char.islower() for char in password)
        if not has_lowercase:
            print(f"{password}: Missing lower case letter.")
        else:
            lower_case = True

        has_uppercase = any(char.isupper() for char in password) 
        if not has_uppercase:
            print(f"{password}: Missing upper case letter.")
        else:
            upper_case = True

        has_numeric = any(char.isnumeric() for char in password)
        if not has_numeric:
            print(f"{password}: Missing numeric letter.")
        else:
            numeric = True

        
        if lower_case and upper_case and numeric:
            password_true = True

        if not password_true:
            invalid_count += 1
            
        if password_true == True:
            valid_count += 1
            password_count = len(password)
            print(f"{password}: Valid password of length {password_count}.")
            
    

    else: 
        invalid_count += 1
        print(f"{password}: Invalid length.")


    




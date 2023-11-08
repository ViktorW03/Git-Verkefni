name = input()
lastname, firstname = name.split(', ')

fitst_initial = firstname[0].upper()
formatted_lastname = lastname.capitalize()

print(f"{fitst_initial}. {formatted_lastname}")
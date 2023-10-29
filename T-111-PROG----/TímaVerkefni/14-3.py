
def main():
    email_to_grade = emails_grades()
    email_to_avg_grade = calculations(email_to_grade)
    display_grade_average(email_to_avg_grade)

def display_grade_average(email_to_avg_grade):
     for email in sorted(email_to_avg_grade.keys()):
        avg_grade = email_to_avg_grade[email]
        if avg_grade == int(avg_grade):
            print(f"{email}: {avg_grade:.0f}")
        else:
            print(f"{email}: {avg_grade:.2f}")

def calculations(email_to_grade):
    email_to_avg_grade = {}
    for email, grades in email_to_grade.items():
        avg_grades = sum(grades) / len(grades)
        email_to_avg_grade[email] = avg_grades
    return email_to_avg_grade 

def emails_grades():
    email_to_grade = {}
    while True:
        email = input().strip()
        grade = float(input().strip())
        
        email_to_grade[email] = email_to_grade.get(email, []) + [grade]

        answer = input().strip().lower()
        if answer == 'n':
            break
    
    return email_to_grade

if __name__ == "__main__":
    main()

# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1B - Spurning 3

number_of_students:int = int(input("Hvað eru margir nemendur í hópnum: "))
students:list = []

def printGrades():
  for student in students:
    print(f'{student[0]}\t{student[1]}')

def updateGrade(student, grade):
  for i in range(len(students)):
    if students[i][0] == student:
      students[i] = (student, grade)
      break # we don't need to loop tru other students anymore


for i in range(number_of_students):
  grade:float = float(input(f"Skráið einkunn namenda nr: {i+1} Einkunn: "))
  students.append((i+1, grade))

printGrades()

while True:
  should_change: str = input("Viltu lagfæra einkunnir (J ef já, annars e-ð annað): ").lower()
  if should_change != 'j':
    break

  student_number:int = int(input("Nr. nemanda sem á að laga: "))
  new_grade: float = float(input("Einkunn: "))
  updateGrade(student_number, new_grade)

  printGrades()

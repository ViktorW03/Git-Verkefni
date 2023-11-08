# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1B - Spurning 4

meetings: list = []

def printOptions() -> None:
  options: list = [
    (1, 'Register meeting'),
    (2, 'Print all meetings'),
    (3, 'Save meetings to a file'),
    (4, 'Read from a file'),
    (9, 'Exit'),
  ]
  print("Choose an option:")
  for option in options:
    print(f'  {option[0]}. {option[1]}')

def registerMeeting() -> None:
  females:str = input("Number of females: ")
  males:str = input("Number of males: ")
  other:str = input("Number of other: ")
  meetings.append({'female': females, 'male': males, 'other': other})

def printAllMeetings() -> None:
  print('Mæting í kennslustund:')
  print ("{:<8} {:<8} {:<8}".format('Female','Male','Other'))
  for meeting in meetings:
    male:str = meeting["male"]
    female:str = meeting["female"]
    other:str = meeting["other"]
    print ("{:<8} {:<8} {:<8}".format(female, male, other))


while True:
  printOptions()
  option:int = int(input("Option: "))

  # Exit
  if option == 9:
    break

  # Register meeting
  if option == 1:
    registerMeeting()
    while True:
      should_continue:str = input("Register another meeting (j/n): ").lower()
      if should_continue != 'j':
        break
      registerMeeting()

  # Print all meetings
  if option == 2:
    printAllMeetings()

  # Save meetings to a file
  if option == 3:
    filename:str = input("Filename to save to: ")
    with open(filename, 'w') as file:
      file.write(str(meetings))

  # Read from a file
  if option == 4:
    filename:str =input("Filename to read from: ")
    with open(filename, 'r') as file:
      meetings = eval(file.read())

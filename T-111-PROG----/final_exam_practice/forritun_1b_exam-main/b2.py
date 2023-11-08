# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1B - Spurning 2

def retturReytur(field) -> bool:
  columns:list = ['A','B','C','D','E','F','H']
  rows:list = [1,2,3,4,5,6,7,8]

  if len(field) != 2:
    return False

  col:str = field[0]
  row:str = field[1]

  if col in columns and int(row) in rows:
    return True
  return False

def test():
  tests:list = ['a1', 'A9', 'I3', 'A12', 'A', '5A', 'A1', 'H8', '']
  answers:list = [0, 0, 0, 0, 0, 0, 1, 1, 0]
  failed_tests:int = 0
  for test in tests:
    if retturReytur(test) != answers[tests.index(test)]:
      print(f'Test case: {test} failed')
      failed_tests += 1

  if failed_tests == 0:
    print('All test cases passed successfuly!')

def printMenu():
  print('Chose an opton:')
  print('1. Run test cases')
  print('2. Test and input manually')


printMenu()
option:int = int(input())

if(option == 1):
  test()
  exit

if(option == 2):
  field:str = input("Enter a field number: ")
  if retturReytur(field):
    print('Correct field')
  else:
    print('Incorrect field')

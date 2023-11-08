# Assignment for Forritun 1B exam

## Verkefni: Forritun 1B - Spurning 1
**Description:**  
Create a program to convert temperatures from Fahrenheit to Celsius. The conversion formula is \(C = \frac{5}{9} \times (F - 32)\). The program should take a user input for the temperature in Fahrenheit, convert it to Celsius, and print the result.

**Input:**  
- A floating-point number representing the temperature in Fahrenheit.

**Output:**  
- A string displaying the converted temperature in Celsius with 2 decimal places.

**Output Test Cases:**
- Input: 32
  Output: "Það eru : 0.00 gráður á Celsius"
- Input: 212
  Output: "Það eru : 100.00 gráður á Celsius"
- Input: 98.6
  Output: "Það eru : 37.00 gráður á Celsius"

---

## Verkefni: Forritun 1B - Spurning 2
**Description:**  
Create a program to validate chessboard field identifiers. A valid field identifier consists of a letter (A-H) representing the column and a number (1-8) representing the row. The program should provide a menu for the user to choose between running predefined test cases or inputting a field identifier manually. If the input is manually entered, the program should print whether it is a correct field or not.

**Input:**  
- An integer for choosing an option from the menu.
- A string representing a chessboard field identifier (if option 2 is chosen).

**Output:**  
- A string indicating whether the field identifier is correct or not (if option 2 is chosen).
- The results of the test cases (if option 1 is chosen).

**Output Test Cases:**
- Chosen option: 1
  Output: 
  ```
  Test case: a1 failed
  Test case: A9 failed
  Test case: I3 failed
  Test case: A12 failed
  Test case: A failed
  Test case: 5A failed
  Test case: A1 passed
  Test case: H8 passed
  Test case:  failed
  ```

- Chosen option: 2, Field: A1
  Output: "Correct field"

- Chosen option: 2, Field: Z9
  Output: "Incorrect field"

---

## Verkefni: Forritun 1B - Spurning 3
**Description:**  
Create a program to manage student grades. The program should ask for the number of students in the group and then their grades. After entering the grades, it should display the list of student grades. Then, the program should allow the user to modify any student's grade. If the user wants to modify a grade, they should input the student's number and the new grade. The program should update the grade and display the updated list. The user should be able to make multiple modifications.

**Input:**  
- An integer representing the number of students in the group.
- A floating-point number for each student's grade.
- A string indicating whether the user wants to modify grades.
- An integer representing the student's number (if the user wants to modify a grade).
- A floating-point number representing the new grade (if the user wants to modify a grade).

**Output:**  
- A list of student numbers and their grades, displayed before and after modifications.

**Output Test Cases:**
- Number of students: 3
  Grades: 4.5, 3.7, 5.0
  Modify grades: no
  Output:
  ```
  1	4.5
  2	3.7
  3	5.0
  ```

- Number of students: 2
  Grades: 2.5, 3.0
  Modify grades: yes, Student number: 1, New grade: 4.0
  Modify grades: yes, Student number: 2, New grade: 5.0
  Modify grades: no
  Output:
  ```
  1	2.5
  2	3.0
  Nr. nemanda sem á að laga: 1
  Einkunn: 4.0
  1	4.0
  2	3.0
  Nr. nemanda sem á að laga: 2
  Einkunn: 5.0
  1	4.0
  2	5.0
  ```

---

## Verkefni: Forritun 1B - Spurning 4
**Description:**  
Create a program to manage meeting attendance records. The program should allow the user to register meetings, print all recorded meetings, save the records to a file, and load records from a file. The user should interact with the program through a menu.

**Input:**  
- An integer for choosing an option from the menu.
- Integers representing the number of females, males, and others attending a meeting (if option 1 is chosen).
- A string representing the filename to save to or load from (if options 3 or 4 are chosen).

**Output:**  
- A table of attendance records displayed when option 2 is chosen.
- Confirmation messages after saving to or loading from a file.

**Output Test Cases:**
- Chosen option: 1, Females: 5, Males: 10, Others: 2
- Chosen option: 1, Females: 8, Males: 7, Others: 1
- Chosen option: 2
  Output:
  ```
  Mæting í kennslustund:
  Female   Male     Other   
  5        10       2       
  8        7        1       
  ```

- Chosen option: 3, Filename: "attendance.txt"
  Output: "Meeting records saved successfully."

- Chosen option: 4, Filename: "attendance.txt"
  Output: "Meeting records loaded successfully."

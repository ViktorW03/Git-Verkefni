# Test function for the Question class
from question import Question
from choice_question import ChoiceQuestion
from exam import Exam

# def test_question_class():
#     q = Question("Who is the inventor of Python?", "Guido van Rossum")
    
#     assert q.get_question() == "Who is the inventor of Python?", "get_question() method failed"
#     assert q.check_answer("Guido van Rossum") == True, "check_answer() with correct answer failed"
#     assert q.check_answer("guido van rossum") == True, "check_answer() with case insensitive answer failed"
#     assert q.check_answer("Unknown") == False, "check_answer() with wrong answer failed"
#     assert str(q) == "Q: Who is the inventor of Python? A: Guido van Rossum", "__str__() method failed"
    
#     print("All tests for Question class passed!")

# # Test function for the ChoiceQuestion class
# def test_choicequestion_class():
#     q2 = ChoiceQuestion("In what year was the Python language first released?")
#     q2.add_choice("1991", True)
#     q2.add_choice("1995", False)
#     q2.add_choice("1998", False)
#     q2.add_choice("2000", False)
    
#     assert str(q2) == "In what year was the Python language first released?\n1. 1991\n2. 1995\n3. 1998\n4. 2000", "__str__() method failed"
#     assert q2.check_answer("1") == True, "check_answer() with correct answer failed"
#     assert q2.check_answer("2") == False, "check_answer() with wrong answer failed"
    
#     print("All tests for ChoiceQuestion class passed!")

# def test_exam_class():
#     q1 = Question("Who is the inventor of Python?", "Guido van Rossum")
#     q2 = ChoiceQuestion("In what year was the Python language first released?")
#     q2.add_choice("1991", True)
#     q2.add_choice("1995", False)
#     q2.add_choice("1998", False)
#     q2.add_choice("2000", False)
#     q3 = Question("What does OOP stand for?", "Object-oriented programming")
#     q4 = ChoiceQuestion("Which of the following is a built-in type in Python?")
#     q4.add_choice("array", False)
#     q4.add_choice("record", False)
#     q4.add_choice("dict", True)
    
#     exam = Exam()
#     exam.add_question(q1)
#     exam.add_question(q2)
#     exam.add_question(q3)
#     exam.add_question(q4)
    
#     assert exam.get_num_questions() == 4, "get_num_questions() method failed"

#     print("All tests for Exam class passed!")

# # Run the test functions
# test_question_class()
# test_choicequestion_class()
# test_exam_class()  # Corrected from test_question_class()

q1 = Question("Who is the inventor of Python?", "Guido van Rossum")
q2 = ChoiceQuestion("In what year was the Python language first released?")
q2.add_choice("1991", True)
q2.add_choice("1995", False)
q2.add_choice("1998", False)
q2.add_choice("2000", False)
q3 = Question("What does OOP stand for?", "Object-oriented programming")
q4 = ChoiceQuestion("Which of the following is a built-in type in Pyhon?")
q4.add_choice("array", False)
q4.add_choice("record", False)
q4.add_choice("dict", True)
exam = Exam()
exam.add_question(q1)
exam.add_question(q2)
exam.add_question(q3)
exam.add_question(q4)


def answer_question(a_question):
    print(a_question.get_question())
    response = input()
    print(a_question.check_answer(response))
    # Main
q = ChoiceQuestion("In what year was the Python language first released?")
q.add_choice("1991", True)
q.add_choice("1995", False)
q.add_choice("1998", False)
q.add_choice("2000", False)
answer_question(q)
print(q)

# exam.take()
# print(f"Your score is {exam.get_points()} point(s) out of {exam.get_num_questions()}")
# print(exam)
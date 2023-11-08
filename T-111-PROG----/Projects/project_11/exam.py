from choice_question import ChoiceQuestion
from question import Question
class Exam:
    """
    Lets user take an exam and add questions,
    hold on to points, number of questions and print the questions
    """
    def __init__(self) -> None:
        self.questions = []
        self.points = 0

    def __str__(self) -> str:
        """
        Make a starting point, then add all the questions to it
        acording to the right format using __repr__ from question.py
        """
        questions = "" # Means no question
        for question in self.questions:
            if questions != "": # Because if there is not a question, add it
                questions += "\n"
            questions += f"{question.__repr__()}" # Call __repr__ to add a question to the f string that
                                                    # prints the question and answer
        return questions

    def add_question(self, question):
        self.questions.append(question)
        self.points += 1
    
    def get_points(self):
        return self.points

    def get_num_questions(self):
        return len(self.questions)
            
    def take(self):
        for question in self.questions:
            print(question.get_question())
            exam_taker_answer = input()
            answer = question.check_answer(exam_taker_answer)
            print(answer)
            print()
            if answer == False:
                self.points -= 1
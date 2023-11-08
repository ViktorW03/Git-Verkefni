from question import Question
class ChoiceQuestion(Question):
    """
    Lets user use the questions from Question class, add choices,
    and check the answer
    """
    def __init__(self, question) -> None:
        super().__init__(question, "")# Inheret the question from the Question class
        self.choices = []
        self.question = question


    def add_choice(self, choice, answer=False): # Set answer to False for error handleing
        self.choices.append(choice)
        if answer:
            super().set_answer(len(self.choices))# Inheret the answer set in questions class and use len to count choices
    
    def check_answer(self, answer) -> bool:
        return int(answer) == int(self._Question__answer_str) # Both values set to int for error handleing
    
    def get_question(self) -> str:
        choices_str = self.question
        index = 1
        for choice in self.choices:
            choices_str += f"\n{index}. {choice}"
            index +=1
        return choices_str

    def __str__(self) -> str:
        return f"Q: {self.question} A: {self._Question__answer_str}"
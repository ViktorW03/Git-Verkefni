class Question:
    """
    Lets ueser create a question and chek the answer and get the question
    """
    def __init__(self, question, answer) -> None:

        self.__question_str = question
        self.__answer_str = answer
        
    def get_question(self):
        return self.__question_str
        
    def check_answer(self, answer) -> bool:
        return self.__answer_str.lower() == answer.lower() # For case sesnetivity.
    
    def set_answer(self, answer):
        self.__answer_str = answer # I
    
    def __str__(self) -> str:
        return f"Q: {self.__question_str} A: {self.__answer_str}"
    
    def __repr__(self) -> str:
        return f"Q: {self.__question_str} A: {self.__answer_str}"


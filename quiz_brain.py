import html
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.number_of_correct_answer = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # if this statement true our
        # input function will until it is false,and it will return true and false

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        text = html.unescape(self.current_question.q_text)

        return f"Q.{self.question_number}:{text}"
        # print(f"Category: {our_question.q_category}\nDifficulty: {our_question.q_difficulty}")
        # user_answer = input(f"Q.{self.question_number}: {our_question.q_text}.(True/False): ").capitalize()
        # self.check_answer(user_answer, our_question.q_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.q_answer
        if user_answer.lower() == correct_answer.lower():
            self.number_of_correct_answer += 1
            return True
        else:
           return False

        # print(f"The correct answer was: {correct_answer}.")
        # print(f"Your current score is: {self.number_of_correct_answer} / {self.question_number}\n")

from cgitb import text
from tkinter import *

from numpy import pad
from quiz_brain import QuizBrain


THEME_COLOR = '#375362'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some question text', width=280, fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_img, command=self.pressed_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, command=self.pressed_false)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text=next_question)
        else:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=f'You have reached to the end of the quiz\nYour score is {self.quiz.number_of_correct_answer} out of {len(self.quiz.question_list)} questions')
        self.score_label.config(text=f'Score: {self.quiz.number_of_correct_answer}')
    def pressed_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def pressed_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
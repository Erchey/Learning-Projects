from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quizz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', fg='white', background=THEME_COLOR, font=('Arial', 10, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=250, bg='white')
        self.question_text = self.canvas.create_text(200, 125, text='Some Quest',
                                                     fill=THEME_COLOR,
                                                     width=380,
                                                     font=('Arial', 20, 'bold'))
        self.canvas.grid(row=1, columnspan=2, pady=30)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, relief='flat',
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, relief='flat',
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def true_pressed(self):
        is_right = self.quizz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        self.give_feedback(self.quizz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quizz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quizz.score}')
            q_text = self.quizz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of this quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

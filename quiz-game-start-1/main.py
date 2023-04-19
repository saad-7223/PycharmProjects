from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = Quizbrain(question_bank)

while quiz.still_has_question():
    a = quiz.next_question()

print(f"You have completed the QUIZ !!!")
print(f"Your final score was {quiz.score}")

class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curr = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {curr.text} (True/False)?: ")
        self.check_answer(ans, curr.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, a, c):
        if a.lower() == c.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was : {c}")
        print(f"Your score is {self.score}/{self.question_number}\n\n")

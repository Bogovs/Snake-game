from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(275)
        self.score = 0
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.write("Game over", align="center", font=("Arial", 20, "normal"))

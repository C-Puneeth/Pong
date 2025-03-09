from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):bbbbb
        self.goto(-100, 200)
        self.write(self.score_1, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.score_2, align="center", font=("Courier", 60, "normal"))

    def lscore_1(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def rscore_2(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()

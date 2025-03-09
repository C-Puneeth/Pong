from turtle import Turtle


class Mid_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(10)
        self.goto(0, 310)
        self.right(90)

    def mline(self):
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.turtlesize(0.5)
        self.goto(0, 0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
        self.last_bounce_time = time.time()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        current_time = time.time()
        if current_time - self.last_bounce_time > 0.1:  # 0.1 second cooldown
            self.x *= -1
            self.move_speed *= 0.8
            self.last_bounce_time = current_time

    def update(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x *= -1  # Ensure the ball changes direction when reset
        self.y *= -1  # Ensure the ball changes direction when reset

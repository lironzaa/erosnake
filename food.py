from turtle import Turtle
import random

chairs = ["chair1.gif", "chair2.gif", "chair3.gif", "chair4.gif"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(chairs[random.randint(0, 3)])
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.speed("fastest")

    def refresh(self):
        self.shape(chairs[random.randint(0, 3)])
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

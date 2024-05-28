from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # #print(f"13 food {random_x} {random_y}")
        # self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        #print(f"20 food {random_x} {random_y}")
        self.goto(random_x, random_y)

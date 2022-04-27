from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self,screenW, screenH):
        super().__init__()
        self.penup()
        self.x = randrange(20,screenW-20,20)
        self.y = randrange(20, screenH-20,20)
        self.shape("circle")
        self.color("red")
        self.shapesize(.5,.5)
        self.goto(self.x,self.y)


    def eaten(self,):
        self.hideturtle()
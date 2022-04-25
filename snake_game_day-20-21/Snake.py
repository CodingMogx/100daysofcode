from turtle import *


class Snake(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("triangle")
        self.tales = []
        self.x = self.pos()[0]
        self.y = self.pos()[1]
        self.create_snake()
        
    def turn_left(self,):
        if self.heading()==0.00:
            pass
        else:
            self.setheading(180)

    def turn_right(self,):
        self.setheading(0)

    def turn_up(self,):
        self.setheading(90)
    
    def turn_down(self,):
        self.setheading(270)

    def auto_move(self,):
        self.x = self.pos()[0]
        self.y = self.pos()[1]
        old_x = self.x
        old_y = self.y
        self.forward(10)
        for tale in self.tales:
            tale_x = tale.pos()[0]
            tale_y = tale.pos()[1]
            print("2")
            tale.setpos(old_x,old_y)
            old_x = tale_x
            old_y = tale_y

    def create_snake(self,):
        for x in range(1,7):
            dele=Turtle("square")
            new_x = self.x-x*20
            dele.setpos(new_x,self.y)
            self.tales.append(dele)
    
    def eat(self,):
        dele=Turtle("square")
        self.tales.append(dele)
    

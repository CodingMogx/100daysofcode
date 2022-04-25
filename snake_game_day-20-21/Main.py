from turtle import *
from Snake import Snake
from time import *


screenHeight = 800
screenWidth = 800
skærm = Screen()

skærm.canvheight = screenHeight
skærm.canvwidth = screenWidth
skærm.tracer(0)
slange = Snake()

skærm.listen()
while True:
    
    print("1")
    skærm.onkey(slange.turn_left, "Left")
    skærm.onkey(slange.turn_right, "Right")
    skærm.onkey(slange.turn_down, "Down")
    skærm.onkey(slange.turn_up, "Up")
    slange.auto_move()
    
    skærm.update()
    sleep(.05)




    
skærm.exitonclick()


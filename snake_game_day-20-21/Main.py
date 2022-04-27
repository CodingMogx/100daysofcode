from turtle import *
from Snake import Snake
from time import *
from Food import Food

screenHeight = 800
screenWidth = 800
skærm = Screen()

skærm.canvheight = screenHeight
skærm.canvwidth = screenWidth
skærm.tracer(0)
slange = Snake()
food = 0
skærm.listen()
while True:
    if food == 0:
        mad = Food(screenH=screenHeight/2, screenW=screenWidth/2)
        food += 1
    print("1")
    skærm.onkey(slange.turn_left, "a")
    skærm.onkey(slange.turn_right, "d")
    skærm.onkey(slange.turn_down, "s")
    skærm.onkey(slange.turn_up, "w")
    slange.auto_move()
    skærm.onkey(slange.eat,"t")
    if slange.distance(mad.x,mad.y) <=10:
        mad.eaten()
        food -=1
    
    skærm.update()
    sleep(.1)




    
skærm.exitonclick()


import turtle
import time
import random
import os
import sys

i = -10 

#Time
skip = 0.1

#Windows Settings
wn = turtle.Screen()
wn.title("Snake Py: El gusanito ")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()

#Player Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"
head.color("white")

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.penup()
food.goto(0,0)
food.direction = "stop"
food.color("red")

#Variables & List
list_new_section = []

def score():
    global i
    i=10+i
    text.goto(0,260)
    text.clear()
    text.write("Score: {}".format(i), align="center", font=("Courier",24,"normal"))
    return(i)
    
def rainbown():
    R = random.randrange(0, 255, 10)
    G = int(255)
    B = random.randrange(0, 255, 10)
    wn.colormode(255)
    print(R,G,B)
    return R,G,B

def up():
    head.direction = "up"
    
def down():
    head.direction = "down"

def left():
    head.direction = "left"

def right():
    head.direction = "right"

def movement():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def generate_food():
    x = random.randrange(-280,280,20)
    y = random.randrange(-280,280,20)
    food.goto(x,y)
    return x,y

def obtain_food_coordenates():
    a = generate_food()
    print("--->",a)    

def digests():
    new_section = turtle.Turtle()
    new_section.speed(0)
    new_section.shape("square")
    new_section.penup()         
    new_section.color(rainbown())
    list_new_section.append(new_section) 

def growing_up():
    total_section = len(list_new_section)
    for index in range(total_section -1 , 0 , -1):
        x = list_new_section[index -1].xcor()
        y = list_new_section[index -1].ycor()
        list_new_section[index].goto(x,y)

    if  total_section > 0 :
        x = head.xcor()
        y = head.ycor()
        list_new_section[0].goto(x,y) 


def eat():    
    if head.distance(food) < 20 :
        #Random generation food
        generate_food()
        #Add new point 
        score()
        #New segment adding in the body
        digests()
    #Growing up , because , the new segment is added. This function append with the head.    
    growing_up()    

def death_wall():
    if head.xcor() > 280 or head.ycor() > 280 or head.xcor() < -280 or head.ycor() < -280 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"        
        os.execl(sys.executable, sys.executable, *sys.argv)

def death_body():                
                for i in list_new_section:   
                    if  len(list_new_section) > 1 :
                        #Ahora puede morir si es mas grande que 1
                        if  i.distance(head) < 20:
                                time.sleep(1)
                                os.execl(sys.executable, sys.executable, *sys.argv)                        
                    
                    
def control():
    wn.listen()
    wn.onkeypress(up, "Up")
    wn.onkeypress(down, "Down")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")

while True:    
    control()
    wn.update()
    death_wall()
    death_body()
    eat()
    movement()
    time.sleep(skip)
    
    

    


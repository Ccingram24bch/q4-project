import turtle
import random

pet = {'name': "", 'breed': "", 'age': 0}

# for the breed figure out how to make the colors in turtle graphics, so the breed chosen determines its color
# add more breeds later maybe
breed = {'Yellow Lab', 'Chocolate Lab', 'German Shepherd', 'Shih Tzu'}

class Dog:
    def __init__(self, name, happiness, health, hunger, thirst, x, y, breed, age):
        self.name = name
        self.happiness = happiness
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.x = x
        self.y = y
        self.breed = breed
        self.age = age

def Petchoice():
    petBreed = ""

    while petBreed not in breed:
        print(breed)
        petBreed = input('Enter which dog breed from the list you would like: ')
        if petBreed == "Shi Tzu":
            dog = turtle.Turtle()
            dog.penup()
            screen = turtle.Screen()
            screen.setup(1000,1000)
            image = 'ShiTzu.jpg'
            screen.addshape(image)
            screen.bgpic(image)

    pet['breed'] = petBreed
    pet['name'] = input('What is the name of your ' + pet['breed'] + '?: ')


Petchoice()

screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()


# sprite integration
# sprite = "...Shih-Tzu-On-White-01.jpg"

# screen.addshape(sprite)
# dog.shape(sprite)

def up():
    tim.setheading(90)
    tim.forward(100)
    x,y = tim.position()
    if tim.ycor() >= 600:
        UP_PAGE = True
        DOWN_PAGE = False
        LEFT_PAGE = False
        RIGHT_PAGE = False
        if UP_PAGE == True:
            screen.setup(1000,500)
            tim.setpos(-350,10)
        #WALK GAME HERe
        #FALSIFY UP PAGE

def down():
    tim.setheading(270)
    tim.forward(100)
    if tim.ycor() <= -1000:
        UP_PAGE = False
        DOWN_PAGE = True
        LEFT_PAGE = False
        RIGHT_PAGE = False
        if DOWN_PAGE == True:
            screen.setup(1000, 500)
            tim.setpos(-350, 10)
        #TRICK GAME?

def left():
    tim.setheading(180)
    tim.forward(100)
    if tim.xcor() <= -1000:
        UP_PAGE = False
        DOWN_PAGE = False
        LEFT_PAGE = True
        RIGHT_PAGE = False
        if LEFT_PAGE == True:
            screen.setup(1000, 500)
            tim.setpos(-350, 10)
        #UPDATE WATER OR HUNGER

def right():
    tim.setheading(0)
    tim.forward(100)
    if tim.xcor() <= 1000:
        screen.setup(500, 5000)
        tim.setpos(100, 100)
        #UPDATE WATER OR HUNGER

def Upright():
    tim.setheading(45)
    tim.forward(100)

def Upleft():
    tim.setheading(135)
    tim.forward(100)

def Downleft():
    tim.setheading(225)
    tim.forward(100)

def Downright():
    tim.setheading(315)
    tim.forward(100)


colors = ["red", "blue", "green", "yellow", "black"]


def clickLeft(x, y):
    tim.color(random.choice(colors))


def clickRight(x, y):
    tim.stamp()


turtle.listen()

turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)


turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(Upright, "'")
turtle.onkey(Upleft, ";")
turtle.onkey(Downleft, '.')
turtle.onkey(Downright, '/')

turtle.mainloop()

#creating images of the Shi Tzu and the Grass background
tim = turtle.Turtle()
tim.penup()
screen = turtle.Screen()
screen.setup(1000,1000)
image = 'test.gif'
screen.addshape(image)
screen.bgpic(image)
image1 = 'Dog1.gif'
screen.addshape(image1)
tim.shape(image1)

tim.speed(10)

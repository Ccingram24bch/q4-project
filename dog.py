import turtle
import random

health = 100
happiness = 0
hunger = 0
thirst = 0
# do age by days
age = 0

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

    pet['breed'] = petBreed
    pet['name'] = input('What is the name of your ' + pet['breed'] + '?: ')


Petchoice()

screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()


# sprite integration
# sprite = "...Shih-Tzu-On-White-01.jpg"

# screen.addshape(sprite)
# tim.shape(sprite)


def up():
    tim.setheading(90)
    tim.forward(100)


def down():
    tim.setheading(270)
    tim.forward(100)


def left():
    tim.setheading(180)
    tim.forward(100)


def right():
    tim.setheading(0)
    tim.forward(100)

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

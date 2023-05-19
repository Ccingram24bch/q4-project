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
dog = turtle.Turtle()
dog.penup()


# sprite integration
# sprite = "...Shih-Tzu-On-White-01.jpg"

# screen.addshape(sprite)
# dog.shape(sprite)

def walk():
    turtle.clear()
    turtle.screensize(1000,500)

def up():
    dog.setheading(90)
    dog.forward(100)
    x,y = tim.position()
    if tim.ycor() >= 600:
        walk()

def down():
    dog.setheading(270)
    dog.forward(100)

def left():
    dog.setheading(180)
    dog.forward(100)

def right():
    dog.setheading(0)
    dog.forward(100)

def Upright():
    dog.setheading(45)
    dog.forward(100)

def Upleft():
    dog.setheading(135)
    dog.forward(100)

def Downleft():
    dog.setheading(225)
    dog.forward(100)

def Downright():
    dog.setheading(315)
    dog.forward(100)


colors = ["red", "blue", "green", "yellow", "black"]


def clickLeft(x, y):
    dog.color(random.choice(colors))


def clickRight(x, y):
    dog.stamp()


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
dog = turtle.Turtle()
dog.penup()
screen = turtle.Screen()
screen.setup(1000,1000)
image = 'test.gif'
screen.addshape(image)
screen.bgpic(image)
image1 = 'Dog1.gif'
screen.addshape(image1)
dog.shape(image1)

dog.speed(10)

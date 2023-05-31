import turtle
import random


pet = {'name': "", 'breed': "", 'age': 0}

# for the breed figure out how to make the colors in turtle graphics, so the breed chosen determines its color
# add more breeds later maybe
breed = {'Yellow Lab', 'Chocolate Lab', 'German Shepherd', 'Shih Tzu'}

class Dog:
    def __init__(self, name, happiness, max_health, current_health, max_hunger, current_hunger, max_thirst, current_thirst, x, y, breed):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.max_hunger = 100
        self.current_hunger = 100
        self.max_thirst = 100
        self.current_thirst = 100
        self.x = x
        self.y = y
        self.breed = breed

def Petchoice():
    petBreed = ""

    while petBreed not in breed:
        print(breed)
        petBreed = input('Enter which dog breed from the list you would like: ')
        if petBreed == "Shih Tzu":
            dog = turtle.Turtle()
            dog.penup()
            screen = turtle.Screen()
            screen.setup(1000, 1000)
            image = 'test.gif'
            screen.addshape(image)
            screen.bgpic(image)
            image1 = 'Dog1.gif'
            screen.addshape(image1)
            dog.shape(image1)
            dog.speed('fastest')

        elif petBreed == "German Shepherd":
            dog = turtle.Turtle()
            dog.penup()
            screen = turtle.Screen()
            screen.setup(1000, 1000)
            image = 'test.gif'
            screen.addshape(image)
            screen.bgpic(image)
            image1 = 'GermanShepherd.gif'
            screen.addshape(image1)
            dog.shape(image1)
            dog.speed('fastest')







        def up():
            dog.setheading(90)
            dog.forward(75)

        def down():
            dog.setheading(270)
            dog.forward(75)

        def left():
            dog.setheading(180)
            dog.forward(75)

        def right():
            dog.setheading(0)
            dog.forward(75)

        def Upright():
            dog.setheading(45)
            dog.forward(75)

        def Upleft():
            dog.setheading(135)
            dog.forward(75)

        def Downleft():
            dog.setheading(225)
            dog.forward(75)

        def Downright():
            dog.setheading(315)
            dog.forward(75)

        turtle.listen()

        turtle.onkey(up, "Up")
        turtle.onkey(down, "Down")
        turtle.onkey(left, "Left")
        turtle.onkey(right, "Right")
        turtle.onkey(Upright, "'")
        turtle.onkey(Upleft, ";")
        turtle.onkey(Downleft, '.')
        turtle.onkey(Downright, '/')


    pet['breed'] = petBreed
   # pet['name'] = input('What is the name of your ' + pet['breed'] + '?: ')
Petchoice()







turtle.mainloop()


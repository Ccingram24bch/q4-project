import turtle
import random
import tkinter

HEIGHT = 1000
WIDTH = 1000

print('Linear Controls-   Arrow Keys are used for linear movement.')
print("Diagonal Controls-  : key is up/left. ' key is up/right.  / is down right. > is down left")

# for the breed figure out how to make the colors in turtle graphics, so the breed chosen determines its color
# add more breeds later maybe
breed = {'Yellow Lab', 'Black Lab', 'German Shepherd', 'Shih Tzu'}

class Dog:
    def __init__(self, name="", max_health=100, current_health=100, max_hunger=100, current_hunger=100, max_thirst=100, current_thirst=100, breed="", activity=0):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.max_hunger = max_hunger
        self.current_hunger = current_hunger
        self.max_thirst = max_thirst
        self.current_thirst = current_thirst
        # self.x = x
        # self.y = y
        self.breed = breed
        self.activity = activity

def create_page_main():
    screen = turtle.Screen()
    screen.title("Main Grass")
    screen.bgcolor("light green")
    screen.setup(width=WIDTH, height=HEIGHT)
    #image = 'test.gif'
    #screen.addshape(image)
    #screen.bgpic(image)

def create_page_fetch():
    screen = turtle.Screen()
    screen.title("Fetch")
    screen.bgcolor("blue")
    #image = 'test.gif'
    #screen.addshape(image)
    #screen.bgpic(image)
 
def create_page_food():
    screen = turtle.Screen()
    screen.title("Food")
    screen.bgcolor("brown")
    #image = 'test.gif'
    #screen.addshape(image)
    #screen.bgpic(image)
 
def switch_page(new_page):
    if new_page == "fetch":
        create_page_fetch()
        dog.setpos(0,0)
    elif new_page == "food":
        create_page_food()
        dog.setpos(0,0)
    else:
        create_page_main()
        dog.setpos(0,0)


petBreed = ""
dog_state = Dog()

while petBreed not in breed:
    print(breed)
    petBreed = input('Enter which dog breed from the list you would like: ')

    #for testing purposes
    if petBreed == "":
        petBreed = "Shih Tzu"
    #testing end

    dog_state.breed = petBreed

    if petBreed == "Shih Tzu":
        dog = turtle.Turtle()
        dog.penup()
        screen = turtle.Screen()
        screen.setup(1000, 1000)
        #image = 'grass.gif'
        #screen.addshape(image)
        #screen.bgpic(image)
        #image1 = 'Tinydog.gif'
        #screen.addshape(image1)
        #dog.shape(image1)
        dog.speed('fastest')

    elif petBreed == "German Shepherd":
        dog = turtle.Turtle()
        dog.penup()
        screen = turtle.Screen()
        screen.setup(1000, 1000)
        #image = 'grass.gif'
        #screen.addshape(image)
        #screen.bgpic(image)
        #image1 = 'GermanShepherd.gif'
        #screen.addshape(image1)
        #dog.shape(image1)
        dog.speed('fastest')

    elif petBreed == "Black Lab":
        dog = turtle.Turtle()
        dog.penup()
        screen = turtle.Screen()
        screen.setup(1000, 1000)
        #image = 'grass.gif'
        #screen.addshape(image)
        #screen.bgpic(image)
        #image1 = 'Blacklab.gif'
        #screen.addshape(image1)
        #dog.shape(image1)
        dog.speed('fastest')

    elif petBreed == "Yellow Lab":
        dog = turtle.Turtle()
        dog.penup()
        screen = turtle.Screen()
        screen.setup(1000, 1000)
        #image = 'grass.gif'
        #screen.addshape(image)
        #screen.bgpic(image)
        #image1 = 'yellow.gif'
        #screen.addshape(image1)
        #dog.shape(image1)
        dog.speed('fastest')

def up():
    dog.setheading(90)
    dog.forward(75)
    x,y = dog.pos()
    if y > HEIGHT / 2:
        switch_page("walk")

def down():
    dog.setheading(270)
    dog.forward(75)
    if dog.xcor() < -HEIGHT / 2:
        switch_page("walk")

def left():
    dog.setheading(180)
    dog.forward(75)
    print(dog_state.activity)
    if dog.xcor() < -WIDTH / 2:
        if dog_state.activity == 0:
            print("GOING LEFT 1")
            dog_state.activity = 1
            switch_page("food")
        elif dog_state.activity == 1:
            print("GOING LEFT 2")
            dog_state.activity = 0
            switch_page("main")
        elif dog_state.activity == 2:
            dog_state.activity = 0
            switch_page("main")

def right():
    dog.setheading(0)
    dog.forward(75)
    print(dog_state.activity)
    if dog.xcor() > WIDTH / 2:
        if dog_state.activity == 0:
            print("GOING RIGHT 1")
            dog_state.activity = 2
            switch_page("fetch")
        elif dog_state.activity == 1:
            print("GOING RIGHT 2")
            dog_state.activity = 0  
            switch_page("main")
            

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

turtle.mainloop()

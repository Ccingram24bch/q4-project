import turtle, sched, time


pet = {'name': "", 'breed': "", 'age': 0}

# for the breed figure out how to make the colors in turtle graphics, so the breed chosen determines its color
# add more breeds later maybe
breed = {'Yellow Lab', 'Chocolate Lab', 'German Shepherd', 'Shih Tzu'}

class Dog:
    def __init__(self, name, happiness, max_health, current_health, max_hunger, current_hunger, max_thirst, current_thirst, x, y, breed):
        self.name = name
        self.happiness = happiness
        self.max_health = 100
        self.current_health = 100
        self.max_hunger = 100
        self.current_hunger = 100
        self.max_thirst = 100
        self.current_thirst = 100
        self.x = x
        self.y = y
        self.breed = breed

#def Petchoice():
    #petBreed = ""

    #while petBreed not in breed:
        #print(breed)
        #petBreed = input('Enter which dog breed from the list you would like: ')
        #if petBreed == "Shi Tzu":
            #dog = turtle.Turtle()
            #dog.penup()
            #screen = turtle.Screen()
            #screen.setup(1000,1000)
            #image = 'ShiTzu.jpg'
            #screen.addshape(image)
            #screen.bgpic(image)

    #pet['breed'] = petBreed
    #pet['name'] = input('What is the name of your ' + pet['breed'] + '?: ')


#Petchoice()

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

def clickLeft(x, y):
    tim.color(random.choice(colors))


def clickRight(x, y):
    tim.stamp()

hbar = turtle.Turtle()

# the survival class has to do with everything involving the dog's overall health, including hunger and thirst
# health, hunger, and thirst will vary based on actions taken by the user


# Set up the turtle for the health bar
#hbar = hbar.Turtle()
hbar.speed(0)  # Set the turtle's animation speed to the maximum
hbar.color("red")
hbar.penup()
hbar.goto(-200, 250)  # Position the turtle at the top left corner of the screen
hbar.pendown()
hbar.hideturtle()

# Set the initial health value and the maximum health value
initial_health = 100
max_health = 100
current_health = initial_health

# Define a function to draw the health bar
def draw_health_bar(health):
    hbar.clear()  # Clear the previous health bar
    width = (health / max_health) * 400  # Calculate the width of the health bar
    hbar.begin_fill()
    for _ in range(2):
        hbar.forward(width)
        hbar.right(90)
        hbar.forward(20)
        hbar.right(90)
    hbar.end_fill()

# Initial drawing of the health bar
draw_health_bar(current_health)

# Example usage: decrease health by 20
current_health -= 20
draw_health_bar(current_health)


#timer stuff
s = sched.scheduler(time.time, time.sleep)
def health_timer(sc):
    #put a vlaue decline for the health bar
    sc.enter(5, 1, health_timer, (sc,))

s.enter(5, 1, health_timer, (s,))
s.run()


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

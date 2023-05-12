health = 100
happiness = 0
hunger = 0
thirst = 0
#do age by days
age = 0

pet = {'name': "", 'breed': "", 'age': 0}

#for the breed figure out how to make the colors in turtle graphics, so the breed chosen determines its color
#add more breeds later maybe
breed = {'Yellow Lab', 'Chocolate Lab', 'German Shepherd'}

class Dog:
    def __init__(self, name, happiness, health, hunger, thirst, x, y, breed, age):
        dog.name = name
        dog.happiness = happiness
        dog.health = health
        dog.hunger = hunger
        dog.thirst = thirst
        dog.x = x
        dog.y = y
        dog.breed = breed
        dog.age = age

def Petchoice():

    petBreed = ""

    while petBreed not in breed:
        print(breed)
        petBreed = input('Enter which dog breed from the list you would like: ')

    pet['breed'] = petBreed
    pet['name'] = input('What is the name of your ' + pet['breed'] + '?: ')

Petchoice()

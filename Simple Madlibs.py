# ▄▄▄       ███▄    █ ▄▄▄█████▓ ██▓███   ▒█████   ██▓  ██████ ▓█████  ███▄    █ 
#▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓██░  ██▒▒██▒  ██▒▓██▒▒██    ▒ ▓█   ▀  ██ ▀█   █ 
#▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██░ ██▓▒▒██░  ██▒▒██▒░ ▓██▄   ▒███   ▓██  ▀█ ██▒
#░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▄█▓▒ ▒▒██   ██░░██░  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒
# ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ▒██▒ ░  ░░ ████▓▒░░██░▒██████▒▒░▒████▒▒██░   ▓██░
# ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ 
#  ▒   ▒▒ ░░ ░░   ░ ▒░    ░    ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░
#  ░   ▒      ░   ░ ░   ░      ░░       ░ ░ ░ ▒   ▒ ░░  ░  ░     ░      ░   ░ ░ 
#      ░  ░         ░                       ░ ░   ░        ░     ░  ░         ░ 
#                                                                              

import random

#Tuples
noun=("car","bus","ball","plane","cup")
season = ("Summer","Fall","Spring","Winter")
superhero = ("Superman","Batman","Spider-Man","Thor","Captain America","Wolverine","Iron-Man","Wonderwoman","Hulk")
animal = ("Dog","Cat","Turtle","Squirrel","Lizard","Nerd","Racoon","Koala","Baboon","Water Buffalo","CatDog")
people = ("Steve Jobs","Bill Gates","Christian Stevens","Prince Harry","Caitlyn Jenner","Kim Kardashian","Miley Cyrus")
verb = ("smoke","run","climb","pounce","lunge","jump","fight","hack","program","stab this programs user","fly","play with each other")
places = ("New York","Secureset","Amersterdam","Denver","Europe","San Franciso","China","India","Madagascar","Quantum Realm")

#Function that generates a random word from the above tuples
def elem(tuple): 
    value = random.randint(0,len(tuple)-1)
    return tuple[value]

# introduction
print ("              ___Welcome to Mad Libs___")
print ("___Press Enter to generate a new story and ! to stop___")

#looping
while True:
    # asks for input to determine if the program needs to be stopped
    x = input("-------------------------------------------------------- \n")
    #▼▼▼sees if the input needs to kill the program
    if x == "!":
        exit
    #if the program doesnt need to be killed then print the mad lib
    else:
        if __name__ == '__main__':
            print("Every " + elem(season) + ", " + elem(superhero) + \
            " is joined by The " + elem(animal) + \
            ", who's secret identity is " + elem(people) + \
            ". They attempt to " + elem(verb) +\
            ", which rarely succeeds. So instead they chase down a " + \
            "villain in " + elem(places) + " who was trying to steal a " + \
            elem(noun) + ".") 

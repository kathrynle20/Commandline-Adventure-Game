from text import exit
from room1 import room1
from room2 import room2

def welcome():
    print("Welcome to the Adventure Game!")
    print("Imagine you are stuck in a maze with many rooms and you can't see where you are.")
    print("You are only given the choice to choose a room. The adventure may be a safe or a dangerous one.")
    print("Whenever you want to leave you can enter exit")
    print("There might be tricks coming your way.... Watch out and good luck! Most importantly, have fun!")

    welcome_room = input("Your first room is the starting room. You leave the first room and are faced with 2 rooms numbers 1 and 2. Enter 1 or 2.")
    if welcome_room == "1":
        room1()
    elif welcome_room == "2":
        room2()
    elif welcome_room == "exit":
        exit()
    else:
        print("Please enter 1 or 2")
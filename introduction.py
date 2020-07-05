from text import exit_game
from room1 import room1
from room2 import room2


def introduction():
    print("Welcome to the Adventure Game!")
    print("Imagine you are stuck in a maze with many rooms and you can't see where you are.")
    print("You are only given the choice to choose a room. The adventure may be a safe or a dangerous one.")
    print("Whenever you want to leave you can enter exit (all lowercase letters)")
    print("There might be tricks coming your way.... Watch out and good luck! Most importantly, have fun!")
    print("Your first room is the starting room")

    welcome_room = input("You leave the first room and are faced with 2 rooms numbers 1 and 2. Enter 1 or 2:")
    
    choose = True
    while choose:
        if welcome_room == "1":
            room1()
            choose = False
        elif welcome_room == "2":
            room2()
            choose = False
        elif welcome_room == "exit":
            exit_game()
            choose = False
        else:
            welcome_room = input("Please enter 1 or 2")
            choose = True

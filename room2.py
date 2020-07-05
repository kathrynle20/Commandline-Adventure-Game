from text import room2_text
import random
from lost import lost
from text import exit_game
from room3 import room3


def room2():
    room2_text()
    safe_key = random.randint(1, 2)

    room2_choice = input("Please enter 1 or 2 to pick a key.")

    choose = True
    while choose:
        if room2_choice == "1":
            if safe_key == 1:
                print("Congratulations, you unlocked the rabbit cage! You are safe to move on to the next room.")
                room3()
            else:
                print("Unfortunately you died because the lion ate you.")
                lost()
            choose = False
        elif room2_choice == "2":
            if safe_key == 2:
                print("Congratulations, you unlocked the rabbit cage! You are safe to move on to the next room.")
                room3()
            else:
                print("Unfortunately you died because the lion ate you.")
                lost()
            choose = False
        elif room2_choice == "exit":
            exit_game()
            choose = False
        else:
            room2_choice = input("Please enter 1 or 2 to pick a key.")
            choose = True

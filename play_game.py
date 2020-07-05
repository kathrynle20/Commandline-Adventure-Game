from introduction import introduction
import random


def play():
    ifPlay = input("Would you like to play the Adventure Game? Enter 1 for yes and 2 for no.")
    
    choose = True
    while choose:
        if ifPlay == "1":
            choose = False
            introduction()
        elif ifPlay == "2":
            choose = False
            print("Thank you for coming! Hope you can play next time.")
        else:
            choose = True
            ifPlay = input("Please enter 1 to play and 2 to exit.")

play()

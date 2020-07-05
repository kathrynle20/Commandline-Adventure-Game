from welcome import welcome
import random
from lost import lost

def play():
    ifPlay = input("Would you like to play the Adventure Game? Enter 1 for yes and 2 for no.")
    if ifPlay == "1":
        welcome()
    elif ifPlay == "2":
        print("Thank you for coming! Hope you can play next time.")

play()

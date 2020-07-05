from text import room3_text
import random
from lost import lost
from text import exit

def room3():
    room3_text()
    room3_choice = input("1 is Protego (shield) and 2 is Sectunsempra (attack). Please enter 1 or 2.")

    try_again = True

    while try_again:
        opponent_spell = random.randint(1,2)
        if opponent_spell == 1:
            opponent_spell = "Protego"
        else:
            opponent_spell = "Sectumsempra"

        if room3_choice == "1":
            if opponent_spell == "Protego":
                print("OH NO! You and your opponent both chose Protego!")
                again = input("1 is Protego (shield) and 2 is Sectunsempra (attack). Please enter 1 or 2.")
                try_again = True
            else:
                print("Congratulations! You blocked your opponent's attack and bought time to escape into the next room safely")
                try_again = False
        
        elif room3_choice == "2":
            if opponent_spell == "Protego":
                print("Congratulations! You attacked your opponent when they chose to sheild.")
                print("You were able to escape safely to the next room!")
                try_again = False
            else:
                print("OH NO! Both you and your opponent attacked each other! You both died.")
                lost()
                try_again = False
        
        elif room3_choice == "exit":
            exit()
            try_again = False
        
        else:
            room3_choice = input("Please enter 1 or 2.")
            try_again = True

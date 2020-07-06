import text
import random
import lost
import room3


def room2():
    text.room2_text()
    safe_key = random.randint(1, 2)

    room2_choice = input("Please enter 1 or 2 to pick a key: ")

    choose = True
    while choose:
        if room2_choice == "1":
            if safe_key == 1:
                print("Congratulations, you unlocked the rabbit cage! You are safe to move on to the next room.")
                room3.room3()
            else:
                print("Unfortunately you died because the lion ate you.")
                lost.lost()
            choose = False
        elif room2_choice == "2":
            if safe_key == 2:
                print("Congratulations, you unlocked the rabbit cage! You are safe to move on to the next room.")
                room3.room3()
            else:
                print("Unfortunately you died because the lion ate you.")
                lost.lost()
            choose = False
        elif room2_choice == "exit":
            text.exit_game()
            choose = False
        else:
            room2_choice = input("Please enter 1 or 2 to pick a key: ")
            choose = True

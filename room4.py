import text
import lost
import room2
import random


def room4():
    text.room4_text()
    room4_name = input("First, choose your superhero! You can type in your favorite superhero or make one up just for yourself!")
    print("Hello " + room4_name + " now you must choose a magic word")
    room4_choice = input("Which magic word would you like to call: C924 or G420")
    
    choose = True
    while choose:
        superhero = random.randint(1, 2)
        if room4_choice == "C924":
            if superhero == 1:
                print("Congrats! You have picked the correct code name. A Superhero came and save you!")
                print("Now you are faced with 2 doors to exit to.")
                choose_door()
            else:
                print("Sorry you pickd the wrong code name! You were killed by a villain.")
                lost.lost()
            choose = False
        elif room4_choice == "G420":
            if superhero == 1:
                print("Sorry you picked the wrong code name! You were killed by a villain.")
                lost.lost()
            else:
                print("Congrats! You have picked the correct code name. A Superhero came and save you!")
                print("Now you are faced with 2 doors to exit to.")
                choose_door()
            choose = False
        elif room4_choice == "exit":
            choose = False
            text.exit_game()
        else:
            room4_choice = input("Please enter C924 or G429")
            choose = True


def choose_door():
    win_door = random.randint(1, 2)
    
    choose = True
    while choose:
        door_choice = input("Enter 1 or 2 to choose a door")
        if door_choice == "1":
            if win_door == 1:
                text.win()
            else:
                text.return_to_room2_text()
                room2()
            choose = False
        elif door_choice == "2":
            if win_door == 2:
                text.win()
            else:
                text.return_to_room2_text()
                room2()
            choose = False
        elif door_choice == "exit":
            text.exit_game()
            choose = False
        else:
            choose = True

import text
import random
import lost
import room3


def room1():
    text.room1_text()
    safe_book = random.randint(1, 2)
    
    choose = True
    while choose:
        room1_choice = input("Enter 1 or 2 to choose a book: ")
        if room1_choice == "1":
            if safe_book == 1:
                print("Congratulations, you found the key! You may use the key to move on to the second room.")
                room3.room3()
            else:
                print("Unfortunately you died because the books have fallen on you.")
                lost.lost()
            choose = False
        elif room1_choice == "2":
            if safe_book == 2:
                print("Congratulations, you found the key! You may use the key to move on to the second room.")
                room3.room3()
            else:
                print("Unfortunately you died because the books have fallen on you.")
                lost.lost()
            choose = False
        elif room1_choice == "exit":
            text.exit_game()
            choose = False
        else:
            choose = True

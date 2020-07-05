from play_game import play
from text import exit

def lost():
    print("Sorry you lost the game!")
    if_play_again = input("If you would like to play again please enter play, if not then enter exit")
    if if_play_again == "play":
        play()
    elif if_play_again == "exit":
        exit()

    
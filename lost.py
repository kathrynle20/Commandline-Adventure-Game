import introduction
import text


def lost():
    print("Sorry you lost the game!")
    if_play_again = input("If you would like to play again please enter play, if not then enter exit")
    
    choose = True
    while choose:
        if if_play_again == "play":
            introduction.introduction()
            choose = False
        elif if_play_again == "exit":
            text.exit_game()
            choose = False
        else:
            if_play_again = input("Please enter play or exit (all in lowercase letters)")
            choose = True

    
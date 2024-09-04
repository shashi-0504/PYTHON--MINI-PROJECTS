
import random
print(" \n                ROCK PAPER SCISSOR GAME                         ")
print("........................................................................................")
print('"1"-->ROCK\n"2"-->PAPER\n"3"-->SCISSOR\n"4"-->STOP PLAYING')
print("........................................................................................")
while(True):

    user_input = int(input("Select 1 or 2 or 3 or 4 : "))
    if (user_input == 1):
        print("User choice is ROCK")
    elif (user_input == 2):
        print("User choice is PAPER")
    elif (user_input == 3):
        print("User choice is SCISSOR")
    else:
        break
    computer_choice = random.randint(1, 3)
    if (computer_choice == 1):
        print("computer choice is ROCK")
    elif (computer_choice == 2):
        print("computer choice is PAPER")
    else:
        print("computer choice is SCISSOR")
    if (user_input == computer_choice):
        print("TIE")
        print("........................................................................................")
    elif (user_input == 1 and computer_choice == 2):
        print("You lose and computer wins")

        print("........................................................................................")
    elif (user_input == 1 and computer_choice == 3):
        print("You win")

        print("........................................................................................")
    elif (user_input == 2 and computer_choice == 1):
        print("You win")

        print("........................................................................................")
    elif (user_input == 2 and computer_choice == 3):
        print("You lose and computer wins")

        print("........................................................................................")
    elif (user_input == 3 and computer_choice == 1):
        print("You lose and computer wins")

        print("........................................................................................")
    elif (user_input == 3 and computer_choice == 2):

        print("You win")

        print("........................................................................................")
    elif(user_input==4):
        break
    else:
        print("User entered Invalid input")
        print(".................................1.......................................................")
    ask=input("Do you want to play again (y/n) :")
    print("........................................................................................")

    if(ask=='y'or ask=='Y'):
        pass
    else:
        break




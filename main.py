from game1 import guess_num
from game2 import make_PC_guess_num
from game3 import baseball

Game = int(input("Which game do you want to play? [1-6] : "))

if Game == 1:
    print("\nWelcome to Number Guesser! Play to know your LUCK")
    x = int(input("Select a level : "))
    guess_num(x)

elif Game == 2:
    print("\nWelcome to Number Matcher! Play to test your Computer's LUCK")
    x = int(input("Select a level : "))
    make_PC_guess_num(x)

elif Game == 3:
    print("\nLet's play Baseball!")
    baseball()
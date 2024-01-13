from PyGames.game1 import guess_num
from PyGames.game2 import make_PC_guess_num


Game = int(input("Which game do you want to play? [1-6]"))

if Game == 1:
    print("Welcome to Number Guesser! Play to know your LUCK")
    x = int(input("Select a level : "))
    guess_num(x)

elif Game == 2:
    print("Welcome to Number Matcher! Play to test your LUCK")
    x = int(input("Select a level : "))
    make_PC_guess_num(x)
    





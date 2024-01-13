import random
import math

def guess_num(max_int):
    
    print(f"level set to =============> {max_int}")
    print(f"Guess a number from 1 to {max_int}!")
    rand = random.randint(1,max_int)
    guess = 0
    attempts = 0
    verdict = 0
    guess_list = []
    luck = ["Worst","Bad", "Neutral", "Good", "Excellent!!"]
    while guess != rand:
        guess = int(input("Enter your guess: "))   
        if guess in guess_list:
            print(f"You already attempted {guess} before. This attempt wont count. Please try again")     
        elif guess > rand:
            guess_list.append(guess)
            print(f"Nope, too high!  failed attempts : {guess_list}")
        elif guess < rand:
            guess_list.append(guess)
            print(f"Nope, too low!  failed attempts : {guess_list}")

    
    print(f"You guess the number correctly. Its {rand}.")
    
    attempts = len(guess_list) + 1
    print(f"failed attempts: {guess_list}, Total Attempts : {attempts}, Max attempts required :", math.ceil(math.log(max_int, 2)))

    if attempts <= math.ceil(0.5*(math.log(max_int, 2))):
        print(f"Tried to attempt in less than {math.ceil(0.5*(math.log(max_int, 2)))} moves")
        verdict = 4
    elif attempts <= math.ceil(0.7*(math.log(max_int, 2))):
        print(f"Tried to attempt in less than {math.ceil(0.7*(math.log(max_int, 2)))} moves")
        verdict = 3
    elif attempts <= math.ceil(1*(math.log(max_int, 2))):
        print(f"Tried to attempt in less than {math.ceil(1*(math.log(max_int, 2)))} moves")
        verdict = 2
    elif attempts <= math.ceil(1.5*(math.log(max_int, 2))):
        print(f"Tried to attempt in less than {math.ceil(1.5*(math.log(max_int, 2)))} moves")
        verdict = 1
    else:
        print(f"Tried to attempt in less than {max_int+1} moves")
        verdict = 0

    print("Your Luck today is", luck[verdict])
    new_game = input("Do you want to play again? [Y/N] or Change level [C] : ")
    if new_game == 'Y' or new_game == 'y':
        guess_num(max_int)
    elif new_game == 'N' or new_game == 'n':
        print('Thanks for playing Number Guesser. Bye!')
    elif new_game == 'C' or new_game == 'c':
        new_num = int(input("Select a level : "))
        max_int = new_num
        guess_num(max_int)
    else:
        print("Invalid input, Do you want to play again? [Y/N] :") 

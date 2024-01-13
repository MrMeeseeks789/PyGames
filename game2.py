import math
import random

def make_PC_guess_num(max_int):
    print(f"Think of a number between 1 and {max_int}")
    attempts = 0
    feedback = ''
    min_int = 1
    comp_guess = 0
    while feedback != 'c':
        comp_guess = random.randint (min_int, max_int)
        print(f"Is it {comp_guess}?")
        feedback = input("No, Higher [h] - Lower [l] || Yes, Correct[c] :")
        if feedback == 'h':
            min_int = comp_guess + 1
            attempts += 1
        elif feedback == 'l':
            max_int = comp_guess - 1
            attempts += 1
    attempts += 1
    print(f"Yay! I guessed it in {attempts} moves.")
    return attempts
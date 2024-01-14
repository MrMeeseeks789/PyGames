import random
import numpy as np 

def toss():
    options = ["bat", "bowl"]
    toss_call = input("Choose Odd [O] or Even [E] : ")
    toss_value = int(input("Enter a Value between 1 and 10 : "))
    comp_toss_value = random.randint(1,10)
    toss_total = toss_value + comp_toss_value
    print (f"computer : {comp_toss_value} \nTotal ==> {f'ODD ({toss_total})' if toss_total%2 == 1 else f'EVEN ({toss_total})'}") 
    if (toss_call == 'e' and toss_total%2 == 0) or (toss_call == 'o' and toss_total%2 == 1) :
        toss = input("\nTOSS UPDATE: You won the toss. Bat or Bowl? \n")
        options.remove(toss)
        print(f"You chose to {toss} & Computer get to {options[0]}")
    elif (toss_call == 'e' and toss_total%2 == 1) or (toss_call == 'o' and toss_total%2 == 0) :
        comp_toss = random.choice(options)
        options.remove(comp_toss)
        toss = options[0]
        print(f"\nTOSS UPDATE: Computer won the toss. \nIt chose to {comp_toss} & You get to {toss}")
    return toss


def bat(target_to_chase):
    print("\n***** \nTime to bat!")
    batting_card = []
    bat_first = False
    out = False
    balls = 0
    if int(bool(target_to_chase)) == 0:
        bat_first = True
        target_to_chase = 0
    while out != True:
        run = int(input("Score a number from 1 to 10 : "))
        ball = bowl_prob()
        if abs(run-ball) == 1:
            out = True
            print (f"Computer chose ---------------------> {ball} Bowled!")
            total_runs = sum(batting_card)
            balls = len(batting_card) + 1
            print(f"You scored a total of {total_runs} in {balls} balls with a strike rate of {total_runs/balls}")
            break
        elif run == ball:
            print(f"Computer chose ---------------------> {ball} (Double run)")
            batting_card.append(2*run)
            scr_target (batting_card,bat_first,target_to_chase)
        else:
            print(f"Computer chose ---------------------> {ball}")
            batting_card.append(run)
            if sum(batting_card) <= target_to_chase or (sum(batting_card) > target_to_chase and bat_first == True):
                scr_target (batting_card,bat_first,target_to_chase)
        if sum(batting_card) > target_to_chase and bat_first == False: # won chasing
            return sum(batting_card), len(batting_card)
    return total_runs, balls


def bowl(target_to_defend):
    print("\n///////\nTime to bowl!")
    batting_card = []
    bowl_first = False
    out = False
    balls = 0
    if int(bool(target_to_defend)) == 0 and type(target_to_defend) is not int:
        bowl_first = True
        target_to_defend = 0
    while out != True:
        probabilities = np.random.dirichlet(np.ones(10), size=1)[0]
        for i in range(5):
            run = random.choices(range(1, 11), weights=probabilities)[0]
            ball = int(input("Bowl a number from 1 to 10 : "))
            if abs(run-ball) == 1:
                out = True
                print(f"Computer chose ---------------------> {run} Bowled!!!!")
                total_runs = sum(batting_card)
                balls = len(batting_card) + 1
                print(f"Computer scored a total of {total_runs} in {balls} balls with a strike rate of {total_runs/balls}")
                break
            elif run == ball:
                print(f"Computer chose ---------------------> {ball} (Double run)")
                batting_card.append(2*run)
                scr_target (batting_card,bowl_first,target_to_defend)
            else:
                print(f"Computer chose ---------------------> {run}")
                batting_card.append(run)
                scr_target (batting_card,bowl_first,target_to_defend)
            total_runs = sum(batting_card)
            if total_runs > target_to_defend and bowl_first == False: # won chasing
                return total_runs, len(batting_card)
    return total_runs, balls
                
def bowl_prob():
    numbers = np.arange(2,10)
    probabilities = np.arange(2,10)
    result = random.choices(numbers, weights=probabilities)[0]
    return result
            
def scr_target (batting_card,bowl_first,target_to_defend):
    print(f"========> Score: {sum(batting_card)}({len(batting_card)})")
    if not bowl_first and (target_to_defend-sum(batting_card)+1 > 0):
        print(f"--------> Target Remaining: {target_to_defend-sum(batting_card)+1}")


# main function

def baseball():
    print("TOSS TIME\n-----------------------------------------\n")
    t = toss()
    if t == 'bat':
        my_runs, my_balls = bat(None)
        print(f"\n-----------------------------------------\nINNINGS BREAK\n-----------------------------------------\nComputer's Target: {my_runs+1} runs")
        comp_runs, comp_balls = bowl(my_runs)
        print("\n-----------------------------------------\nRESULT")
        if my_runs > comp_runs:
            print(f"You won the game by {my_runs-comp_runs} runs. Congrats!!!")
        elif my_runs == comp_runs:
            print(f"Its a Tie.. Both scored {my_runs} runs. GG")
        else:
            print(f"You lost. Computer scored {comp_runs} runs in {comp_balls} balls and won the match. Tough luck")
        
    elif t == 'bowl':
        comp_runs, comp_balls = bowl(None)
        print(f"\n-----------------------------------------\nINNINGS BREAK\n-----------------------------------------\nYour Target: {comp_runs+1} runs")
        my_runs, my_balls = bat(comp_runs)
        print("\n-----------------------------------------\nRESULT")
        if my_runs > comp_runs:
            print(f"You won the game by scoring {my_runs} runs in {my_balls} with an strike rate of {float(my_runs/my_balls)}. Congrats!!!")
        elif my_runs == comp_runs:
            print(f"Its a tie.. Both scored {my_runs} runs. GG")
        else:
            print(f"You lost. Computer won the game by {comp_runs-my_runs} runs. Tough luck")
        
    return 0



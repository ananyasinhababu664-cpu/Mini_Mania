import random
def hand_game():
    print("let's being with the game!")
    option = ['R','P','S']
    ci=random.choice(option)
    
    print("for PAPER press 'P',for SCISSOR press 'S',for ROCK press 'R'")
    ui=input("enter your choice:")
    print("computer's choice:",ci)
    if ui==ci:
        print("Tie")
    elif ui=='R' and ci=='P'or ui=='P' and ci=='S':
        print ("Opps!You Lose")
    else:
        print("Congrats!You Win")    

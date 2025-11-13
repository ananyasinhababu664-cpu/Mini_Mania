import random,pickle
from rank_sys import rank_sort
def guess_no(username):
    print("let's play the game!")
    comp_input=random.randint(1,30)
    score = 30
    while True:
        user_input=int(input("\nGuess a number between 1-30:"))
        if user_input==comp_input:
            print("Congrats!You won with a score of ",score)
            break
        elif user_input<comp_input:
            score -= 1
            print("Number guessed is too low")
        else:
            score -= 1
            print("Number guessed is too high")
    f = open('rank_gn.obj','rb')
    rank = pickle.load(f)
    curr_data = [score , username]
    rank.append(curr_data)
    f.close()
    f = open('rank_gn.obj','wb')
    rank = rank_sort(rank)
    pickle.dump(rank,f)
    f.close()
f = open('rank_gn.obj','wb')
# rank = rank_sort(rank)
pickle.dump([],f)
f.close()
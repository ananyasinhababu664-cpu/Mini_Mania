import random,pickle
from rank_sys import rank_sort
def scribble_word(username):
    words=['python','computer','keyboard','program','jumble']
    word=random.choice(words)
    j=list(word)
    random.shuffle(j)
    jumbled_word="".join(j)
    print("Jumbled word is:",jumbled_word)
    score = 100 
    while True:
        guess=input("Enter Guess:")
        if guess==word:
            print("Correct! Your score is:",score)
            break
        else:
            print("Opps! Wrong Guess!")
            score -= 10       
    f = open('rank_sg.obj','rb')
    rank = pickle.load(f)
    curr_data = [score , username]
    rank.append(curr_data)
    f.close()
    f = open('rank_sg.obj','wb')
    rank = rank_sort(rank)
    pickle.dump(rank,f)
    f.close()
    

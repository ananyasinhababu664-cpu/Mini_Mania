def rank_sort(D):  #Bubble Sort
    for i in range(len(D)):
        for j in range(i,len(D)-1):
            if(D[j][0] < D[j+1][0]):
                D[j] , D[j+1] = D[j+1] , D[j]
    return D

def leaderboard(filename):
    import pickle
    print('\t\t**LEADERBOARD**')
    print("Rank  Name    Score")
    f = open(filename, "rb")
    data = pickle.load(f)
    for i in range(len(data)):
        print(i+1 , '   ', data[i][1] , '  ', data[i][0])
from guess_numb import guess_no
from rock_ps import hand_game
from scribble_game import scribble_word
from rank_sys import leaderboard
txt='''\nMini Games!!!
    - Guess the number (1)
    - Rock,Paper,Scissors(2)
    - Scribble/Jumble word(3)
Select a game(press q to exit):\n'''

while True:
    value=input(txt)
    player = input('Enter Player Name:')
    if value=="1":
        guess_no(player)
        ans = input("For Leaderboard print 'y': ")
        if ans in 'yesYES':
            leaderboard("rank_gn.obj")
    elif value=="2":
        hand_game()
    elif value=="3":
        scribble_word(player)
        ans = input("For Leaderboard print 'y': ")
        if ans in 'yesYES':
            leaderboard("rank_sg.obj")
    else:
        print(" Exit")
        break
    

def attack(p1,p2,player):
    fro,to = input('Enter the move combination - ').split()
    if player[p1][fro] == 0 or player[p2][to] == 0:
        print('Hand ded!')
        attack(p1,p2,player)
    else:
        player[p2][to] += player[p1][fro]
        if player[p2][to] > 5:
            player[p2][to] = 0


def split(p, player):
    hand,keep,give = input('Enter the move combination - ').split()
    keep = int(keep)
    give = int(give)
    opp = 'R' if hand == 'L' else 'L'
    try:
        assert keep+give==player[p][hand]
        player[p][hand] = keep
        player[p][opp] += give
        if player[p][opp] > 5:
            player[p][opp] = 0        
    except AssertionError:
        print('Invalid split!')
        split(p, player)


def type_of_moov(p1,p2,player):
    print('Enter type of move for Player',p1,'- ')
    move = input()
    if move == 'A':
        attack(p1,p2,player)
    elif move == 'S':
        split(p1,player)
    else:
        print('Invalid move!\nValid moves are:\nA - attack\nS - split')
        type_of_moov(p1,p2,player)

def check_winner(player):
    if(player[1]['L']==0 and player[1]['R']==0):
        return 2
    elif(player[2]['L']==0 and player[2]['R']==0):
        return 1
    else:
        return 0

def display_current(player):
    print('Current status:')
    print('Player 1 -', player[1]['L'], player[1]['R'])
    print('Player 2 -', player[2]['L'], player[2]['R'])
    print('\n')

def game():
    player = { 1:{'L':1, 'R':1}, 2:{'L':1, 'R':1} }
    turn = 1
    idle = 2
    winner = check_winner(player)
    while(winner==0):
        display_current(player)
        type_of_moov(turn, idle ,player)
        winner = check_winner(player)
        turn, idle = idle, turn
    print('Player', winner, 'won!')
    ch = input('Play Again? (y/n) ')
    if(ch == 'y'):
        return True
    else:
        return False

choice = True
while choice:
    choice = game()
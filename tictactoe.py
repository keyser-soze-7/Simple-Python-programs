board = {'tL': ' ', 'tM': ' ', 'tR': ' ',
         'mL': ' ', 'mM': ' ', 'mR': ' ',
         'lL': ' ', 'lM': ' ', 'lR': ' '}


def print_board():
    print(board['tL'] + '|' + board['tM'] + '|' + board['tR'])
    print('-+-+-')
    print(board['mL'] + '|' + board['mM'] + '|' + board['mR'])
    print('-+-+-')
    print(board['lL'] + '|' + board['lM'] + '|' + board['lR'])

def win():
    if(board['tL'] == board['tM'] == board['tR'] != ' '):
        return 1
    elif(board['mL'] == board['mM'] == board['mR'] != ' '):
        return 1
    elif(board['lL'] == board['lM'] == board['lR'] != ' '):
        return 1
    elif(board['tL'] == board['mL'] == board['lL'] != ' '):
        return 1
    elif(board['tM'] == board['mM'] == board['lM'] != ' '):
        return 1
    elif(board['tR'] == board['mR'] == board['lR'] != ' '):
        return 1
    elif(board['tL'] == board['mM'] == board['lR'] != ' '):
        return 1
    elif(board['tR'] == board['mM'] == board['lM'] != ' '):
        return 1
    else:
        return 0

def full():
    for v in board.values():
        if(v == ' '):
            return 1
        
    return 0

def move(char):
    print('Enter the position player: ' + char)
    pos = input()
    spl = 0
    while(spl == 0):
        for r in board.keys():
            if(r == pos and board[pos] == ' '):
                spl = 1
                break
        if(spl == 0):
            print('Enter valid position: ')
            pos = input()
        
    board[pos] = char
    return      



char = 'x'
while(win() == 0 and full() == 1):
    print_board()
    move(char)
    if(char == 'x'):
        char = 'o'
    else:
        char = 'x'

print_board()        
if(full() == 0):
    print('Match drawn')

else:
    if(char == 'o'):
        print('Player 1 wins')
    else:
        print('Player 2 wins')


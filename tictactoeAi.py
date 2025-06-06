human='X'
computer='O'

board=[' ']*9
def displayboard(board):
    print("-"*9)
    print(f' |{board[0]}|{board[1]}|{board[2]}|')
    print(f' |{board[3]}|{board[4]}|{board[5]}|')
    print(f' |{board[6]}|{board[7]}|{board[8]}|')
    print("-" * 9)

def checkwin():
    if board[0]==board[1]==board[2] and board[0]!=' ':
        return True
    elif board[3]==board[4]==board[5] and board[3]!=' ':
        return True
    elif board[6]==board[7]==board[8] and board[6]!=' ':
        return True
    elif board[0]==board[4]==board[8] and board[0]!=' ':
        return True
    elif board[2]==board[4]==board[6] and board[2]!=' ':
        return True
    elif board[0]==board[3]==board[6] and board[0]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    else:
        return False

def iswin(letter):
    if board[0]==board[1]==board[2] and board[0]==letter:
        return True
    elif board[3]==board[4]==board[5] and board[3]==letter:
        return True
    elif board[6]==board[7]==board[8] and board[6]==letter:
        return True
    elif board[0]==board[4]==board[8] and board[0]==letter:
        return True
    elif board[2]==board[4]==board[6] and board[2]==letter:
        return True
    elif board[0]==board[3]==board[6] and board[0]==letter:
        return True
    elif board[1]==board[4]==board[7] and board[1]==letter:
        return True
    elif board[2]==board[5]==board[8] and board[2]==letter:
        return True
    else:
        return False

def checkdraw():
    if board.count(' ') == 0:
        return True
    else:
        return False

def emptyspaces(pos):
    if board[pos]==' ':
        return True
    else:
        return False

def humanplayer(position,letter):
    board[position]=letter
    displayboard(board)
    if checkwin():
        if letter=='X':
            print('human won')
            exit()
        else:
            print("computer wins")
            exit()
    if checkdraw():
        print("Tied")
        exit()

def computerplayer(letter):
    bestscore=-100
    bestpos=0
    for index in range(0,len(board)):
        if emptyspaces(index):
            board[index]=letter
            score=minimax(board,False)
            board[index]=' '
            if score>bestscore:
                bestscore=score
                bestpos=index
    board[bestpos]=letter
    displayboard(board)
    if checkwin():
        if letter=='O':
            print('computer won')
            exit()
        else:
            print("human wins")
            exit()
    if checkdraw():
        print("Tied")
        exit()
    return

def minimax(board,ismaximising):
    if iswin(computer):
        return 10
    elif iswin(human):
        return -10
    elif checkdraw():
        return 0
    if ismaximising:
        bestscore = -100
        for index in range(0, len(board)):
            if emptyspaces(index):
                board[index] = computer
                score = minimax(board, False)
                board[index] = ' '
                bestscore=max(bestscore,score)
        return bestscore
    else:
        bestscore=100
        for index in range(0,len(board)):
            if emptyspaces(index):
                board[index]=human
                score=minimax(board,True)
                board[index]=' '
                bestscore = min(bestscore, score)
        return bestscore

displayboard(board)
while not checkwin():
    userip=int(input('enter the position :'))
    if board[userip]!=' ':
        print('invalid move')
        continue
    humanplayer(userip,human)
    computerplayer(computer)

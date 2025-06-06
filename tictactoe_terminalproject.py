import random

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

def checkdraw():
    if board.count(' ')==0:
        return True



def emptyspaces():
    global empty
    empty=[]
    for i in range(len(board)):
        if board[i]==' ':
            empty.append(i)


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

def computerplayer(letter):
    emptyspaces()
    compmove=random.choice(empty)
    board[compmove]=letter
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

displayboard(board)
while not checkwin():
    userip=int(input('enter the position :'))
    if board[userip]!=' ':
        print('invalid move')
        continue
    humanplayer(userip,human)
    computerplayer(computer)



#alternate

# import random
#
# human='X'
# computer='O'
#
# board=[' ']*9
# def displayboard(board):
#     print("-"*9)
#     print(f' |{board[0]}|{board[1]}|{board[2]}|')
#     print(f' |{board[3]}|{board[4]}|{board[5]}|')
#     print(f' |{board[6]}|{board[7]}|{board[8]}|')
#     print("-" * 9)
#
# def checkwin():
#     if board[0]==board[1]==board[2] and board[0]!=' ':
#         return True
#     elif board[3]==board[4]==board[5] and board[3]!=' ':
#         return True
#     elif board[6]==board[7]==board[8] and board[6]!=' ':
#         return True
#     elif board[0]==board[4]==board[8] and board[0]!=' ':
#         return True
#     elif board[2]==board[4]==board[6] and board[2]!=' ':
#         return True
#     elif board[0]==board[3]==board[6] and board[0]!=' ':
#         return True
#     elif board[1]==board[4]==board[7] and board[1]!=' ':
#         return True
#     elif board[2]==board[5]==board[8] and board[2]!=' ':
#         return True
#     else:
#         return False
#
# def checkdraw():
#     if board.count(' ') == 0:
#         return True
#     return False
#
# def emptyspaces(pos):
#     if board[pos]==' ':
#         return True
#     else:
#         return False
#
# def humanplayer(position,letter):
#     board[position]=letter
#     displayboard(board)
#     if checkwin():
#         if letter=='X':
#             print('human won')
#             exit()
#         else:
#             print("computer wins")
#             exit()
#     if checkdraw():
#         print("Tied")
#         exit()
#
# def computerplayer(letter):
#     while True:
#         compmove = random.randint(0, 8)
#         if emptyspaces(compmove):
#             break
#     board[compmove] = letter
#     displayboard(board)
#     if checkwin():
#         if letter=='O':
#             print('computer won')
#             exit()
#         else:
#             print("human wins")
#             exit()
#     if checkdraw():
#         print("Tied")
#         exit()
#
# displayboard(board)
# while not checkwin():
#     userip=int(input('enter the position :'))
#     if board[userip]!=' ':
#         print('invalid move')
#         continue
#     humanplayer(userip,human)
#     computerplayer(computer)

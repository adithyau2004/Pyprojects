from tkinter import *
import random

def nextturn(row,column):
    global player

    if buttons[row][column]['text']=='' and checkwinner() is False:
        if player==players[0]:
            buttons[row][column]['text']=player
            if checkwinner() is False:
                player=players[1]
                label.config(text=(players[1]+' turn'))
            elif checkwinner() is True:
                label.config(text=(player[0]+' wins'))
            elif checkwinner() =='Tie':
                label.config(text='Tie')
        else:
            buttons[row][column]['text'] = player
            if checkwinner() is False:
                player = players[0]
                label.config(text=(players[0] + ' turn'))
            elif checkwinner() is True:
                label.config(text=(player[1] + ' wins'))
            elif checkwinner() == 'Tie':
                label.config(text='Tie')
def checkwinner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!='':
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True

    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!='':
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"]!='':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"]!='':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    elif emptyspaces()==False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return 'Tie'
    else:
        return False

def emptyspaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!='':
                spaces-=1
    if spaces==0:
        return False
    else:
        return True

def newgame():
    global player
    player= random.choice(players)
    label.config(text=player+' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='',bg='#F0F0F0')

window=Tk()
window.title('Tic Tac Toe')
players=['x','o']
player=random.choice(players)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
label=Label(text=player +' turn',font=('consolas',40))
label.pack(side='top')
resetbutton=Button(text='Restart',font=('consolas',20),command=newgame)
resetbutton.pack(side='top')

frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text='',font=('consolas',40),width=5,height=2,
                                    command=lambda row=row, column=column: nextturn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
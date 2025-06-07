from tkinter import *
import random

GAMEWIDTH=1000
GAMEHEIGHT=700
SPEED=50
SPACESIZE=25
BODYPARTS=3
SNAKECOLOUR='#00FF00'
FOODCOLOUR='#FF0000'
BACKGROUNDCOLOUR='#000000'

class Snake:
    def __init__(self):
        self.body=BODYPARTS
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODYPARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACESIZE,y+SPACESIZE,fill=SNAKECOLOUR,tag='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        x=random.randint(0,(GAMEWIDTH/SPACESIZE)-1)*SPACESIZE
        y = random.randint(0, (GAMEHEIGHT / SPACESIZE) - 1) * SPACESIZE
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACESIZE,y+SPACESIZE,fill=FOODCOLOUR,tag='food')

def nextturn(snake,food):
    x,y = snake.coordinates[0]
    if direction == 'up':
        y-=SPACESIZE
    elif direction == 'down':
        y+=SPACESIZE
    elif direction== 'left':
        x-=SPACESIZE
    elif direction=='right':
        x+=SPACESIZE

    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+SPACESIZE,y+SPACESIZE,fill=SNAKECOLOUR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text='Score:{}'.format(score))
        canvas.delete('food')
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkcollision(snake):
        gameover()
    else:
        window.after(SPEED,nextturn,snake,food)

def changedirection(newdirection):
    global direction
    if newdirection=='left':
        if direction!='right':
            direction=newdirection
    elif newdirection=='right':
        if direction!='left':
            direction=newdirection
    elif newdirection=='up':
        if direction!='down':
            direction=newdirection
    elif newdirection=='down':
        if direction!='up':
            direction=newdirection

def checkcollision(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=GAMEWIDTH:
        return True
    if y<0 or y>=GAMEHEIGHT:
        return True
    for bodypart in snake.coordinates[1:]:
        if x==bodypart[0] and y==bodypart[1]:
            return True
        else:
            False

def gameover():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=('consolas',70),text='GAME OVER',fill='red',tag='gameover')

window=Tk()
window.title('Snake game')
score=0
direction='down'
label=Label(window, text='Score:{}'.format(score), font={'consolas',40})
label.pack()
canvas =Canvas(window,bg=BACKGROUNDCOLOUR,height=GAMEHEIGHT,width=GAMEWIDTH)
canvas.pack()

window.bind('<Left>',lambda event: changedirection('left'))
window.bind('<Right>',lambda event: changedirection('right'))
window.bind('<Up>',lambda event: changedirection('up'))
window.bind('<Down>',lambda event: changedirection('down'))

snake=Snake()
food=Food()
nextturn(snake,food)
window.mainloop()
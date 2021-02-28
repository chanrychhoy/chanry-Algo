import tkinter as tk
import random
# CONSTANT
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

WINDOW_HEIGHT = 1000
WINDOW_WIDTH= 1000

CORONA_WIDTH=50
CORONA_HEIGHT=50
# GLOBAL VARIABLE
colors=["pink","orange","green","blue","yellow","purple","lime"]
# movement in x direction
dx=1
# movement in y direction
dy=0

# FUNCTIONS

def canMoveRight():
    postionPlayer = canvas.coords(playerId)
    x2 = postionPlayer[2]
    print(x2)
    return x2< WINDOW_WIDTH

def onKeyRight(event):
    global dx,dy
    if canMoveRight():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 10, 0)

def canMoveLeft():
    postionPlayer = canvas.coords(playerId)
    x1= postionPlayer[0]
    print(x1)
    return x1<WINDOW_WIDTH and x1!=0

def onKeyLeft(event):
    global dx,dy
    if canMoveLeft():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, -10, 0)

def canMoveUp():
    postionPlayer = canvas.coords(playerId)
    y1= postionPlayer[1]
    print(y1)
    return y1<WINDOW_HEIGHT and y1!=0

def onKeyUp(event):
    global dx,dy
    if canMoveUp():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 0, -10)

def canMoveDown():
    postionPlayer = canvas.coords(playerId)
    y2= postionPlayer[3]
    print(y2)
    return y2<WINDOW_HEIGHT 

def onKeyDown(event):
    global dx,dy
    if canMoveDown():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 0, 10)
# Monster
def Corona():
    canvas.move("Corona", 0,100)
def collisionCorona():
    coronaX=randfcom.randrange(0,1000)
    coronaY=0
    randomcolor = random.choice(colors)
    coronaId = canvas.create_rectangle(coronaX, coronaY, coronaX +CORONA_WIDTH,coronaY+CORONA_HEIGHT, fill=randomcolor, tags="Corona")
    canvas.after(50, lambda:Corona())
    canvas.after(1000, collisionCorona)

# GRAPHIC
windows = tk.Tk() 
windows.geometry(str(WINDOW_WIDTH) + "x"  +  str(WINDOW_HEIGHT))
canvas = tk.Canvas(windows)
# player
playerX = WINDOW_WIDTH/ 2
playerY = WINDOW_HEIGHT - 100 - PLAYER_HEIGHT
playerId = canvas.create_oval(playerX, playerY, playerX + PLAYER_WIDTH, playerY + PLAYER_HEIGHT, fill="red")
windows.bind("<Right>",onKeyRight)
windows.bind("<Left>",onKeyLeft)
windows.bind("<Up>",onKeyUp)
windows.bind("<Down>",onKeyDown)
# HERE YOU CAN START TO DRAW
canvas.pack(expand=True, fill='botftth')
collisionCorona()
windows.mainloop()      

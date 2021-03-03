import tkinter as tk
import random
from tkinter import messagebox
# CONSTANT
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

WINDOW_HEIGHT = 1000
WINDOW_WIDTH= 1000

CORONA_WIDTH=50
CORONA_HEIGHT=50

CANDY_WIDTH=40
CANDY_HEIGHT=40
# GLOBAL VARIABLE
colors=["pink","orange","green","blue","yellow","purple","lime"]
arrayCorona=[]
mybg=tk.PhotoImage(file="images.png")
canvas.create_image(0,0, anchor="nw", image=mybg)

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
    if canMoveRight():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 10, 0)

def canMoveLeft():
    postionPlayer = canvas.coords(playerId)
    x1= postionPlayer[0]
    print(x1)
    return x1<WINDOW_WIDTH and x1!=0

def onKeyLeft(event):
    if canMoveLeft():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, -10, 0)

def canMoveUp():
    postionPlayer = canvas.coords(playerId)
    y1= postionPlayer[1]
    print(y1)
    return y1<WINDOW_HEIGHT and y1!=0

def onKeyUp(event):
    if canMoveUp():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 0, -10)

def canMoveDown():
    postionPlayer = canvas.coords(playerId)
    y2= postionPlayer[3]
    return y2<WINDOW_HEIGHT 

def onKeyDown(event):
    if canMoveDown():
        postionPlayer = canvas.coords(playerId)
        canvas.move(playerId, 0, 10)

# candy
def moveCandy():
    canvas.move("moveCandy", 0,10)
    canvas.after(1000, lambda:moveCandy())
def createCandy():
    CandyX=random.randrange(0,1000)
    CandyY=0
    randomcolor = random.choice(colors)
    candyId = canvas.create_oval(CandyX, CandyY, CandyX +CANDY_WIDTH,CandyY+CANDY_HEIGHT, fill=randomcolor, tags="moveCandy")
    moveCandy()
    canvas.after(1000, createCandy)
# Monster

def moveCorona():
    # positionCovid=canvas.coords(createCorona())
    canvas.move("moveCorona", 0,10)
    canvas.after(300, lambda:moveCorona())
    
def createCorona():
    positioncorona = []
    coronaX=random.randrange(0,1000)
    coronaY=0
    randomcolor = random.choice(colors)
    coronaId = canvas.create_rectangle(coronaX, coronaY, coronaX +CORONA_WIDTH,coronaY+CORONA_HEIGHT, fill=randomcolor, tags="moveCorona")
    
    moveCorona()
    canvas.after(2000, createCorona)
    
# GRAPHIC
windows = tk.Tk() 
windows.geometry(str(WINDOW_WIDTH) + "x"  +  str(WINDOW_HEIGHT))
canvas = tk.Canvas(windows)

# player
playerX = WINDOW_WIDTH/ 2
playerY=WINDOW_HEIGHT-100
playerId = canvas.create_oval(playerX, playerY, playerX + PLAYER_WIDTH, playerY + PLAYER_HEIGHT, fill="red", tags="player")

windows.bind("<Right>",onKeyRight)
windows.bind("<Left>",onKeyLeft)
windows.bind("<Up>",onKeyUp)
windows.bind("<Down>",onKeyDown)
# HERE YOU CAN START TO DRAW
canvas.pack(expand=True, fill='both')
createCorona()
createCandy()
windows.mainloop()      

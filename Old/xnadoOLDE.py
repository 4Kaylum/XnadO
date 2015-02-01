2import random
import pygame, sys
from pygame.locals import *
import time

pygame.init()
winsurobj = pygame.display.set_mode((304,304))
pygame.display.set_caption("X and O")
boardobj = pygame.image.load('board.png')
xobj = pygame.image.load('x.png')
oobj = pygame.image.load('o.png')
xcur = pygame.image.load('xcur.png')
ocur = pygame.image.load('ocur.png')
fpsclock = pygame.time.Clock()

inSq=[" |"," |"," |",\
      " |"," |"," |",\
      " |"," |"," |"]
onSq=[(000,000),(101,000),(203,000),(000,101),(101,101),(203,101),(000,203),(101,203),(203,203)]

def clearLines(x):
    while x>0:
        print()
        x-=1

def inpVsNum(x):
    if x==7:
        return 0
    if x==8:
        return 1
    if x==9:
        return 2
    if x==4:
        return 3
    if x==5:
        return 4
    if x==6:
        return 5
    if x==1:
        return 6
    if x==2:
        return 7
    if x==3:
        return 8
    
def outSquare(inSq,x,onSq,xoro):
    y=0
    winsurobj.blit(boardobj,(0,0))
    if xoro == 'x':
        pygame.mouse.set_cursor((8,8),\
                                (0,0),\
                                (0,0,0,0,0,0,0,0),\
                                (0,0,0,0,0,0,0,0))
        winsurobj.blit(xcur, pygame.mouse.get_pos())
    else:
        pygame.mouse.set_cursor((8,8),\
                                (0,0),\
                                (0,0,0,0,0,0,0,0),\
                                (0,0,0,0,0,0,0,0))
        winsurobj.blit(ocur, pygame.mouse.get_pos())
    for item in inSq:
        if item=='X|':
            winsurobj.blit(xobj, onSq[y])
        if item=='O|':
            winsurobj.blit(oobj, onSq[y])
        y+=1
    pygame.display.update()

def endGame(x,letter):
    a=0
    for item in x:
        if item !=" |":
            a+=1
    if x[0]==letter and x[3]==letter and x[6]==letter or\
        x[1]==letter and x[4]==letter and x[7]==letter or\
        x[2]==letter and x[5]==letter and x[8]==letter or\
        x[0]==letter and x[1]==letter and x[2]==letter or\
        x[3]==letter and x[4]==letter and x[5]==letter or\
        x[6]==letter and x[7]==letter and x[8]==letter or\
        x[0]==letter and x[4]==letter and x[8]==letter or\
        x[2]==letter and x[4]==letter and x[6]==letter or\
        a==9:
        outSquare(inSq,0,onSq,'x')
        time.sleep(0.5)
        return True
    
def clickSquare(pos):
    #[0] = x;; [1] = y
    if pos[1] >= 0 and pos[1] < 101:
        if pos[0] >= 0 and pos[0] < 101:
            print("\n1,3")
            return inpVsNum(7)
        if pos[0] >= 101 and pos[0] < 203:
            print("\n2,3")
            return inpVsNum(8)
        if pos[0] >= 203:
            print("\n3,3")
            return inpVsNum(9)
    if pos[1] >= 101 and pos[1] < 203:
        if pos[0] >= 0 and pos[0] < 101:
            print("\n1,2")
            return inpVsNum(4)
        if pos[0] >= 101 and pos[0] < 203:
            print("\n2,2")
            return inpVsNum(5)
        if pos[0] >= 203:
            print("\n3,2")
            return inpVsNum(6)    
    if pos[1] >= 203:
        if pos[0] >= 0 and pos[0] < 101:
            print("\n1,1")
            return inpVsNum(1)
        if pos[0] >= 101 and pos[0] < 203:
            print("\n2,1")
            return inpVsNum(2)
        if pos[0] >= 203:
            print("\n3,1")
            return inpVsNum(3)

def playGame():
    play=True
    while play:
        outSquare(inSq,1,onSq,'x')
        while True:
            outSquare(inSq,0,onSq,'x')
            abcdef=False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    inp = clickSquare(pos)
                    abcdef=True
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_BACKSPACE:
                       oppon=True
                       break
            if abcdef==True:
                if inSq[inp]==" |":
                    inSq[inp]="X|"
                    print("Placed:",pos)
                    if endGame(inSq,"X|")==True:
                        oppon=False
                    else:
                        abcdef=False
                        oppon=True
                    break
        if endGame(inSq,"X|")==True:
            clearLines(50)
            play=False
            clearLines(2)
            outSquare(inSq,0,onSq,'o')
            time.sleep(0.5)
        outSquare(inSq,1,onSq,'o')
        while oppon==True:
            outSquare(inSq,0,onSq,'o')
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    inp = clickSquare(pos)
                    abcdef=True
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_BACKSPACE:
                       oppon=False
                       break
            if abcdef==True:
                if inSq[inp]==" |":
                    inSq[inp]="O|"
                    print("Placed:",pos)
                    if endGame(inSq,"O|")==True:
                        oppon=False
                    else:
                        oppon=False
                        abcdef=False
                    break
        if endGame(inSq,"O|")==True:
            clearLines(50)
            play=False
            clearLines(2)
            outSquare(inSq,0,onSq,'o')
            time.sleep(0.5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        fpsclock.tick(30)

while True:
    inSq=[" |"," |"," |"," |"," |"," |"," |"," |"," |"]
    winsurobj.blit(boardobj,(0,0))
    clearLines(50)
    playGame()
    pygame.init()

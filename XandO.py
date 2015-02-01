import random, pygame, sys, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("X and O")

winsurobj = pygame.display.set_mode((304,304))
boardobj  = pygame.image.load('board.png')
xobj      = pygame.image.load('x.png')
oobj      = pygame.image.load('o.png')
xcur      = pygame.image.load('xcur.png')
ocur      = pygame.image.load('ocur.png')
fpsclock  = pygame.time.Clock()

inSq = [\
0 , 0 , 0 ,\
0 , 0 , 0 ,\
0 , 0 , 0  ]
# 1 = X
# 2 = O

dimenstions = (3,3)
winningRange = 3
lst = 'lst'
xy = 'xy'
rul = [0,101,202]
inpVsNum = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}

def getMouse(turn):
	groot = 0
	waitforMouse = True
	while waitforMouse:
		outSquare(inSq,turn)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				waitforMouse = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					groot = 1
					waitforMouse = False
	if groot == 0:
		xpos=0
		ypos=0
		checknum=0
		for item in rul:
			if pos[0] >= item:
				xpos=checknum
			if pos[1] >= item:
				ypos=checknum
			checknum += 1
		return (xpos,ypos)
	else:
		return 1

def winningMoves(i):
	wins = [ [] , [] , [] , [] ]
	i = ordFromNum(i,'xy')
	# print i
	xLimit = i[0] + winningRange - 1
	yLimit = i[1] + winningRange - 1
	xMax = dimenstions[0] ## 3
	yMax = dimenstions[1] ## 3
	xGrid = i[0]
	yGrid = i[1]

	for cha in range(winningRange):
		if xLimit < xMax and xLimit >= 0:
			wins[0].append( ( cha + xGrid , yGrid ) )
		if yLimit < yMax and yLimit >= 0:
			wins[1].append( ( xGrid , cha + yGrid ) )
		if xLimit < xMax and xLimit >= 0 and yLimit < yMax and yLimit >= 0: #Diag topLeft to botRight
			wins[2].append( ( cha + xGrid , cha + yGrid ) )
		if i[0] - winningRange + 1 >= 0 and i[0] - winningRange + 1 < xLimit and yLimit < yMax and yLimit >= 0: #Diag topRight to botLeft
			wins[3].append( ( xGrid - cha , yGrid + cha ) )		
	return wins

def endGame(inSq,letter):
	a=0
	oopslivon = False
	for item in inSq: 
		if item != 0:
			a+=1
	if a==9:
		oopslivon = True
	for i in range(len(inSq)):
		for item in winningMoves(i):
			xy = 0
			for win in item:
				try:
					if inSq[ordFromNum(win,'lst')] == letter:
						xy += 1
				except:
					pass
			if xy == 3:
				oopslivon = True
	if oopslivon == True:
		outSquare(inSq,1)
		time.sleep(0.5)
		return True

def outSquare(inSq,xoro):
    chk = 0
    winsurobj.blit(boardobj,(0,0))
    if xoro == 1:
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
        if item == 1 :
            winsurobj.blit(xobj, ordFromNum(chk,'xy',1))
        if item == 2 :
            winsurobj.blit(oobj, ordFromNum(chk,'xy',1))
        chk += 1
    pygame.display.update()

def ordFromNum(n,a,r=0):
	x = n
	if a == 'lst' and type(n) == tuple:
		x = n[0]
		x += n[1]*3
	if a == 'xy' and type(n) == int:
		if r == 1:
			x = (rul[n%3],rul[int(n/3)])
		else:
			x = (n%3,int(n/3))
	return x

def checkEmpty(inSq,coOrds,turn):
	coOrds = ordFromNum(coOrds,lst)
	if inSq[coOrds] == 0:
		inSq[coOrds] = turn
		return inSq
	else:
		return False

while True:
	inSq=[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
	while True:

		xTurn = True
		while xTurn:
			pos = getMouse(1)
			if pos == 1:
				break
			temp = checkEmpty(inSq,pos,1)
			if temp == False:
				pass
			else:
				inSq = temp
				xTurn = False
		if pos == 1:
			break
		if endGame(inSq,1):
			break

		oTurn = True
		while oTurn:
			pos = getMouse(2)
			if pos == 1:
				break
			temp = checkEmpty(inSq,pos,2)
			if temp == False:
				pass
			else:
				inSq = temp
				oTurn = False
		if pos == 1:
			break
		if endGame(inSq,2):
			break


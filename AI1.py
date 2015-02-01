import random
import XandO as xo 

# inSq = 
# dimenstions = xo.dimenstions
# winningRange = xo.winningRange
lst = 'lst'
xy = 'xy'
pieceID = 2

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

## Finds all of the pieces on the board that belong to the AI
def findPieces(grid,pieceID):
	myPiece = []
	for item in grid:
		if item == pieceID:
			myPiece.append(ordFromNum(item,'xy'))
	return myPiece

## Looks at the current pieces and returns where else they can go
## so that they win.
def whereWin(myPieces):
	whereToWin = []
	for item in myPieces:
		whereToWin.append(winningMoves(item))
	return whereToWin

## Finds all the possible routes for winning.
def possRoute(myPieces,whereToWin):
	y = []
	for item in whereToWin:
		x = 0
		for i in myPieces:
			if i in item:
				x += 1
		if x == 2:
			y.append(item)
	return y

## Checks to see if any given space is empty
def checkEmpty(inSq,coOrds,turn):
	coOrds = ordFromNum(coOrds,lst)
	if inSq[coOrds] == 0:
		inSq[coOrds] = turn
		return inSq
	else:
		return False

## Checks to see if any of the spaces in the notable moves are empty
## If they are, it returns said space
def notableEmpty(y):
	pl = False
	for item in y:
		for x in item:
			if pl == False:
				if bool(checkEmpty(inSq,x,pieceID)) == True:
					pl = x
	return pl

def whereToGo(inSq):
	myPieces = findPieces(xo.inSq,pieceID) ## See where my pieces are
	whereToWin = whereWin(myPieces) ## See where those pieces can win
	possible = possRoute(myPieces,whereToWin) ## See if I can win at the moment
	nota = notableEmpty(possible) ## I CAN WIN PUT IT HERE (or false)

	if nota:
		return checkEmpty(inSq,nota,pieceID)
	else:
		while True:
			x = checkEmpty(inSq,ordFromNum(random.randint(0,len(inSq)-1),'xy'),pieceID)
			if x == True:
				return x
				break


'''

* Block opposing moves
	* Scan board for moves that they can win
	* Add one to the end so they can't score 
* Make suitable own moves
	* Scan the board for moves that they can win 
	* Add on the the end so they can score 
* If no suitable move can be made, pick randomly 
	* checkEmpty( Random.randint( 0, len(grid)-1 ) )

'''
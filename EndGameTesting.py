inSq=[ 0 , 0 , 0 ,\
	   0 , 0 , 0 ,\
	   0 , 0 , 0 ]

dimenstions = (3,3)
winningRange = 3

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

	# for x in range(winningRange):
	# 	if winP <= dimenstions[0] and winP > 0:
	# 		wins[0].append( (i+x,0) )
	# 	if winP <= dimenstions[1] and winP > 0:
	# 		wins[1].append( (0,i+x) )
	# 	if winP <= dimenstions[0] and winP <= dimenstions[1] and winP > 0:
	# 		wins[2].append( (i+x,i+x) )
	# 	if winM <= dimenstions[0] and winM <= dimenstions[1] and winM > 0:
	# 		wins[3].append( (i+x,i+x) )

	# for cha in range(winningRange):

	# 	## Maximum value that it can be.
	# 	z = winningRange + i - 1 ## Range-1 because that's what the for loop does

	# 	## if z < x makes sure that the character stays in the square.
	# 	if z < x and z >= 0:
	# 		wins[0].append( (cha + i) )

	print wins
	return wins

	# return [ [ (i,0)  ,  (i+1,0)  ,  (i+2,0) ]   , \
	#          [ (0,i)  ,  (0,i+1)  ,  (0,i+2) ]   , \
	#          [ (i,i)  ,  (i+1,i+1),  (i+2,i+2) ] , \
	#          [ (i,i)  ,  (i-1,i-1),  (i-2,i-2) ]   ]

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

endGame(inSq,1)
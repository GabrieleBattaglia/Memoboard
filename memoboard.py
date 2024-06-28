# MEMOBOARD - Your helper to play chess without a chessboard.
# Born on monday, may 6th, 2024 by Gabriele Battaglia IZ4APU.
# June 28th, 2024: moved on Github

#QI
from GBUtils import key, dgt, menu, manuale
import time, datetime, random

# CONST
VER="1.0.1, May 2024"
STARTTIME=time.time()

#variables
mnu={"quit":"to quit the app",
					"help":"to read instruction on MemoBoard",
					"menu":"to read this menu",
					"knights":"Execise with knights",
					"bishops":"Exercise with diagonals",
					"colors":"This square is white or black?",
					"test":"Take your test on all skills!"}
log=open("memoboard.txt","t+a")
log.write(f"# {time.asctime()} Hello, Memoboard {VER} starts.")
board=set()
for y in "12345678":
	for x in "ABCDEFGH":
		board.add(f"{x}{y}")
columns={"A":"Alpha",
									"B":"Bravo",
									"C":"Charlie",
									"D":"Delta",
									"E":"Echo",
									"F":"Foxtrot",
									"G":"Golf",
									"H":"Hotel"}
blacks=set()
for y in "1357":
	for x in "ACEG":
		blacks.add(f"{x}{y}")
for y in "2468":
	for x in "BDFH":
		blacks.add(f"{x}{y}")
whites=board-blacks
board=list(board); blacks=list(blacks); whites=list(whites)
diagonals={'A1H8':['A1','B2','C3','D4','E5','F6','G7','H8'],
											'B1H7':['B1','C2','D3','E4','F5','G6','H7'],
											'C1H6':['C1','D2','E3','F4','G5','H6'],
											'D1H5':['D1','E2','F3','G4','H5'],
											'E1H4':['E1','F2','G3','H4'],
											'F1H3':['F1','G2','H3'],
											'G1H2':['G1','H2'],
											'B1A2':['B1','A2'],
											'C1A3':['C1','B2','A3'],
											'D1A4':['D1','C2','B3','A4'],
											'E1A5':['E1','D2','C3','B4','A5'],
											'F1A6':['F1','E2','D3','C4','B5','A6'],
											'G1A7':['G1','F2','E3','D4','C5','B6','A7'],
											'H1A8':['H1','G2','F3','E4','D5','C6','B7','A8']}

def Prox(sq, kind, range):
	'''square proximity
	rx a square, kind and a range, it returns another square which is in its proximity
	kind could be "B" for bishop or other for knights exercise'''
	x,y=ord(sq[0])-64,ord(sq[1])-48
	x1,x2=x-range,x+range
	if x1<1: x1=1
	if x2>8: x2=8
	y1,y2=y-range,y+range
	if y1<1: y1=1
	if y2>8: y2=8
	while True:
		psq=chr(random.randint(x1,x2)+64)+chr(random.randint(y1,y2)+48)
		check=False
		if kind=="B":
			found=[]
			for k,v in diagonals.items():
				if sq in v: found.append(k)
			for j in found:
				if psq in diagonals[j]: check=True
		else:
			xsq=ord(sq[0]); ysq=ord(sq[1])
			xpsq=ord(psq[0]); ypsq=ord(psq[1])
			if xpsq==xsq-2 and ypsq==ysq-1: check = True
			elif xpsq==xsq-1 and ypsq==ysq-2: check = True
			elif xpsq==xsq+1 and ypsq==ysq-2: check = True
			elif xpsq==xsq+2 and ypsq==ysq-1: check = True
			elif xpsq==xsq+2 and ypsq==ysq+1: check = True
			elif xpsq==xsq+1 and ypsq==ysq+2: check = True
			elif xpsq==xsq-1 and ypsq==ysq+2: check = True
			elif xpsq==xsq-2 and ypsq==ysq+1: check = True
		if not check and (sq[0]!=psq[0] and sq[1]!=psq[1]): break
	return psq
def ExKnights(ripetitions):
	'''Exercise on knights
	returns score,scoreslist,duration,timeslist,wins'''
	score=0; wins=0; scoretime=15
	timeex=time.time()
	timeslist=[]
	scoreslist=[]
	while ripetitions>0:
		sq1=random.choice(board)
		yes=random.choice([True,False])
		if not yes: sq2=Prox(sq1,'N',2)
		else:
			x=ord(sq1[0])-64; y=ord(sq1[1])-48
			while True:
				x1=x+random.choice([-2,-1,1,2])
				y1=y+random.choice([-2,-1,1,2])
				if x1>=1 and y1>=1 and x1<=8 and y1<=8: break
			sq2=f"{chr(x1+64)}{chr(y1+48)}"
		print(f"{columns[sq1[0]]} {sq1[1]} and {columns[sq2[0]]} {sq2[1]}")
		time.sleep(.8)
		now=time.time()
		s=key().lower()
		singlescore = (scoretime*1000)-(time.time()-now)*1000
		if singlescore<0: singlescore=0
		if s=="y" and yes:
			wins+=1
			score+=singlescore
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
		elif s=="n" and not yes:
			wins+=1
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
			score+=singlescore
		ripetitions-=1
	duration=time.time()-timeex
	return score,scoreslist,duration,timeslist,wins

def ExBishops(ripetitions):
	'''Exercise on bishops
	returns score,scoreslist,duration,timeslist,wins'''
	score=0; wins=0; scoretime=15
	timeex=time.time()
	timeslist=[]
	scoreslist=[]
	while ripetitions>0:
		kd=random.choice(list(diagonals.keys()))
		sq1=random.choice(diagonals[kd])
		yes=random.choice([True,False])
		if not yes: sq2=Prox(sq1,'B',3)
		else:
			while True:
				sq2=random.choice(diagonals[kd])
				if sq1!=sq2: break
		print(f"{columns[sq1[0]]} {sq1[1]} and {columns[sq2[0]]} {sq2[1]}")
		time.sleep(.8)
		now=time.time()
		s=key().lower()
		singlescore = (scoretime*1000)-(time.time()-now)*1000
		if singlescore<0: singlescore=0
		if s=="y" and yes:
			wins+=1
			score+=singlescore
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
		elif s=="n" and not yes:
			wins+=1
			score+=singlescore
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
		ripetitions-=1
	duration=time.time()-timeex
	return score,scoreslist,duration,timeslist,wins

def ExColors(ripetitions):
	'''Exercise on colorss
	returns score,scoreslist,duration,timeslist,wins'''
	score=0; wins=0; scoretime=15
	timeex=time.time()
	timeslist=[]
	scoreslist=[]
	while ripetitions>0:
		sq=random.choice(board)
		print(f"{columns[sq[0]]} {sq[1]} ")
		time.sleep(.8)
		now=time.time()
		s=key().lower()
		singlescore = (scoretime*1000)-(time.time()-now)*1000
		if singlescore<0: singlescore=0
		if s=="w" and sq in whites:
			wins+=1
			score+=singlescore
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
		elif s=="b" and sq in blacks:
			wins+=1
			score+=singlescore
			scoreslist.append(singlescore)
			timeslist.append(time.time()-now)
		ripetitions-=1
	duration=time.time()-timeex
	return score,scoreslist,duration,timeslist,wins
#QM
print(f"Welcome to MemoBoard.\nYour helper to play chess without chessboard.\nThis utility helps you to manage your chessboard and to become a better chess player.\n\tby Gabriele Battaglia (IZ4APU). Version {VER}.\n\t\tType 'help' or 'menu'.")
while True:
	s=menu(d=mnu, ntf="Command not found", show=False, keyslist=True)
	if s=="quit": break
	elif s=="colors":
		print("Guess the square color.\n Please answer by pressing B for black and W for white.")
		rpt=dgt(prompt="\nNice and good luck with colors, how many guesses you want to take? ",kind="i",imin=5,imax=150)
		wait=key(prompt="Go?")
		print(" Start")
		log.write(f"\n## Single exercise on square color:")
		score,scoreslist,duration,timeslist,wins=ExColors(rpt)
		print(f"You've got {score:.0f} points over {wins} guessed out of {rpt}.")
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
	elif s=="knights":
		print("Guess if these two squares are on a knight's jump.\n Please answer by pressing Y for yes and N for no.")
		log.write(f"\n## Single exercise on knight's jump:")
		rpt=dgt(prompt="\nGood and have fun with knight's jump, how many guesses you want to take? ",kind="i",imin=5,imax=150)
		wait=key(prompt="Go?")
		print(" Start")
		score,scoreslist,duration,timeslist,wins=ExKnights(rpt)
		print(f"You've got {score:.0f} points over {wins} guessed out of {rpt}.")
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
	elif s=="bishops":
		print("Guess if these two squares are on the same diagonal.\n Please answer by pressing Y for yes and N for no.")
		log.write(f"\n## Single exercise on bishop's move:")
		rpt=dgt(prompt="\nGood and have fun with Bishop's exercise, how many guesses you want to take? ",kind="i",imin=5,imax=150)
		wait=key(prompt="Go?")
		print(" Start")
		score,scoreslist,duration,timeslist,wins=ExBishops(rpt)
		print(f"You've got {score:.0f} points over {wins} guessed out of {rpt}.")
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
	elif s=="help": manuale(nf="README.md")
	elif s=="menu": menu(d=mnu,show=True)
	elif s=="test":
		totalduration,totalscore=0,0
		totaltimeslist=[]; totalscoreslist=[]; totalwins=0
		print("Welcome to the SUPER TEST of this application\nHere you will test on all the Memoboard skills. Have a great job.")
		log.write(f"\n## SUPER TEST on all skills:\n\tSquare colors")
		print("Let's begin with colors. Are you ready for 25 guesses? Again B for black and W for white.")
		rpt=25
		wait=key(prompt="Go?")
		score,scoreslist,duration,timeslist,wins=ExColors(rpt)
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
		totalduration+=duration
		totalscore+=score
		totaltimeslist.extend(timeslist)
		totalscoreslist.extend(scoreslist)
		totalwins+=wins
		print("Good! And now it's knight's time, 25 rounds. Again Y for yes and N for no.")
		log.write(f"\n\tKnight's jump")
		wait=key(prompt="Go?")
		score,scoreslist,duration,timeslist,wins=ExKnights(rpt)
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
		totalduration+=duration
		totalscore+=score
		totaltimeslist.extend(timeslist)
		totalscoreslist.extend(scoreslist)
		totalwins+=wins
		print("Great! now it's bishops time. Y for yes and N for no.")
		log.write(f"\n\tBishops")
		wait=key(prompt="Go?")
		score,scoreslist,duration,timeslist,wins=ExBishops(rpt)
		log.write(f"\nYou've got {wins} right out of {rpt} in {duration:.1f} seconds")
		log.write(f"\nYou scored {score:.0f} points: max {max(scoreslist):.0f}, ave {score/rpt:.0f}, min {min(scoreslist):.0f}")
		log.write(f"\nYour times: max {max(timeslist):.1f}, ave {duration/rpt:.1f}, min {min(timeslist):.1f} secs")
		totalduration+=duration
		totalscore+=score
		totaltimeslist.extend(timeslist)
		totalscoreslist.extend(scoreslist)
		totalwins+=wins
		print("SUPER! And now the most difficult one: the mixed exercise.\nBe ready to answer all 3 kinds of questions. B and W for colors and Y and N for knights and bishops.")
		wait=key(prompt="Go?")
		mul=1.33; testtimes=[]; testscores=[]; testwins=0; testduration=0; testscore=0
		for j in range(1,rpt+1):
			sel=random.choice([1,2,3])
			if sel==1:
				print("Color")
				score,scoreslist,duration,timeslist,wins=ExColors(1)
				totalduration+=duration
				testduration+=duration
				totalscore+=score*mul
				testscore+=score*mul
				totaltimeslist.extend(timeslist)
				totalscoreslist.extend(scoreslist)
				totalwins+=wins
				testtimes.extend(timeslist)
				testscores.extend(scoreslist)
				testwins+=wins
			elif sel==2:
				print("Knights")
				score,scoreslist,duration,timeslist,wins=ExKnights(1)
				totalduration+=duration
				testduration+=duration
				totalscore+=score*mul
				testscore+=score*mul
				totaltimeslist.extend(timeslist)
				totalscoreslist.extend(scoreslist)
				totalwins+=wins
				testtimes.extend(timeslist)
				testscores.extend(scoreslist)
				testwins+=wins
			elif sel==3:
				print("Bishops")
				score,scoreslist,duration,timeslist,wins=ExBishops(1)
				totalduration+=duration
				testduration+=duration
				totaltimeslist.extend(timeslist)
				totalscoreslist.extend(scoreslist)
				totalwins+=wins
				totalscore+=score*mul
				testscore+=score*mul
				testtimes.extend(timeslist)
				testscores.extend(scoreslist)
				testwins+=wins
		print("Wonderful! Well done! The report will be saved on memoboard.txt after you close this app.")
		print(f"You ended up with {totalscore:.0f} points over {totalwins} guessed out of 100.")
		log.write(f"\n\tMixed SUPER TEST RESULTs are\nGuessed {testwins} right out of 25 in {testduration:.1f} seconds")
		log.write(f"\nYou scored {testscore:.0f} points: max {max(testscores):.0f}, ave {testscore/25:.0f}, min {min(testscores):.0f}")
		log.write(f"\nYour times: max {max(testtimes):.1f}, ave {testduration/25:.1f}, min {min(testtimes):.1f} secs")
		log.write(f"\n\tGLOBAL SUPER TEST RESULTs are\nTotal guessed {totalwins} right out of 100 in {totalduration:.1f} seconds")
		log.write(f"\nYour global score is {totalscore:.0f} points: max {max(totalscoreslist):.0f}, ave {totalscore/100:.0f}, min {min(totalscoreslist):.0f}")
		log.write(f"\nYour overall times are: max {max(totaltimeslist):.1f}, ave {totalduration/100:.1f}, min {min(totaltimeslist):.1f} secs")
endtime=time.time()-STARTTIME
print(f"\nMemoboard {VER}, ran for {int(endtime/60)} minutes and {int(endtime%60)} seconds.\n\tPlease check memoboard.txt Bye-Bye")
log.write(f"\n### Goodbye from Memoboard {VER}, it ran for {int(endtime/60)} minutes and {int(endtime%60)} seconds.\n")
log.close()
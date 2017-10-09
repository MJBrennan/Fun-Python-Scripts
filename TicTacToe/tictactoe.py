



def tictactoe():
	
	arr = [["","",""],["","",""],["","",""]]
	gamewon = False
	movecounter = 0
	currentplayer = "X"
	tempstring1 = ""
	tempstring2 = ""
	#Enter Cooridates

	while(gamewon == False):

		print("Enter Move Coordinates:")
		move1 = input()
		resarr = move1.split(',')
		
		num1 = int(resarr[0])
		num2 = int(resarr[1])

		num1 = num1 - 1
		num2 = num2 - 1

		arr[num1][num2] = currentplayer
		print("Current Standings:")
		for i in range(0,3):
			print(arr[i])

		#Check if there is a winner

		playerone = "XXX"
		playertwo = "YYY"

		for i in range(0,2):

			if(currentplayer == "X"):
				tempstring1 += ''.join(arr[i])
			else:
				tempstring2 += ''.join(arr[i])

		if(currentplayer == "X"):

			if(playerone in tempstring1):
				gamewon = True
				return print( currentplayer + " is the winner")


		if(currentplayer == "Y"):

			if(playertwo in tempstring2):
				gamewon = True
				return print( currentplayer + " is the winner")


		if(all(arr[0]) == True and all(arr[1]) == True and all(arr[2]) == True):
			return print ("Game is a draw")

		if(currentplayer == "X"):
			currentplayer = "Y"
		else:
			currentplayer = "X"

		tempstring1 = ""
		tempstring2 = ""

if __name__ == '__main__':
	tictactoe()





#left to right

	#line 2

	#get up and down
	'''
	arr[0][0]
	arr[1][0]
	arr[2][0]

	arr[0][1]
	arr[1][1]
	arr[2][1]

	arr[0][2]
	arr[1][2]
	arr[2][2]

	#diagnoal left
	arr[0][0]
	arr[1][1]
	arr[2][2]

	#diagonal right
	arr[0][2]
	arr[1][1]
	arr[2][0]
	'''


	#Check if its a draw

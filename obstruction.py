import random	#imports the random module	
import os 		#imports the os module

NUM_PLAYERS=2	#constant for number of players
NUM_ROWS=6			#constant for number of rows in board
NUM_COLS=6		#constant for number of columns in board
CHECKERS=["O","X"]      #list for CHECKERS
GREY="#"
board=[]		
top_row=[]		
checked_cells=0	
x=1				             

if 0<NUM_ROWS<10 and 0<NUM_COLS<10 and NUM_ROWS*NUM_COLS>=16:          #condition for board dimensions restriction
	
	for i in range(NUM_ROWS):           #creating the board
		row_list=[]
		for j in range(NUM_COLS):
			row_list.append(" ")
		board.append(row_list)
	print("   ", end=" ")			

	for j in range(NUM_COLS):		
		print (chr(65+j), end="   ")
	print()
	print("  "+"+---"*NUM_COLS+"+")

	for i in range(NUM_ROWS):			#printing the board
		if i<10:
			print (i, end=" ")
		else:
			print (i, end="")
		for j in range(NUM_COLS):
			print ("|"+board[i][j],end="  ")
		print("|")
		print("  "+"+---"*NUM_COLS+"+")

	first_turn=random.randint(0, NUM_PLAYERS-1)					   #choosing the first player randomly

	while checked_cells<NUM_ROWS*NUM_COLS:                             
		if first_turn==0:                                          
			current_player=input("Player O wants to place O on: ")
			d=0														
		elif first_turn==1:
			current_player=input("Player X wants to place X on: ")
			d=1
		while x!= 0:  								#initial value of x is 1                                        		
		#checking multiple conditions for input 
			if current_player!="" and current_player[1:].isdigit() and 65<=ord(current_player[0].upper())<NUM_COLS+65 and 0<=int(current_player[1:])<NUM_ROWS and board[int(current_player[1:])][ord(current_player[0].upper())-65]==" ":
				first_string=ord(current_player[0].upper())
				second_string=int(current_player[1])
				x=0                                 #while loop ends
			else:
				print("Invalid input."+\
				 "Try again with a valid input(unchecked cells within the board range) and valid form(letter followed by number) .")
				current_player=input("Player "+CHECKERS[d]+ " wants to place "+CHECKERS[d]+ " on: ")

		if second_string==0 and first_string==65:               #for topmost left corner
			board[second_string][first_string-65]=CHECKERS[d]
			if second_string+1<NUM_ROWS:	
				board[second_string+1][first_string-65]=GREY
			if first_string-64<NUM_COLS:
				board[second_string][first_string-64]=GREY
			if second_string+1<NUM_ROWS and first_string-64<NUM_COLS:
				board[second_string+1][first_string-64]=GREY

		elif second_string==0 and first_string-65==NUM_COLS-1:         #for topmost right corner
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string][first_string-66]=GREY
			if second_string+1<NUM_ROWS:
				board[second_string+1][first_string-65]=GREY
				board[second_string+1][first_string-66]=GREY

		elif second_string==(NUM_ROWS-1) and first_string==65:         #for lowermost left corner
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string-1][first_string-65]=GREY
			if first_string-64<NUM_COLS:
				board[second_string][first_string-64]=GREY
				board[second_string-1][first_string-64]=GREY

		elif second_string==(NUM_ROWS-1) and first_string-65==NUM_COLS-1:    #for lowermost right corner
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string][first_string-66]=GREY
			board[second_string-1][first_string-65]=GREY
			board[second_string-1][first_string-66]=GREY

		elif second_string==0:                                        #for first row cells in the board
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string][first_string-66]=GREY
			if first_string-64<NUM_COLS:
				board[second_string][first_string-64]=GREY
			if second_string+1<NUM_ROWS:
				board[second_string+1][first_string-65]=GREY
				board[second_string+1][first_string-66]=GREY
				board[second_string+1][first_string-64]=GREY

		elif second_string==(NUM_ROWS-1):                                 #for last row cells in the board
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string-1][first_string-65]=GREY
			board[second_string-1][first_string-66]=GREY
			board[second_string-1][first_string-64]=GREY
			board[second_string][first_string-64]=GREY
			board[second_string][first_string-66]=GREY

		elif first_string==65:                                       #for first column cells in the board
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string-1][first_string-65]=GREY
			board[second_string+1][first_string-65]=GREY
			if first_string-64<NUM_COLS:
				board[second_string][first_string-64]=GREY
				board[second_string-1][first_string-64]=GREY
				board[second_string+1][first_string-64]=GREY

		elif first_string-65==NUM_COLS-1:                             #for last column cells in the board
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string-1][first_string-65]=GREY
			board[second_string-1][first_string-66]=GREY
			board[second_string][first_string-66]=GREY
			if second_string+1<NUM_ROWS:
				board[second_string+1][first_string-65]=GREY
				board[second_string+1][first_string-66]=GREY	
		else:                                                         #for every other cells in the board except above
			board[second_string][first_string-65]=CHECKERS[d]
			board[second_string-1][first_string-65]=GREY
			board[second_string+1][first_string-65]=GREY
			board[second_string-1][first_string-66]=GREY
			board[second_string][first_string-66]=GREY
			board[second_string+1][first_string-66]=GREY
			board[second_string-1][first_string-64]=GREY
			board[second_string+1][first_string-64]=GREY
			board[second_string][first_string-64]=GREY
		os.system("clear")
		print("   ", end=" ")	
		for j in range(NUM_COLS): 								#printing the topmost row of alphabets
			print (chr(65+j), end="   ")
		print()
		print("  "+"+---"*NUM_COLS+"+")
		
		for i in range(NUM_ROWS):								#printing the updated board after the checker is placed
			print (i, end=" ")
			for j in range(NUM_COLS):
				print ("|"+board[i][j],end="  ")
			print("|")
			print("  "+"+---"*NUM_COLS+"+")
		for i in range(NUM_ROWS):                          		
			for j in range(NUM_COLS):
				if board[i][j]!= " ":							#checking how many cells are not empty 
					checked_cells=checked_cells+1     			        
		if checked_cells==NUM_ROWS*NUM_COLS:                	#declaraing the winner if all cells are checked
			print ("Player "+CHECKERS[d]+ " wins the game!!!")
		else:                                           
			checked_cells=0                          
			x=1
		if d==0:                 								 #alternating turns for the users
			first_turn=1
		else:
			first_turn=0			
else:
	print("Please make sure the number of cells is between 4X4 and 9X9. Sorry for inconvenience!")







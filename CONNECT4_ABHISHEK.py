import random    #imports random module
import os        #imports os module
import time      #imports time module

NUM_ROWS = 6      # constant variable for number of rows

NUM_COLUMNS = 7   # constant variable for number of columns

NUM_PLAYERS = 2  # constant variable for number of players 

#function to create a board with using constant rows and constant columns
def create_board():
    board=[]
    for r in range(NUM_ROWS):
        row=[]  
        for c in range(NUM_COLUMNS):
            row.append(' ')
        board.append(row)   
    return board

#function to display the board with using constant rows and constant columns
def display_board(board):
    for column in range(NUM_COLUMNS): 
        print('   ' + chr(65+column), end='')   
    print('\n +' + '---+'*NUM_COLUMNS)    
    for row in range(NUM_ROWS):
        print(' | ', end='')
        for column in range(NUM_COLUMNS):
            print(board[row][column] + ' | ', end='')  
        print("\n +"+"---+"*NUM_COLUMNS)


#function to check the win condition in the game with using board and player symbol in all cases 
def check_win_condition(board,player_symbol):
    
    # Checking each win case i.e horizontal, vertical, and both diagonal win 
    
    
    # for the the horizontal win check
    for row in range(NUM_ROWS):
        count = 0                                   #initializing the count to 0
        for col in range(NUM_COLUMNS):
            if board[row][col] == player_symbol:    #checking the player symbol in the board
                count += 1                          #increasing  the count if the symbol is found
                if count == 4:                      #if the count reaches 4 win condition is met
                    return True
            else:                                   #if the symbol is not found then reset the counter
                count = 0                        


    # loop for the Vertical win check
    for col in range(NUM_COLUMNS):
        count = 0                                      #initializing the count to 0
        for row in range(NUM_ROWS):
            if board[row][col] == player_symbol:      #checking the player symbol in the board 
                count += 1                            #increasing  the count if the symbol is found
                if count == 4:                        #if the count reaches 4 win condition is met
                    return True
            else:                                     #if the symbol is not found then reset the counter
                count = 0

    #WIN CHECK FOR DIAGONAL CASES
    
    # Diagonal check in the (\ direction)
    for row in range(NUM_ROWS - 3):                   #The loop will start from row 0 to 2
        for col in range(NUM_COLUMNS - 3):            #The loop will start from columns 0 to 3
            count = 0
            for i in range(4):                        # Checking 4 cells diagonally down to right
                if board[row + i][col + i] == player_symbol:   #checking the player symbol in the board
                    count += 1                        
                    if count == 4:                    #if the count reaches 4 win condition is met
                        return True
                else:
                    count = 0                         # Reset counter if the sequence is broken

    # Diagonal check in the (/ direction)
    for row in range(NUM_ROWS - 3):                   #The loop will start from row 0 to 2
        for col in range(3, NUM_COLUMNS):             #The loop will start from columns 0 to 3
            count = 0
            for i in range(4):                        # Checking 4 cells diagonally down to right
                if board[row + i][col - i] == player_symbol:    #checking the player symbol in the board
                    count += 1
                    if count == 4:                   #if the count reaches 4 win condition is met
                        return True
                else:
                    count = 0                         # Reset counter if the sequence is broken
    
    return False                            # Return False if no win condition is found


#Checking for the draw condition in the game
def check_draw_condition(board):          
    for col in range(NUM_COLUMNS):
        if board[0][col] == ' ':
            return False
    return True


board=create_board()
display_board(board)

# Randomly select a player to start the game
turn = random.randint(1, NUM_PLAYERS)

#Assigning the player symbols to the players
player_sign_dict = {1: 'X', 2: 'O', 3: 'V', 4: 'H', 5: 'M'}

#Assuming initial the game to be not over
game_over = False       

#Main game loop
while game_over==False:
    
    #Asking the player to the input the column to place their symbol
    player_symbol= player_sign_dict[turn]
    player_input= input("Player "+player_symbol+", Plz enter a column: ")
    
    
    #Checking the input of the player met our conditions or not
    if len(player_input) == 1 and player_input.isalpha() and 'A' <= player_input <= chr(65 + NUM_COLUMNS - 1):
        
        #Converting the input to the column number
        column = ord(player_input.upper()) - 65       
        
        #If the column is full then the player losing their turn
        if board[0][column] != ' ':
            print("Column "+ player_input+ " is full. User loses their turn.")
            time.sleep(1)           #Wait for 1 second
            os.system('clear') 
            display_board(board)    #Display the board after losing the turn
            turn = (turn % NUM_PLAYERS) + 1     #Passing the turn to the next player
        
        else:                         #If the column is not full then place the symbol in the column

            
            for row in range(NUM_ROWS - 1, -1, -1):
                if board[row][column] == ' ':
                    board[row][column] = player_symbol
                    break             #Break the loop after placing the symbol in the column
            

            os.system('clear')  #Clear the screen after placing the symbol
            display_board(board)       #Display the board after placing the symbol and calling the function



            #Checking the win condition and draw condition after placing the symbol and calling the function
            if check_win_condition(board,player_symbol):
                print("Player "+player_symbol+" is the winner!")
                game_over = True        #If the win condition is met then the game is over


            #Checking the draw condition after placing the symbol and calling the function
            elif check_draw_condition(board):
                print("It's a draw!")
                game_over = True        #If the draw condition is met then the game is over
            
            #If the both the condition isn't met then the turn is passed to the next player 
            turn = (turn % NUM_PLAYERS) + 1
    
    
    #If the input of the player doesn't met our conditions then ask the player to enter the column again
    else:
        print("Invalid column. Plz try again.")
        time.sleep(1)                                           # Wait for 1 second
        os.system('cls' if os.name == 'nt' else 'clear')        # Clear the error message
        display_board(board)                                    # Display the board after clearing the error

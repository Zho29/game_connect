import random    #imports random module
import os        #imports os modulee
import time      #imports time module


NUM_ROWS = 6      # constant variable for number of rows
NUM_COLUMNS = 6   # constant variable for number of columns
NUM_PLAYERS = 2   # constant variable for number of players 



JOKER = '*'      # constant variable for joker, useful in the time of the logical decision of game
 


main_board = []        #visible board to the user 
hidden_board = []      #invisible board to the user, save data internally



#Creating the intial visible board to the user
for r in range(NUM_ROWS):
    row=[]  
    for c in range(NUM_COLUMNS):
        row.append('#')
    main_board.append(row)



# Create a hidden board with letter twins and jokers
alphabet_list=[]                   #list using to save alphabet from A-Q and a-q
for alpha in range(17):
    alphabet_list.append(chr(65+alpha))  #Uppercase alphabet from A-Q
    alphabet_list.append(chr(97+alpha))  #Lowercase alphabet from a-q
letters=alphabet_list+['*','*']     #complete letters list of the tiles with joken in as well



#Shuffling the index of the alphabet letters and joker in our hidden board 
hidden_list=[]
while letters:                               
    index = random.randint(0, len(letters) - 1)      #random selection of the index
    hidden_list.append(letters.pop(index))          #adding the elements to the hidden list by emptying the letters list



# Assigning letters and joker to the hidden board from previous part
for i in range(NUM_ROWS):
    row = []
    for j in range(NUM_COLUMNS):
        if hidden_list:                           #Emptying the hidden list by poping out the first index and adding to the hidden board
            row.append(hidden_list.pop(0))                           
    hidden_board.append(row)                      #Creation of the hidden board internally with value and dimesnion 6x6


# Scores for both players
scores = [0, 0]


# Seelct a player to start the game 
turn = random.randint(0, NUM_PLAYERS - 1)


game_over=False  #Variable to store the state of the game 


# Main game loop
while game_over==False:

    # Clear screen 
    os.system('clear')
    

    #Displaying the score count of the players  
    print("Player 2 score:",scores[1])
    print("Player 1 score:",scores[0])

    # Most initial game board that player see 

    for column in range(NUM_COLUMNS): 
        print('   ' + chr(65+column), end='')   

    print("\n +" + "---+" * NUM_COLUMNS)

    for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for column in range(NUM_COLUMNS):
            print(main_board[row][column] + ' | ', end='')  
        print("\n +"+"---+"*NUM_COLUMNS)

    
    #loop for list with alphabet A-F
    first_six_alphabet_list=[]
    for x in range(6):
        first_six_alphabet_list.append(chr(65+x))
  

    # Input for the first coordinate from the player
    while True:
        first_coordinate = input("Player"+str(turn + 1)+": Plz enter a coordinates(A5,B1,etc) ")

        # Checking if the first letter is A-F and second letter is a digit
        if len(first_coordinate) == 2 and first_coordinate[0] in first_six_alphabet_list and first_coordinate[1].isdigit():
           
            column = first_coordinate[0]   #Storing the first letter value
            row = first_coordinate[1]      #Storing the first digit value

            # Check if the digit inputed is valid 
            if  0 <= int(row) < NUM_ROWS:
                
                column_index = ord(column) - 65           #converting to the index value from A-F
                row_index = int(row)                      #converting to the index value from string '0'-'5'

                # Seeing if the card is still hidden in the main board 
                if main_board[row_index][column_index] == "#":
                    
                    break                      # Exit the loop as the input is valid 
                
                else:
                    print("This card has already been revealed. Try again.")
            
            else:
                print("Invalid column or row. Please enter coordinates within range.")
        
        else:
            print("Invalid input. Please enter a letter and a number (e.g., A1).")
    
    # Clear screen 
    os.system('clear')


    # Showing the first card 
    column_1 = ord(first_coordinate[0]) - 65                # Changing column string to integer .'A' to 0
    row1 = int(first_coordinate[1])                         # changing row string to integer.  '0' to 0
    main_board[row1][column_1] = hidden_board[row1][column_1]
    

    #Displaying the score count of the players  
    print("Player 2 score:",scores[1])
    print("Player 1 score:",scores[0])


    # Updating the board after the first card is shown 
    for column in range(NUM_COLUMNS): 
        print('   ' + chr(65+column), end='')   
    
    print("\n +" + "---+" * NUM_COLUMNS)
    
    for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for column in range(NUM_COLUMNS):
            print(main_board[row][column] + ' | ', end='')  
        print("\n +"+"---+"*NUM_COLUMNS)

    # Input for the second coordinate from the player
    while True:
        second_input = input("Player "+str(turn + 1)+": Plz enter a coordinates(A5,B1,etc) ")

        # Checking if the first letter is A-F and second letter is a digit
        if len(second_input) == 2 and second_input[0] in first_six_alphabet_list and second_input[1].isdigit():
            
            column = second_input[0] # Convert the letter to uppercase
            row = second_input[1]

            # Check if the digit inputed is valid 
            if  0 <= int(row) < NUM_ROWS:
                
                column_index = ord(column) - 65    #converting to the index value from 'A'-'F'
                row_index = int(row)               #converting to the index value from string '0'-'5'

                # Seeing if the card is still hidden in the main board 
                if main_board[row_index][column_index] == "#":
                    break                     # Exit the loop as the input is valid
                
                else:
                    print("This card has already been revealed. Try again.")
            
            else:
                print("Invalid column or row. Please enter coordinates within range.")
        
        else:
            print("Invalid input. Please enter a letter and a number (e.g., A1).")



    # Showing  the second card
    column_2 = ord(second_input[0]) - 65                      # Changing column string to integer .'A' to 0
    row2 = int(second_input[1])                               # changing row string to integer.  '0' to 0
    main_board[row2][column_2] = hidden_board[row2][column_2]
    
    # Clear screen 
    os.system('clear')
    

    #Displaying the score count of the players  
    print("Player 2 score:",scores[1])
    print("Player 1 score:",scores[0])
          

    # Showing the updated board to the user with the second input
    for column in range(NUM_COLUMNS): 
        print('   ' + chr(65+column), end='')   
    
    print("\n +" + "---+" * NUM_COLUMNS)
    
    for row in range(NUM_ROWS):
        print(str(row) + '|', end=' ')
        for column in range(NUM_COLUMNS):
            print(main_board[row][column] + ' | ', end='')  
        print("\n +"+"---+"*NUM_COLUMNS)
    

    #Logic checking in the game 


    #Checking the rare case of both reveal card is JOKER
    if hidden_board[row1][column_1] == JOKER and hidden_board[row2][column_2] == JOKER:
        scores[turn] += 2             #Score awarded is 2 not 1 in other cases
        
        
        time.sleep(2)    # Pause for program to show the jokers
        

        #Removing the JOKERS indexS from both the main and hidden board 
        main_board[row1][column_1] = ' '
        main_board[row2][column_2] = ' '
        hidden_board[row1][column_1] = ' '
        hidden_board[row2][column_2] = ' '

    
    # Checking where one card is Joker but other card is the twin 
    elif hidden_board[row1][column_1] == JOKER or hidden_board[row2][column_2] == JOKER:


        # Case when the first revealed card is joker
        if hidden_board[row1][column_1] == JOKER:                
            original_card = hidden_board[row2][column_2]               
            if chr(65)<=original_card<=chr(65+16):              #Checking if the letter is uppercase and converting it to lowercase and vica versa
                twin_card=original_card.lower()
            else:
                twin_card=original_card.upper()
            for r in range(NUM_ROWS):                         #Searching for the twin card revealed to us 
                for c in range(NUM_COLUMNS):
                    if hidden_board[r][c] == twin_card:         #Removing the twin of the revealed card 
                        main_board[r][c] = ' '
                        hidden_board[r][c] = ' '



        # Case when the second revealed card is joker                
        elif hidden_board[row2][column_2] == JOKER:
            original_card = hidden_board[row1][column_1]
            if chr(65)<=original_card<=chr(65+16):       #Checking if the letter is uppercase and converting it to lowercase and vica versa
                twin_card=original_card.lower()
            else:
                twin_card=original_card.upper()
            for r in range(NUM_ROWS):                   #Searching for the twin card revealed to us 
                for c in range(NUM_COLUMNS):
                    if hidden_board[r][c] == twin_card:       #Removing the twin of the revealed card
                        main_board[r][c] = ' '
                        hidden_board[r][c] = ' '


        # Removing the joker and the revealed card. Awarding point to the player .
        main_board[row1][column_1] = ' '
        main_board[row2][column_2] = ' '
        hidden_board[row1][column_1] = ' '
        hidden_board[row2][column_2] = ' '
        scores[turn] += 2
        

        # Pause for 2 seconds to show the match
        time.sleep(2)
  
    
    
    # Checking pair of card by simply changing letter to lowercase but we can do uppercase too
    elif hidden_board[row1][column_1].lower() == hidden_board[row2][column_2].lower():
        scores[turn] += 1         #Awarding just 1 in this case
        
        
        time.sleep(2)  # Pause for 2 seconds to show the match

        
        # Removing the pair out of the board
        main_board[row1][column_1] = ' '
        main_board[row2][column_2] = ' '
        hidden_board[row1][column_1] = ' '
        hidden_board[row2][column_2] = ' '
     
    else:
        
        time.sleep(2)   # Pause for 2 seconds to show the revealed cards
        

        # Not found as twin, we simply fold them back to #
        main_board[row1][column_1] = '#'
        main_board[row2][column_2] = '#'

        
        # Switching player turns after the try was wasted 
        turn = (turn + 1) % NUM_PLAYERS

    # let gaming to be over intially
    game_over=True

    for row in main_board:    #looping inside the box to see if there is any # left
        for box in row:
            if box == '#':
                game_over = False      # If found a single # game doesnt stop
                break                  


# Final display of the score 
os.system('clear')
print("Player 2 Score:"+str(scores[1])) 
print("Player 1 Score:"+str(scores[0])) 


#logic behind finding out the winner
if scores[0] > scores[1]:
    print("Player 1 wins!")
elif scores[1] > scores[0]:
    print("Player 2 wins!")
else:
    print("It's a tie!")
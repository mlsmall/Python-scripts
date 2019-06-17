
def DisplayBoard(board):
    background = f"+-------+-------+-------+\
\n|       |       |       |\
\n|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\
\n|       |       |       |\
\n+-------+-------+-------+\
\n|       |       |       |\
\n|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\
\n|       |       |       |\
\n+-------+-------+-------+\
\n|       |       |       |\
\n|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\
\n|       |       |       |\
\n+-------+-------+-------+"

    #print("This is the board", end='\n')
    print(background)

def EnterMove(board):
# the function accepts the board current status, asks the user about their move and updates the board 
    move = int(input('Where would you like to place your O? '))
    if move < 1 or move > 10:
        print('The number must between 1 and 9. Try again.')
        EnterMove(board)
    else:
        number = move-1 # cell's number from 1 through 8
        row = number//3 # cell's row
        column = number %3 # cell's column
        if board[row][column] == 'O' or board[row][column] == 'X':
            print('That spot is taken. Try another one.')
            EnterMove(board)
        else:
            print('Player goes')
            board[row][column] = 'O'
    
    return board
        


def MakeListOfFreeFields(board):
#this function browses the board and builds a list of all the free squares. 

    freesquares=[]
    
    for i in range(9):
        row = i//3
        column = i %3
        if board[row][column] != 'X' and board[row][column] != 'O':
            freesquares.append((row, column))
    
    return freesquares
        

def VictoryFor(board, sign):
# the function analyzes the board status to check if the player using 'O's or 'X's has won the game   

    # Checking if the player won
    if sign == 'O':
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            return 2

        elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
            return 2

        elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
            return 2
   
        elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            return 2

        elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            return 2

        elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            return 2
        
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 2

        elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            return 2
            
        else:
            return
        
    
    # Checking if the computer won
    else:
        
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            return 1

        elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            return 1

        elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            return 1
    
        elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
            return 1

        elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
            return 1

        elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':           
            return 1

        elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            return 1

        else:
            return


    
#
# 
#

def DrawMove(board):
# this function draws the computer's move and updates the board    

    from random import randrange
    
    compumove = randrange(10)
    
    number = compumove-1
    row = number//3
    column = number %3

    if board[row][column] == 'O' or board[row][column] == 'X':
        DrawMove(board)             
        
    else:
        print('Computer goes')
        board[row][column] = 'X'

    return board
    

# The game functions are defined above
# Now lets start the game

board = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(9):
    #DisplayBoard(board)    

    board = DrawMove(board)
    winX = VictoryFor(board, 'X')
    if winX == 1:
        DisplayBoard(board)
        print('The computer Wins!')
        break
    freesquares = MakeListOfFreeFields(board)
    if len(freesquares) == 0:
        DisplayBoard(board)
        print('The game is a tie.')
        break
    DisplayBoard(board)
    
    board=EnterMove(board)
    win0 = VictoryFor(board, 'O')
    if win0 == 2:
        DisplayBoard(board)
        print('Congratulations! You Win!')
        break  
    freesquares = MakeListOfFreeFields(board)
    if len(freesquares) == 0:  
        DisplayBoard(board)
        print('The game is a tie.')
        break
    DisplayBoard(board)

    VictoryFor(board, '0')
    
    
    
    
    

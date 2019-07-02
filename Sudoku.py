# Sudoku
# This function checks whether 9 lists of numbers consitute a Sudoku board

'''row1 = list(input("Enter first row: "))
row2 = list(input("Enter second row: "))
row3 = list(input("Enter third row: "))
row4 = list(input("Enter fourth row: "))
row5 = list(input("Enter fifth row: "))
row6 = list(input("Enter six row: "))
row7 = list(input("Enter seventh row: "))
row8 = list(input("Enter eight row: "))
row9 = list(input("Enter ninth row: "))'''

#Sudoku board
row1='295743861'
row2='431865927'
row3='876192543'
row4='387459216'
row5='612387495'
row6='549216738'
row7='763524189'
row8='928671354'
row9='154938672'

'''#Not a sudoku board
row1="195743862"
row2="431865927"
row3="876192543"
row4="387459216"
row5="612387495"
row6="549216738"
row7="763524189"
row8="928671354"
row9="254938671"'''



board = [[1 for i in range(9)] for j in range(9)]


board[0] = list(row1)
board[1] = list(row2)
board[2] = list(row3)
board[3] = list(row4)
board[4] = list(row5)
board[5] = list(row6)
board[6] = list(row7)
board[7] = list(row8)
board[8] = list(row9)

subboards = board[:]

subboards[0] = [board[0][0:3], board[1][0:3], board[2][0:3]]
subboards[1] = [board[0][3:6], board[1][3:6], board[2][3:6]]
subboards[2] = [board[0][6:], board[1][6:], board[2][6:]]
subboards[3] = [board[3][0:3], board[4][0:3], board[5][0:3]]
subboards[4] = [board[3][3:6], board[4][3:6], board[5][3:6]]
subboards[5] = [board[3][6:], board[4][6:], board[5][6:]]
subboards[6] = [board[6][0:3], board[7][0:3], board[8][0:3]]
subboards[7] = [board[6][3:6], board[7][3:6], board[8][3:6]]
subboards[8] = [board[6][6:], board[7][6:], board[8][6:]]

columns = board[:]

columns[0] = [board[i][0] for i in range(9)]
columns[1] = [board[i][1] for i in range(9)]
columns[2] = [board[i][2] for i in range(9)]
columns[3] = [board[i][3] for i in range(9)]
columns[4] = [board[i][4] for i in range(9)]
columns[5] = [board[i][5] for i in range(9)]
columns[6] = [board[i][6] for i in range(9)]
columns[7] = [board[i][7] for i in range(9)]
columns[8] = [board[i][8] for i in range(9)]

check1 = []
check2 = []
check3 = []
finalcheck = []

# check if all sub-boards (3x3) are good
for i in range(0,9):
    listcheck = [1,2,3,4,5,6,7,8,9]
    for row in subboards[i]:       
        for digit in row:
            if int(digit) in listcheck:
                listcheck.remove(int(digit))
                check1.append(1)

if len(check1) == 81:
    finalcheck.append(1)
    
# check if all rows are good
for rows in board:
    listcheck = [1,2,3,4,5,6,7,8,9]
    for digit in rows:
        if int(digit) in listcheck:
            listcheck.remove(int(digit))
            check2.append(1)
                

if len(check2) == 81:
    finalcheck.append(1)
    
# check if all columns are good
for column in columns:
    listcheck = [1,2,3,4,5,6,7,8,9]
    for digit in column:
        if int(digit) in listcheck:
            check3.append(1)
            listcheck.remove(int(digit))
            
if len(check3) == 81:
    finalcheck.append(1)

print(finalcheck)

if len(finalcheck) == 3:
    print("Sudoku!")

else:
    print("This is not a Sudoku board.")



            
        
    
    

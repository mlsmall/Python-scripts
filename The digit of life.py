# The Digit of Life

birthday = input("What is your birthday?\n\
Enter it in any format YYYYMMDD or YYYYDDMM or MMDDYYY: ")

while len(birthday) != 8:
    birthday = input('Sorry. Please try again: ')

sumbirthday = 0

for number in birthday:
    sumbirthday += int(number)
    
string = str(sumbirthday)

sumstring = 0
for character in string:
    sumstring += int(character)
    
print("Your digit of life is", sumstring)
    
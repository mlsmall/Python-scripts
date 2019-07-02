# Find a word inside a string of characters

string1 = input("Enter a word: ").lower()
string2 = input("Enter a combination of characters: ").lower()

check=[]    

for letter in string1:
    if letter in string2:
        check.append(1)
    else:
        check.append(0)

if 0 in check:
    print('No')
else:
    print('Yes')
    
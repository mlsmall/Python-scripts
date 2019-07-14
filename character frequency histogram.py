# Character frequency histogram
# This program reads a textfile and outputs the frequeny of each character
from os import strerror

filename = input("What is the filename? ")

try:
    file = open(filename, 'r')
except IOError as e:
    print("Cannot open file.", strerror(e.errno))
    exit()
    
store = {}
count = 0

read = file.read()
for char in read:
    if char.isalpha() == True:
        if char not in store.keys():
            count = 1
            store.update({char.lower(): count})
        else:
            count += 1
            store.update({char.lower(): count})

for key, value in sorted(store.items()):
    print(key, '-->', value)

file.close()

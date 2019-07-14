# Character frequency histogram sorted
# This program reads a textfile and outputs the frequeny of each character
# The characters are sorted in order of appearance from most to least and output
# to a .hist file.
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

clean_name = filename.split('.')[0]
output = open(clean_name + '.hist', 'w+t')


newstore = {}

for key, value in sorted(store.items(), key=lambda x: x[1], reverse=True):
    output.write(str(key) + ' --> ' + str(value) + '\n')


#output.write(string(newstore)

file.close()
output.close()

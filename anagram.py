# Anagrams
# This programs detects if two words or sentences are anagrams

firstword = input('Enter the first word or sentence: ')
secondword = input('Enter the second word or sentence: ')

firstword = firstword.replace(" ", "")
secondword = secondword.replace(" ", "")

listw = []

for character in firstword.lower():
    if character in secondword.lower():
        listw.append(1)
    else:
        listw.append(0)

if 0 not in listw:
    print('These words are anagrams')

else:
    print('These words are not anagrams')
          

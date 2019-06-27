# My split function for strings
# Takes a string, splits each word, removes all spaces, and makes a list out of the words.

def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return []

    # prepare a list to return
    wordlist = []
    # prepare a word to build subsequent words
    word = ""
    # prepare the last word of the list
    lastword = ""

 
    for character in strng:
        word += character
        if character == " ":
            word = word[:-1]
            wordlist.append(word)
            word = ""
            
    index = strng.rfind(' ')
    
    for lastchars in strng[index:]:
        lastword += lastchars
    
    wordlist.append(lastword)
    
    for word in wordlist:
        if word.isspace() or word == "":
            wordlist.remove(word)

 
    return wordlist
        
        

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("The cat in the hat is the hat in the cat."))

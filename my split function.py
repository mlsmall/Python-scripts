# My split function for strings
# Takes a string, splits each word, removes all spaces, and makes a list out of the words.

def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return []

    # initialize a list to return
    wordlist = []
    # initialize a word to build subsequent words
    word = ""
    # initialize the last word of the list
    lastword = ""

    # Making a word from the sum of characters before an empty space
    # And then appending that word to the list
    for character in strng: # For every character inside the string
        word += character
        if character == " ":
            word = word[:-1]
            wordlist.append(word)
            word = ""
            
    # Index of where the last space is in the string
    index = strng.rfind(' ')
    
    # Adding the charcters from the last space until the end of the string
    for lastchars in strng[index:]:
        lastword += lastchars
    # Appending the last character to the list
    wordlist.append(lastword)
    
    # Removing any additional spaces inside the list
    for word in wordlist:
        if word.isspace() or word == "":
            wordlist.remove(word)

 
    return wordlist
        
        
# Testing the function
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("The cat in the hat is the hat in the cat."))

# Caesar cipher
# This program will encode your message using the Caesar cipher

text = input("Enter your message: ")

# While loop to make sure the correct shift value is entered
# Shift is used to shift your letters to the right
shift = 0
while shift == 0:
    try:
        shift = int(input('Enter your shift value between 1-25: '))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        print("Wrong shift value. Try again.")
        shift = 0
     

cipher = ''
for char in text:
    if not char.isalpha(): # If the character is a number
        cipher += char # Leave the character the same
        
    elif char == " ": # If the character is a space
        cipher += char # Leave the character the same
    
    elif char.isupper() == True: # If the character is an uppercase letter
        code = ord(char) + shift # Add the shift to the character

        if code > ord('Z'): # If the encoded character is greater than ord(Z)
            code = code + ord('A') - ord('Z') - 1 # Start over from 'A'

        cipher += chr(code)

    elif char.islower() == True: # If the character is a lowercase letter
        code = ord(char) + shift # Add the shift to the character

        if code > ord('z'): # If the encoded character is greater than ord(z)
            code = code + ord('a') - ord('z') - 1 # Start over from 'a'

        cipher += chr(code)

    else: # Every other character remains the same
        cipher += char

print("Your encoded message is: ", cipher)

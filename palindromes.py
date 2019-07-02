# Palindromes
# A palindrome is a text that looks the same whether it's read forward or backward
# Example: kayak, Ten animals I slam in a net

text = input("Enter a text: ")
if text.isspace() == True:
    print("This isn't a palindrome. Try again.")
    text = input("Enter a text: ")
    
text2 = ""
for char in text:
    if char == " ":
        continue
    text2 += char

reverse = ""
for i in range(len(text2)):
    reverse += text2[len(text2)-1-i]

print(text2)
print(reverse)

if text2 == reverse:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    
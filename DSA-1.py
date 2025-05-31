#Palindrome checker
text = input("Enter a string: ")
reverse = ""
for i in range(len(text)-1, -1, -1):
    reverse += text[i]
if text == reverse:
    print("Yes! It is a palindrome.")
else:
    print("Sorry! It's not a palindrome")
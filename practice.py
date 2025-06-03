'''
START
Input nibo ekta number
1. Convert number to string
2. Reverse the string
3. Compare original string with reversed string
    If same:
        Print "Palindrome"
    Else:
        Print "Not Palindrome"
END
'''
num = input("Enter a number: ") #converted num to string
rev = num[::-1] #reversed stirng
if num == rev:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")


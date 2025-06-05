'''
START
Input nibo ekta number
Step 1:
    sum = 0
Step 2:
    Prottek digit niye:
        sum er sathe add korbo
Step 3:
    Output korbo sum
END
'''
num = input("Enter a number: ")
total = 0

for digits in num:
    total += int(digits)

print(f"Sum of the digits is: {total}")

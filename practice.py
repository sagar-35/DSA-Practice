'''
START
INPUT number1
INPUT number2
INPUT number3
IF number1 >= number2 AND number1 >= number3 THEN
    largest ← number1
ELSE IF number2 >= number1 AND number2 >= number3 THEN
    largest ← number2
ELSE
    largest ← number3
END IF
OUTPUT "The largest number is", largest
END
'''
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))
num3 = float(input("Enter Number 3: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")
# factorial finding
# START
# user input
# if user input < 0
# print negative numbers not for factorials
# elif user input is equals to 0 and 1 
# it's factorial will be 1 
# factorial variables 1 
# for loop 2 theke n porjontto 1 ghore kore barbe 
# print 
# END

num = int(input("Enter a number: "))

if num < 0: 
    print("Factorial not for negative numbers.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1.")
else:
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    print(f"{num}! = {factorial}")
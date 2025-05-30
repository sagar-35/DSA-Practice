# Factorail Practice
def factorial(n):
    if n < 0:
        return "Negative number is not a factorial."
    elif n == 1 or n == 0:
        return 1 
    else:
        result = 1
        for i in range(2, n+1):
            result *= i 
        return result

num = int(input("Enter a number: "))
print(f"{num}! = ", factorial(num))
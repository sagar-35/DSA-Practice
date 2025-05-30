# Factorial 
# Step-1 Function

def factorial(n):
# Step-2 Variable 
    result = 1
# Step-3 Loop for multiply by multiple time
    for i in range(1, n+1):
        result = result * i

# Step-4 return
    return result

# Step-5 User input
num = int(input("Enter any number for factorial: "))
print(f"{num}! = ",factorial(num))




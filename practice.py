'''START
1. List create korbo
2. Even and odd count er jonno duita variable banabo (even = 0, odd = 0)
3. Loop chalabo list er upor:
    jodi number % 2 == 0:
        even++
    na hole:
        odd++
4. Output: even count and odd count
END'''

list = [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1 
    else:
        odd_count += 1
    
print(f"Even = {even_count}")
print(f"Odd = {odd_count}")


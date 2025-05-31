# Problems vowels in a string
# in: Hello World
# out: 3
# START
# Input user theke
# count set korbo 0 
# for each character in string:
#       if character is vowel(a, e, i, o, u) or uppercase version:
#       count +1
# print count

text = input("Enter any string: ")
count = 0

for chr in text:
    if chr.isalpha() and chr.lower() in "aeiou":
        count += 1
print("Number of vowel: ", count)
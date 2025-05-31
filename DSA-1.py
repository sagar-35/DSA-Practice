#Angrams checker
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.lower().replace(" ", "")
text2 = text2.lower().replace(" ", "")

sorted_text1 = sorted(text1)
sorted_text2 = sorted(text2)

if sorted_text1 == sorted_text2:
    print("They are Anagrams")
else:
    print("Not Anagrams!")
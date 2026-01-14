sum = 0
s1 = input("Enter a sentence1: ")
s2 = input("Enter a sentence2: ")

print("The Reversed of s1 is:", s1[::-1])
print("The first letter of original s2 is:",s2[0])
sum = len(s1) - len(s2)
print("The result of S1 - S2 Length is:",sum)
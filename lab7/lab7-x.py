sum = 0
s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

sum = len(s1) - len(s2)

print("The Original sentence s1 is: ",s1)
print("The Reversed sentence s1 is: ",s1[::-1])

print("The first letter of org s2 is:",s2[0])
print("The last  Reversed of s2 is:",s2[-1])

print("The amount od length s1 - s2 is",sum)
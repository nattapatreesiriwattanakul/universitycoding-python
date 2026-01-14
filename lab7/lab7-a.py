# 6610742246 Nattapat Reesiriwattanakul
# lab7 Question A
# reverse string and show the result of Original and reveresed
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Enter the string to reverse: ")
print("The original string  is : ", end="")
print(s)
print("The reversed string is : ", end="")
print(reverse(s))



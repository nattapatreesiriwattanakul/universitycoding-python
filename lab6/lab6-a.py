# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question A
# กำหนดตัวแปรค่าn เข้าสู่def เข้าฟังก์ชันหาค่าfactorial
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", fact(num))

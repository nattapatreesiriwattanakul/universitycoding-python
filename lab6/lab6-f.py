# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question F
# ใช้function ที่กำหนดร่วมกับloop while หาค่าgcd
def find_gcd(a, b):
    while b:
        a, a = b, a % b
        return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
num = find_gcd(a, b)
print(f"The GCD of two number a and b is {num}")

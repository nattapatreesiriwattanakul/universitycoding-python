# 6610742246 Nattapat Reesiriwattanakul
# lab10 Question A
# ใช้tryในการกำหนดเงื่อนไข จากinputที่รับเช้ามา

n=int(input("Enter the value of n: "))
d=int(input("Enter the value of d: "))
c=int(input("Enter the value of c: "))
try:
    q=n/(d-c)
    print("Quotient:",q)
except ZeroDivisionError:
    print("Division by Zero!")


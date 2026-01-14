# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question C
# เรียกใช้ฟังก์ชันแต่ละอันออกมา แต่ละอันจะมีงานของตัวเอง
def cir():
    r = int(input("Enter the radius: "))
    area = 3.14 * r * r
    return area

def tria():
    b = int(input("Enter the base: "))
    h = int(input("Enter the height: "))
    area = 1/2 * b * h
    return area

def square():
    a = int(input("Enter the side: "))
    area = a * a
    return area

def rect():
    l = int(input("Enter the length: "))
    w = int(input("Enter the width: "))
    area = l * w
    return area

print(cir())
print(tria())
print(square())
print(rect())

# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question B
# เพิ่มการเก็บค่า ในลิสต์จากข้อA เพื่อหาค่าสูงที่สุดจากทุกตัวในลิสต์
def find_max(lst):
    max = lst[0]
    for a in lst:
        if a > max:
            max = a
    return max

num = int(input('How many numbers: '))
lst = []
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Maximum element in the list is :", find_max(lst))

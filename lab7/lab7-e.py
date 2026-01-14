# 6610742246 Nattapat Reesiriwattanakul
# lab7 Question E
# แสดงผลคำ(a) ให้เป็นไปตามรูปแบบที่โจทย์ต้องการ โดยใช้[]ในการเข้ามาข่วย a แสดงผลในรูปแบบค่าที่ต้องการ
a = "hello"
print("String is: ", a)

# accessing a string
print("Accessed String is: ", a[3])

# Slicing Operation
print("Slicing Operation:", a[0:3])
print("Forward Slicing:", a[0:4])
print("Backward Slicing:", a[-3:-1])
print("Slicing using size:", a[1:4:2])

# concatenation
print("concatenation:", a + "Hi")

# repetition
print("Repetition:", a * 3)

# membership
print("Membership e in a:", 'e' in a)
print("Membership v in a:", 'v' in a)

# methods
print("string in Uppercase:", a.upper())
print("Length of string:", len(a))

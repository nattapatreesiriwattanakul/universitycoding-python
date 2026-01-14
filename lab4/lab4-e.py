# 6610742246 Nattapat Reesiriwattanakul
# lab 4 Question E
# นำข้อมูลและตัวแปรที่กำหนดไว้ ดึงค่ามาแสดงผลตามOutput
type1 = (1, 3, 4, 5, 'test')
tuple1 = ('a', 'b', 1, 3, [5, 'x', 'y', 'z'])
color = 'red','green','blue'

print(type1)

print(tuple1[0])
print(tuple1[4][1])
print(tuple1[4])
print(tuple1[2:])

new_tuple = type1[0:3], * color
print(new_tuple)

print(1 in type1)
print('z' in tuple1)
print(max(type1[0:3]))
print(sum(type1[0:3]))
new_list = list(type1[0:3])
print(new_list)
print("Result: Thus, the applications and operations of list , tuple has been executed. ")
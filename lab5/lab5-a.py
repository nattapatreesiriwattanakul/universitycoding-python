# 6610742246 Nattapat Reesiriwattanakul
# lab 05 Question B
# สร้างcomponents list แสดงผลทั้งหมด และทำการpopข้อมูลออก หลังจากนั้นแสดงผลรายการทั้งหมดหลังจากอัพเดต

components = {}
print(type(components))

components = set() #ไม่เก็บค่าซ้ำ
print(type(components))

components = {"Clutch", "Gear Box", "Front dead axle", "Engine", "Rear drive axle", "Differential"}
print("Initial Components:", components) 

b = input("Enter the components to be added: ") 
components.add(b)

print("Components of automobile after adding an element in set")
print(components)

# ลบ-pop สุ่ม
print("Removing one Component")
components.pop()

print("Updated Components after removing an element in set")
print(components)
# 6610742246 Nattapat Reesiriwattanakul
# lab 05 Question B
# สร้างlist eliment และทำการแสดงข้อมูลโดยใช้ tool(pop) ในการลบค่า สุดท้ายทำการเพิ่มค่า และแสดงผล
Elements_dictionary = {}
Elements_dictionary = {
    1: 'Roof',
    2: 'Parapet',
    3: 'Lintels',
    4: 'Beams',
    5: 'Columns',
    6: 'Walls',
    7: 'Floor',
    8: 'Stairs'
}

print("The dictionary elements of Civil Structure")
print(Elements_dictionary)

# pop()
print("Remove the particular item in the Civil structure")
removed_item = Elements_dictionary.pop(4)
print("Removed:", removed_item)

# เพิ่ม
Elements_dictionary[9] = 'Plinth Beam'
print("The Dictionary Elements after adding one element in Civil Structure")
print(Elements_dictionary)

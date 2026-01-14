# 6610742246 Nattapat Reesiriwattanakul
# lab7 Question C
# รับค่าสองตัว ใช้loop for ในการหาและเช็คค่าว่ามีตรงกันไหม ถ้าตรงกันเพิ่มค่าcountและแสดงผล
test_str = input("Enter the String: ")
character = input("Enter the Character: ")
count_char = 0
count_notchar = 0 #add

for i in test_str:
    if i == character:
        count_char = count_char + 1
    else:
        count_notchar = count_notchar +1 #add
print("Count is : " + str(count_char))
print("Total count of uncharacter is : " + str(count_notchar)) #add


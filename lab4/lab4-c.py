# 6610742246 Nattapat Reesiriwattanakul
# lab 4 Question C
# กำหนดค่าในลิสต์ แสดงเมนูทั้งหมดที่มี พร้อมกับเลือกchoice เลือกด้วย ตัวเลขตามลำดับ 
materials = ('Bricks', 'Cement', 'Steel', 'Wood', 'Glass', 'Concrete', 'Stone')
ch = 'y'

while ch == 'y':
    print("1. Display Materials")
    print("2. Display types of Materials")
    print("3. Display Reverse order of materials")
    print("4. Count of Needed materials")
    print("5. Choose a material at random")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Materials:", materials)
    elif choice == 2:
        print("Types of Materials:", set(materials))  # (unique ones)
    elif choice == 3:
        print("Materials in reverse order:", materials[::-1])
    elif choice == 4:
        print("Number of needed materials:", len(materials)) 
    elif choice == 5:
        import random
        print("Random material:", random.choice(materials)) 
    
    ch = input("Do you want to continue...?y/n: ")

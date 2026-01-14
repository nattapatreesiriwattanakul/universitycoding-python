# 6610742246 Nattapat Reesiriwattanakul
# lab 4 Question B
# กำหนดค่าในลิสต์ แสดงเมนูทั้งหมดที่มี พร้อมกับเลือกchoice เลือกด้วย ตัวเลขตามลำดับและจะมีการแสดงผลตามเมนูที่ต้องการ จบท้ายลูปด้วยการถามความต้องการทำซ้ำ(y)
components = ['RADIATOR', 'AC COMPRESSOR', 'BATTERY', 'ALTERNATOR', 'AXLE', 'BRAKES', 'SHOCK ABSORBERS', 'TRANSMISSION', 'FUEL TANK']
components1 = ['CATALYTIC CONVERTER', 'MUFFLER', 'TAILPIPE']
ch = 'y'

# ขั้นตอนที่ 2: แสดงเมนูและอ่านตัวเลือก
while ch == 'y':
    print("1.Display Main Components")
    print("2.Display All Components")
    print("3.Total Components")
    print("4.Components in Alphabetical Order")
    choice = int(input("Select: "))
   
    if choice == 1:
        print("Display Main Components:", components)
    elif choice == 2:
        print("Display All Components:", components + components1)
    elif choice == 3:
        total_components = len(components) + len(components1)
        print("Total Components", total_components)
    elif choice == 4:
        all_components_sorted = sorted(components + components1)
        print("Components in Alphabetical Order:", all_components_sorted)
    
    ch = input("Do you want to continue...?(y/n): ")

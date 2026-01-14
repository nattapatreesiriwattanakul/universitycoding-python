# 6610742246 Nattapat Reesiriwattanakul
# lab 4 Question A
# สร้างลิสต์เปล่าสำหรับการเก็บข้อมูล มีchoice ให้เลือกในครั้งแรก 1 และ 2 //1จะมีการเพิ่มชื่อหนังสือที่inputค่าเข้ามา 2จะแสดงชื่อทั้งหมดที่อยู่ในlist //
# หลังจากจบกระบวนการรอบแรกจะมีการถาม หากตอบy จะวนเข้าลูปอีกครั้งนอกนั้นหลุดจากลูป
my_book = []  
ch = 'y'
count = 1 #add
while ch == 'y':
    print("1. Add New Book")
    print("2. Display Books")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_name = input("Enter the name of the book: ")
        my_book.append(book_name)
        print(f"> {book_name} has been added.") #add
    elif choice == 2:
        print("> Books in the list:")
        for book in my_book:
            print(f"{count}.{book}") #change
            count += 1 #add
        print(f"> The number of my books is {count - 1}.") #add

    ch = input("Do you want to continue...?y/n: ")
    if ch == 'n': #goodboy
        print("Good Bye") #cf loop

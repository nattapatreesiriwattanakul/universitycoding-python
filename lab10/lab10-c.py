# 6610742246 Nattapat Reesiriwattanakul
# lab10 Question C
# กำหนดmin max ที่ต้องการและใช้ค่าในการคำนวณต่อในเงื่อนไข

def input_number(min,max):
    try:
        while True:
            n=int(input("Please enter a number between {} and {} :".format(min,max)))
            n=int(n)
            if(min<=n<=max):
                print(n)
                break
            else:
                print("Above 100, wrong")
                break
    except:
        print("mark must be a valid number")
input_number(1,100)
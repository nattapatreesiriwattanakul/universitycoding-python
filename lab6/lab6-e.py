# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question E
# กำหนด ค่าตัวเลือก - รายละเอียดในฟังก์ชัน เพื่อแสดงผลตามinputที่ผู้ใช้ต้องการ
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

     
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no": #badboy 
            break
    else:
        print("Invalid Input. Try it Again") #cf loop

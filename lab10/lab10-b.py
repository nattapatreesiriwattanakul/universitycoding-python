# 6610742246 Nattapat Reesiriwattanakul
# lab10 Question B  
# ใช้try คู่กับการใช้เงื่อนไข  if else และเรียกใช้mainด้วย

def main():
    try:
        age=int(input("Enter your age: "))
        if age>18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote")
    except:
        print("age must be a valid number")
main()

# 6610742246 Nattapat Reesiriwattanakul
# lab7 Question B
# ใช้ if else ในการตรวจสอบค่าinput ที่รับเข้ามา โดยใช้การอ่านค่าและแสดงผล
string = input(("Enter a letter: "))
if(string == string[::-1]):
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")

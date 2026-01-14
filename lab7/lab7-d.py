# 6610742246 Nattapat Reesiriwattanakul
# lab7 Question D
# ใช้methodการแทนที่(.replce) โดยแยกทำตามขั้นตอน (เสร็จขั้นตอนแล้วprintออกมาดูก่อน) 
string = " HI! HI! HI! WELCOME TO PYTHON PROGRAMMING"
print("Original String:", string)

replace1 = string.replace("HI", "HELLO")
print("Replaced String 1:", replace1)

replace2 = replace1.replace("HELLO", "Hello", 3)
print("Replaced String 2:", replace2)

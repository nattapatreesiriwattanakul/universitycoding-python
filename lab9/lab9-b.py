# 6610742246 Nattapat Reesiriwattanakul
# lab9 Question B
# เปิด txt และเรียกใช้ทำตามขั้นตอน

fin = open("book.txt", "r")
str = fin.read()
l = str.split()
count_words = 0
for i in l:
   count_words = count_words + 1
print(count_words)
fin.close()
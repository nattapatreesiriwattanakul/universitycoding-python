# 6610742246 Nattapat Reesiriwattanakul
# lab9 Question C
# ใช้คำสั่งในการตรวจสอบ

fin = open("name.txt", "r")
str = fin.read()
words = str.split()
max_len = len(max(words, key=len))
for word in words:
   if len(word) == max_len:
       longest_word = word
print(longest_word)
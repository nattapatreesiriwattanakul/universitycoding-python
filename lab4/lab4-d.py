# 6610742246 Nattapat Reesiriwattanakul
# lab 4 Question C
# แสดงค่าตามที่โจทย์ต้องการโดยใช้คำสั่งเข้ามาใช้กับตัวแปรnumbers คามนutputที่ต้องการ

numbers = [11, 22, 33, 100, 200, 300]

print(min(numbers)) 
print(max(numbers)) 
print(numbers[1]) 
print(numbers[-1]) 
print(numbers.pop(3)) 
print(numbers[2]) 

numbers.clear()

numbers.extend(['world', 'hi']) 
print(numbers)

numbers.insert(0,'hello') 
print(numbers)

word = ['bye'] 
print(word)

numbers.extend(word)
print(numbers)

numbers.insert(3,100)
print(numbers)

numbers.append(99)
print(numbers)

numbers.extend([11,22])
print(numbers)

numbers[2] = 100
print(numbers)

del numbers[1:4]
numbers.insert(1,11)
numbers.insert(2,22)
numbers.insert(3,33)
print(numbers)

del numbers[2:4]
print(numbers)

numbers.clear()
numbers.extend(['A', 'F', 'Z', 'O', 'L'])
print(numbers)

numbers.pop(1)
print(numbers)

numbers.clear()
print(numbers)








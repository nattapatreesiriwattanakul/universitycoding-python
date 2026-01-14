# 6610742246 Nattapat Reesiriwattanakul
# lab 06 Question D
# รับค่าinputไปทำต่อในfunction sum_list() ใช้loop forในงาน และprint resultออกมา
def sum_list(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    return sum

l = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    x = int(input("Enter the element: "))
    l.append(x)

result = sum_list(l)
print(result)

# 6610742246 Nattapat Reesiriwattanakul
# lab 05 Question C
# รับค่านักเรียน เก็บข้อมูลและแสดงข้อมูลในรูปแบบloop for

n = int(input("Please enter number of students: "))
all_students = []

for i in range(n): #loop
    stud_name = input('Enter the name of student: ')
    stud_rollno = int(input('Enter the roll number of student: '))
    mark1 = int(input('Enter marks in subject 1: '))
    mark2 = int(input('Enter marks in subject 2: '))
    mark3 = int(input('Enter marks in subject 3: '))

    total = mark1 + mark2 + mark3
    average = total / 3

    student_record = { #d
        'Name': stud_name,
        'Rollno': stud_rollno,
        'Mark1': mark1,
        'Mark2': mark2,
        'Mark3': mark3,
        'Total': total,
        'Average': average
    }

    all_students.append(student_record)

# แสดงข้อมูลของนักเรียน
for student in all_students:
    print("\nStudent Record:") 
    for key, value in student.items(): #,
        print(f"{key}: {value}")

# 6610742246 Nattapat Reesiriwattanakul
# lab9 Question A
# inputชื่อที่ต้องการ เรียกคำสั่งตามโจทย์

print("Enter the Name of Source File: ")
sourcefile = input()
print("Enter the Name of Target File: ")
targetfile = input()
fileHandle = open(sourcefile, "r")
texts = fileHandle.readlines()
fileHandle.close()
fileHandle = open(targetfile, "w")
for s in texts:
   fileHandle.write(s)
fileHandle.close()
print("File Copied Successfully!")
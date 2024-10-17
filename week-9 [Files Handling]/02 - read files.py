# -------------------------------------------
# ---- File Handling - Read Files ----
# -------------------------------------------
# 
# file.read(size!) => return file content
# file.readLines(size!) => return file content lines as list
# file.readLine(size!) => return one line at a time
# -------------------------------------------
import os


myFile = open(r"d:\programming\VsCode-Workspace\Courses\Python\week-9 [Files Handling]\read.txt", "r")


# كيرجع ليك بيانات عن الملف ماشي المحتوى ديالو file فاش كطبع ال
# print(myFile) # File Data Object



# ------------------------------

# // كترد ليك المحتوى ديال ال ملف read ال
# // لي بغيتي تعرض chars واحد وهو اختياري. وهو عدد ال arg وكتقبل

# print(myFile.read()) # file content



# ------------------------------

# كيقرا ليك سطر بسطر readline ال

# print(myFile.readline()) # hello my name mohamed id-abdellah
# print(myFile.readline()) # i am from morocco

# ------------------------------


# list كترد ليك السطور كاملين على شكل readLines ال

# print(myFile.readlines())
# ['hello my name mohamed id-abdellah\n', 'i am from morocco\n', 'i am tewenty-one yrs old\n', '01 testing\n', '02 testing\n', '03 testing\n', '04 testing\n', '05 testing\n', '06 testing\n', '07 testing\n', '08 testing\n', '09 testing\n', '10 testing']



for line in myFile:
    print(line)
    if line.startswith("07"): break


# كتسد الملف و مكتخليكش مزال تعدل عليه, خاص تحلو تاني من جديد close ال
myFile.close()
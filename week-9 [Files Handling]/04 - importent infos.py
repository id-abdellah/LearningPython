# -------------------------------------------
# ---- File Handling - Important infos ----
# -------------------------------------------
# 
# file.truncate(size) => truncates file content
# file.tell() => return the index position of cursor
# file.seek(offset)
# -------------------------------------------
import os

myFile = open(fr"{os.path.dirname(os.path.abspath(__file__))}\impInfos.txt", "a")


print(myFile.tell()) # 27


# لي غتخلي من محتوى الملف والباقي تمسحو bites كتعطيها عدد ال truncate هاذ ال
myFile.truncate(10) # hello from

myFile.write(" python with love")


myFile.close()


# فبحال الا كتقوليه قرا الملف من هاد الموضع seek اما بالنسبة لل
# يعني كيرجع محتوى الملف من الموضع لي غتعطيه ليه

myFile2 = open(fr"{os.path.dirname(os.path.abspath(__file__))}\impInfos.txt", "r")

myFile2.seek(11)
print(myFile2.read()) # python with love





# file handling تالهنا كمل درس ال
# system ولي كتقد من خلالو تعامل مع ال os اخير هو module ولكن كاين
# بحال انك تمسح مجلد اولا ملف اولا تعاود التسمية. المهم التعامل مع النظام

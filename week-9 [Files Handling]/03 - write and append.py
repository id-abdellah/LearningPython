# -------------------------------------------
# ---- File Handling - Write and Append ----
# -------------------------------------------
# 
# file.write(str) => writing given str in the content
# file.writeLines(list) => writing list content in the file
# -------------------------------------------

import os


# وهي انه كينشئ الملف الا مكانش ديجا w mode او حاجة خاص نعرفوها على ال
# ف هو كيمسح غاع المحتوى لي كان قبل عاد كيضيف الجديد write تاني حاجة مهمة وهي انك فاش كدير

myFile = open(fr"{os.path.dirname(os.path.abspath(__file__))}\write.txt", "w")

myFile.write("Hello my name is mohamed\n")
myFile.write("i am from morocco and i am twenty-one years old\n\n")

for n in range(1, 10):
    myFile.write("- " + str(n) + "\n")
else:
    myFile.write("\n")



# المحتوى ديالها فالملف write باش loop و كدير عليها list فهي كتقبل منك writeLines() اما بالنسبة لل

myFriendsList = ["Laayal\n", "Atiq\n", "Mohamed\n", "Solayman\n", "Brahim\n", "Obito\n\n"]
myFile.writelines(myFriendsList)


myFile.write("Hello Bruh\n" * 20)


myFile.close()


# ---------------------------------------------------
# "a" mode

# file فال write تاهو كدير append mode بالنسبة لل
# جديد content القديم و انما كيزيد عليه ال content ولكن هو مكيمسحش ال

# كاين cursor هي فين ال content البلاصة لي كيضيف فيها

# new lines ضفناها درنا بزاف دال str يعني مثلا اخر
# cursor غضيف فاخر بلاصة لي كاين فيها ال append ال

myFile2 = open(fr"{os.path.dirname(os.path.abspath(__file__))}\write.txt", "a")

myFile2.write("Obito Uchiha \n\n\n")

myFile2.write("Naruto Saseki")

myFile2.write(" sssss")
myFile2.close()
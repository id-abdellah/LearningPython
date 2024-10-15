# ------------------------------------
# --- Lists ---
# ------------------------------------
#
# [1] List is mutable => add, delete, edit
# [2] List items is not unique
# [3] List can have different data types
# ------------------------------------

# وخا كدير نفس الخدمة array فاللغات لوخرين ولكن ماشي array بحالها بحال ال list دبا قالك ال
# array فيه ال numpy خارجي سميتو module هنا فالبايثون خاصنا واحد ال arrays حيت باش نقدو نستعملو ال


myAwesomeList = ["one", "two", "three", 1, 2, True, False]

# indexing مكناش نقدو نديرو قيمة سالبة فال js دبا فال
# هنا لا
print(myAwesomeList[-1]) # False
print(myAwesomeList[-2]) # True

print(myAwesomeList[0:4]) # ['one', 'two', 'three', 1]
print(myAwesomeList[3:len(myAwesomeList)]) # [1, 2, True, False]

# list راه خدامين تالفال strings لي درنا فال indexing slicing خلاصة غاع المسايل ديال ال

print(myAwesomeList[::1]) # ['one', 'two', 'three', 1, 2, True, False]
print(myAwesomeList[::2]) # ['one', 'three', 2, False]
print(myAwesomeList[::3]) # ['one', 1, False]


# ------------------------

# فراه باينة كما العادة list فال item باش تعدل فشي
myAwesomeList[0] = "zero"
myAwesomeList[1] = "000000"
myAwesomeList[-1] = 100000
print(myAwesomeList) # ['zero', '000000', 'three', 1, 2, True, 100000]


# باش تعدل على قطعة كاملة slicing ويمكن ليك حتا تدير ال
# باش يعوض بقيمتهم list غار هو خاص دير القيم ديال
# list من ال slicing خاوية كيمسح العناصر لي خديتي فال list الا خليتي ال

myAwesomeList[0:2] = ["1", "2"]
print(myAwesomeList) # ['1', '2', 'three', 1, 2, True, 100000]

# لي خديتي slices على str غيقسم العناصر ديال ال list بلاصة str فحالة درتي
# عادي list اما لدرتي كتر من القيم لي خديتي ف كيزيدهم فال

myAwesomeList[0:2] = "abcd"
print(myAwesomeList) # ['a', 'b', 'c', 'd', 'three', 1, 2, True, 100000]

myAwesomeList[0:4] = [1, 2, 3, 4]
print(myAwesomeList) # [1, 2, 3, 4, 'three', 1, 2, True, 100000]

myAwesomeList[4:] = [5]
print(myAwesomeList) # [1, 2, 3, 4 5]
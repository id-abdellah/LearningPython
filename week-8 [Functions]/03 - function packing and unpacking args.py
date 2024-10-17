# -----------------------------------------------
# ---- Function - Packing and Unpacking args ----
# -----------------------------------------------
# 
# *args
# -----------------------------------------------

# فالجافاسكريبت spread تقريبا نفس القضية ديال ال
# فيها عناصر مجموعين تقد تفككهم list اي انها مثلا لعندك شي
# كما كتشوف التحت data type فعليا كتقد تفكك اي

myList = [1, 2, 3, 4]
myTuple = ("a", "b", "c")
myString = "obito"
mySet = {11, 22, 33, 44}
myDict = {"aa": 100, "b": 200, "c": 300}
print(*myList) # 1 2 3 4
print(*myTuple) # a b c
print(*myString) # o b i t o
print(*mySet) # 33 11 44 22
print(*myDict) # aa b c



# js بحال تقريبا ال astrics كدير ال function لي غدخل فشي args كما كتشوف التحت فاش مكتعرفش عدد ال
# loop و تقد دير عليه Tuple بالنسبة للمتغير لي كيرجع كيكون نوعو

def sayHello1(*friends):
    # type(friends) => tuple
    for name in friends:
        print(f"Hello {name}")

sayHello1("Mohamed", "Ahmed", "Sayed", "Obito")



# js بحال لي فال rest parameters ايضا كتخدم بيها ك
# فاللخر unpacking var غار شريطة يكون ال

def showDetails(name, *skills):
    print(f"Hello Mr.{name} ur skills are: ")
    for skill in skills:
        print(skill)
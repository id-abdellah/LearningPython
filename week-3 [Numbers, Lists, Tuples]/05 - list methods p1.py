# ------------------------------------
# --- List methods p1 ---
# ------------------------------------
#
# append(obj: any)
# extend(iterable) => the same thing as spread operator in js
# remove(value)
# sort(reverse=False | True) => reverse by default is False. mutate original array
# reverse() => reverse list. and mutate original array
# ------------------------------------


# ------------------------------------
# append(obj)

# من اللخر ديالها list باينة كضيف عناصر اخرين من اي نوع لل append ال

myList_1 = [1, 2, 3]
myList_2 = ["a", "b", "c"]

myList_1.append(4)
myList_1.append(True)
myList_1.append(myList_2)
print(myList_1) # [1, 2, 3, 4, True, ['a', 'b', 'c']]


# ------------------------------------
# extend(iterable)

# واحد element كاملة شدها حطها كاملة ك list فاش درنا append فال
# و لكن كتفرق العناصر ديالها list لل string او list سواء iterable الخدمة ديالها انها كضيف extend ال

a = [1, 2, 3]
b = ["a", "b", "c"]

a.extend(b)
a.extend("ef")

print(a) # [1, 2, 3, 'a', 'b', 'c', 'e', 'f']


# ------------------------------------
# remove(value)

# list من ال element هادي باينة الخدمة ديالها انها كتمسح شي
# ولكن فحالة عندك مثلا شي قيم معاودين ف هي كتمسح فقط اول واحد جا فطريقها

x = [1, 2, 3, 4, 5]
x.remove(3)

print(x) # [1, 2, 4, 5]



# ------------------------------------
# sort()

# arrayt لل sort هادي باينة كدير
# كترتبهم ليك تصاعديا by default ولكن هي
# True بالقيمة reverse flag الا بغتي تنازليا كدير ال

# error غرجع str اي الارقام اما لدرتي فيها int من ال list كتقبل منك فقط sort ال

# intergers يما string غار متخلطهمش ليه, يما strings ولكن ايضا كيرتب ال

y_1 = [1, -100, -1, 20, 3, 30, -90]
y_2 = [1, -100, -1, 20, 3, 30, -90]
y_3 = ["d", "c", "a", "z"]

y_1.sort() 
y_2.sort(reverse=True) 
y_3.sort() 

print(y_1) # [-100, -90, -1, 1, 3, 20, 30]
print(y_2) # [30, 20, 3, 1, -1, -90, -100]
print(y_3) # ['a', 'c', 'd', 'z']



# ------------------------------------
# reverse()

# list هادي باينة كتعكس ال

z = [1, 2, 3, "a", "b", True]
z.reverse()

print(z) # [True, 'b', 'a', 3, 2, 1]

# ------------------------------------
# ------------------------------------
# --- List methods p2 ---
# ------------------------------------
#
# clear() => remove all items from list
# copy() => retrun shallow copy of list
# count(value) => return a number of occurences of a value
# index(value) => return index of a value
# insert(index, object) => insert an object before the index
# pop(index) => return and remove the element of that index
# ------------------------------------



# ------------------------------------
# clear()

a = [1, 2, 3, 4]
a.clear()
print(a) # []


# ------------------------------------
# copy()

# list هادي باينة كدير نسخة من
# shallow copy ولكن

b = [1, 2, 3, 4]

c = b.copy()

b.append(5)

print(b) # [1, 2, 3, 4, 5]
print(c) # [1, 2, 3, 4, 5]



# ------------------------------------
# count(value)

#  list وكترجع ليك شحال من مرة تعاودات فال value هادي تاهي باينة كتعطيها

d = [1, 1, 2, 3, 4, 1, 1, 5]

print(d.count(1)) # 4



# ------------------------------------
# index(value)

# ديال القيمة لي غتعطيه ليه index تاهادي باينة كترجع ليك ال
# كيقابلو يعني لكانت القيمة مضوبلة غترجع ليك اندكس ديال اول واحد index كترجع اول

e = ["a", "b", "c", "d", "c", "e", "f"]

print(e.index("c")) # 2



# ------------------------------------
# insert(index, object)

# كضيف من اللخر append غار ال append هادي كدير نفس الخدمة ديال ال
# list وهادي كضيف فلبلاصة لي بغيتي فال

# لي درتي index قبل ال object و كتضيف هاد ال object و index كتعطيها

f = ["a", "b", "c", "d", "f", "g"]

f.insert(-1, 10) # accepts negativ indexing
f.insert(0, 100)
f.insert(3, 300)

print(f) # [100, 'a', 'b', 300, 'c', 'd', 'f', 10, 'g']



# ------------------------------------
# pop(index)

# js هادي بحال لي كاينة فال
# من الليست و كترجعها ليك index و كتمسح القيمة لي كاينة فديك ال index كتعطيها

# هو اللخر يعني الا مدرتيش الاندكس ايبقا يرجع و يمسح الاندكس اللخر default index ال

g = ["Obito", "Saski", "Kakashi", "Madara", "Naruto", "Konoha"]

print(g.pop(0)) # Obito
print(g.pop(-1)) # Konoha, accept negativ indexing
print(g.pop(3)) # Naruto

print(g) # ['Saski', 'Kakashi', 'Madara']
# ------------------------------------
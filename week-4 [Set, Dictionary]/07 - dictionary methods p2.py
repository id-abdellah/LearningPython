# --------------------------------------
# ---- Dictionary Methods p2 ----
# --------------------------------------
#
# setDefault()
# popitem()
#   returns and remove the last item u added to the dictionary
#   the returns data is "Tuple (key, value)"
#
# items()
# dict.fromKeys(iterabl, value)
# --------------------------------------



# --------------------------------------
# setDefault()

# شوف المثال التحت من بعد نشرحوا

a = {
    "name": "Obito"
}
print(a) # {'name': 'Obito'}
print(a.setdefault("name", "Mohamed")) # Obito
print(a.setdefault("age", 21)) # 21
print(a.setdefault("country")) # None
print(a) # {'name': 'Obito'}

# dict لي عطيتي ليها فكترجع ليك القيمة الاصلية ديالو فال key الا لقات ال setDefault هاد ال
# جديد بالقيمة لي غتعطيه ليها و غترج ليك القيمة key اما لملقاتوش ف كتنشئ
# None غتولي value فقط فال key فحالة درتي فيها ال
# ولي كيرمزو للاشي js فال Null هي بحال ال None هاد ال

# --------------------------------------



# --------------------------------------
# popitem()

# dict ضفتيها فال key كترجع ليك اخر popitem() هاد ال
# dict وبطبيعة الحالة فاش كترجعو كتمسحو من ال

# tuple كنوع key value pairs ولكن خاص تعرف بلي كترجع ليك ال
# كيكون العنصر التاني value وال tuple كيكون العنصر اللول فال key يعني ال

b = {
    "name": "mohamed",
    "age": 21,
    "country": "MR"
}

print(b.popitem()) # ('country', 'MR')
print(b.popitem()) # ('age', 21)
print(b) # {'name': 'mohamed'}

# --------------------------------------



# --------------------------------------
# items()

# فقط keys لي كيرجع ليك ال keys كانت عندنا حاجة سميتها
# فقط values لي كيرجع ال values وكان عندنا

# keys values paire كلها يعني ال items اما هادي فكترجع ال

# tuple ف item فيها كل list كيرجعو على هيئة items ال

c = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
}

print(c.items()) # dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)])


# --------------------------------------


# --------------------------------------
# dict.fromKeys(iterable, value)

# keys بدوك ال dict وكترد ليك value و كتقبل ايضا tuple str list يا iterable فشي keys هادي كتعطيها

myKeys1 = ("keyOne", "keyTwo", "keyThree")
myKeys2 = ["keyList1", "keyList2", "keyList3"]
myKeys3 = "Obito"
myValue = 100

print(dict.fromkeys(myKeys1, myValue)) # {'keyOne': 100, 'keyTwo': 100, 'keyThree': 100}
print(dict.fromkeys(myKeys2, myValue)) # {'keyList1': 100, 'keyList2': 100, 'keyList3': 100}
print(dict.fromkeys(myKeys3, myValue)) # {'O': 100, 'b': 100, 'i': 100, 't': 100, 'o': 100}

# --------------------------------------
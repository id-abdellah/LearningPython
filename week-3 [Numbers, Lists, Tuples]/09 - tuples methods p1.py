# ------------------------------------
# --- Tuples Methods ---
# ------------------------------------
#
# Tuple with one element => (value,) || value,
# Tuple concatenation => (a, b, c) + (d, e) == (a, b, c, d, e)
# Repeat (*)
#   "str" * 3 = "strstrstr"
#   (1, 2) * 3 = (1, 2, 1, 2, 1, 2)
#   [1, 2] * 3 = [1, 2, 1, 2, 1, 2]
# 
# count(value) & index(value) methods
#
# tuple destruct
# 
# ------------------------------------


# فيه عنصر واحد tuple دبا المشكل عندنا غيولي ملي يكون عندنا
# حيت لكان عندنا فيه عنصر واحد. اللغة غترف على نوع البيانات ديال داك العنصر

a = (200)
b = "Obito"

print(type(a)) # int
print(type(b)) # str

# tuple باش نحلو هاد المشكل خاصنا نزيدو فاصلة فاللخر باش نقولو ليه بلي هداك راه

a = (200,)
b = "Obito",

print(type(a), len(a)) # tuple 1
print(type(b), len(b)) # tuple 1




# ---- Tuple concatenation ----

c = (1, 2, 3)
d = (4, 5)

e = c + d + ("A", True)

print(e) # (1, 2, 3, 4, 5, 'A', True)



# ---- Tuple, List, String repeat (*) ----

# اكثر من مرة ساهلة فالبايثون string او انك تعاو مثلا ال repeat دبا موضوع ال
# strings tuples lists حيت كتخدم غا بعلامة الضرب و كتقد تعاود ال

myStr = "Mohamed"
myList = [1, 2]
myTuple = ("a", True)

print(myStr * 5) # MohamedMohamedMohamedMohamedMohamed
print(myList * 5) # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 5) # ('a', True, 'a', True, 'a', True, 'a', True, 'a', True)




# --- count(value) & index(value) methods ---

myTuple_8 = (1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1)

print(myTuple_8.count(1)) # 5

print(f"the position of 7 in the list is: {myTuple_8.index(7)}") # the position of 7 in the list is: 6
print("the position of 7 in the list is: {:d}".format(myTuple_8.index(7))) # the position of 7 in the list is: 6




# --- Tuple destruct ---

# js لي فال destructuring نفس ال

# كدير المتغيرات لي بغيتي تستخرج باي سمية tuple destruct فال
# tuple لل assign و كتخليهم ي
# _, كدير tuble لشي قيمة فال ignor فاش كتبغي دير

h = ("a", "b", 200,"c")

x, y, _, z = h

print(x, y, z) # a b c

help(tuple)
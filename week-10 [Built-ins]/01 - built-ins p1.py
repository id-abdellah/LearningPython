# ---------------------------------------------
# ---- Built-in Functions P1 ----
# ---------------------------------------------
#
# all(iterable) => returns True if all iterable elements is True
# any(iterable) => returns True if at least on element in an iterable is True
# bin(num) => return binary representation of a number
# id() => return id of value on the memory
# ---------------------------------------------


# ---------------------------------------------
# all()

# // True كترجع True وكتشوف واش عاغ العناصر iterable كتقبل منك all ال
# // false كترجع false كان عنصر واحد

a = [1, 2, 3, 4, 0]

if all(a):
    print("all list elements are True")
else:
    print("there is at least one false element")


# ---------------------------------------------
# any()

# all عكس ال any ال

# true هو list الا كان على الاقل عنصر واحد فال true كترد any حيت ال
# false كترجع false الا كان كولشي

if any(a):
    print("there is at least one true element")
else:
    print("there is no any true element")


# ---------------------------------------------
# bin()

# binary هادي كترد ال
# يعني كتعطيها عدد عشري وكترد الصيغة الثنائية ديالو

print(bin(3)) # 0b11
print(bin(10)) # 0b1010


# ---------------------------------------------
# id()

# memory دبا حنا عارفين ان المتغيرات هي وسيلة مكتخزنش البيانات و انما كتشير للبلاصة ديالها فال
# memory يعني اي بيانات دخلناهم كتكون عندهم بلاصة فال
# باش نعرفو بلاصتو فيناهي بالضبط id يعني كلشي عندو

# memory ديال الداتا فال id كترد لينا ال id() ال

x = 10
z = 200

print(id(x)) # 140731762604760
print(id(z)) # 140731762610840

# ---------------------------------------------
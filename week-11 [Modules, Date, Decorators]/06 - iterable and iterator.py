# ----------------------------------------------------------------
# ---- Iterable & Iterator ----
# ----------------------------------------------------------------
# 
# ----------------------------------------------------------------
# Iterable
# [1] Object contains data that can be iterated 
# [2] Like (str, list, set, tuple, dict)
# ----------------------------------------------------------------
# Iterator
# [1] Object used to iterate over iterable using next() method return 1 element at a time
# [2] You can generate iterator From iterable when using iter() method
# [3] For loop already calls iter() on the iterable behinde the scene
# [4] Gives "StopIteration" if ther is no next element
# ----------------------------------------------------------------

# هي لي كتجيب لينا عنصر مورا عنصر next() دبا عندنا
# loop باش يدار عليه iterator لل iterable ولي كيحول iter() وعندنا

# شوف المثال التحت باش تفهم
# يحبس loop باش ال StopIteration فاش مكيكونش شي عنصر باقي. كترجع next ديك ال

myStr = "obito"

myIterator = iter(myStr)

print(next(myIterator))# o
print(next(myIterator))# b
print(next(myIterator))# i
print(next(myIterator))# t
print(next(myIterator))# o


# كيما كتشوف التحت iter كتستعمل loop وخلف الكواليس. ال

for s in iter(myStr):
    print(s)
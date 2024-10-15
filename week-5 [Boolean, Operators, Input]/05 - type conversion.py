# --------------------------------------
# ---- Type Conversion ----
# --------------------------------------
#
# --------------------------------------

# وهي قضية تحويل البيانات من نوع لنوع


# str() and int()
# فيما يخص الارقام int string float تقد تحول مابين ال

a = 10
b = 20.2

print(type(a), type(b)) # int float
print(type(str(a)), type(str(b))) # str str

print(type("50")) # str
print(type(int("50"))) # int


print("#" * 50)



# tuple(itrable)
# set list dict str بحال tuple لل iterable ايضا تقد تحول اي
# keys كياخذ فقط ال dictionary بالنسبة لل

print(tuple("Obito")) # ('O', 'b', 'i', 't', 'o')
print(tuple([1, 2, 3, 4, 5])) # (1, 2, 3, 4, 5)
print(tuple({"A", "B", "C"})) # ('A', 'B', 'C')
print(tuple({"aa": 1, "bb": 2, "cc": 3})) # ('aa', 'bb', 'cc')


print("#" * 50)


# list(iterable)
# list لل iterable ايضا تقد تحول اي

print(list("Obito")) # ['O', 'b', 'i', 't', 'o']
print(list((1, 2, 3, 4, 5))) # [1, 2, 3, 4, 5]
print(list({"A", "B", "C"})) # ['B', 'A', 'C']
print(list({"aa": 1, "bb": 2, "cc": 3})) # ['aa', 'bb', 'cc']



print("#" * 50)



# set()

print(set("Obito")) # {'b', 'o', 'i', 't', 'O'}
print(set((1, 2, 3, 4, 5))) # {1, 2, 3, 4, 5}
print(set(["A", "B", "C"])) # {'A', 'B', 'C'}
print(set({"aa": 1, "bb": 2, "cc": 3})) # {'bb', 'cc', 'aa'}


print("#" * 50)


# dict()

# dict متقدش تحولو ل str اولا ال
# dict متقدش تحولو ل set تا ال


# key value فيهم جوج عناصر nested tuples تكون فيها tuple خاص ال dict ل tuple باش تحول ال
# list نفس الحاجة بالنسبة لل

tupleToDict = (("key1", 100), ("key2", 200), ("key3", 300))
listToDict = [["key1", 400], ["key2", 500], ["key3", 600]]

print(dict(tupleToDict)) # {'key1': 100, 'key2': 200, 'key3': 300}
print(dict(listToDict)) # {'key1': 400, 'key2': 500, 'key3': 600}



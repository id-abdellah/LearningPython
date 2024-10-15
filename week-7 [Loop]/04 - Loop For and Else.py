# ----------------------------------------------------
# ---- For Loop ----
# ----------------------------------------------------
# 
# Syntax
#
# for item in iterable:
#   Block of Code
# else:
#   Code will run once the loop ends
# ----------------------------------------------------

# مفيهش شرط كيتحقق python بالنسبة لل loop for ال
# iterable كيشد كيدوز على غاع العناصر فال variable و كتمسي iterable و انما كتعطيها

myList = ["a", "b", "c", "d", "e", "f", "g"]

for letter in myList:
    print(letter)
else:
    print("letters ends")


myStr = "Obito"

for s in myStr:
    print(f"[ {s.upper()} ]")
else:
    print("str ends")


myDict = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

for key in myDict: 
    print(key)
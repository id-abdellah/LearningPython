# ------------------------------------
# --- string methods p4 ---
# -------------------------
# 
# replace(oldValue, newValue, count)
# join(iterable)
#   "separator".join([] | ())
# ------------------------------------



# -------------------------------------------------
# replace(oldValue, newValue, count)


a = "one one two two one one three three"

print(a.replace("one", "1")) # 1 1 two two 1 1 three three
print(a.replace("one", "1", 2)) # 1 1 two two one one three three



# -------------------------------------------------
# join(iterable)

# list or tuple سواء iterable كتقبل منك join ال
# iterable فيه ال join عاد دير seperator فيه string ولكن باش تخدم بيها خاصك هو اللول تسبق
# string يكون iterable ولكن خاص المحتوى ديال ال

myList = ["o", "b", "i", "t", "o"]

print("-".join(myList)) # o-b-i-t-o
print(" ".join(myList)) # o b i t o
print("".join(myList)) # obito
print(", ".join(myList)) # o, b, i, t, o

# -------------------------------------------------
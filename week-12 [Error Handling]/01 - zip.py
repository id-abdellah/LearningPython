# -----------------------------------------------------------
# ---- Zip ----
# -----------------------------------------------------------
#
# zip() return a zip object contains all objects
# zip() length is the length of lowest object
# -----------------------------------------------------------


# tuple نوع iterator كيرجع ليك zip على حسب مافهمت ان ال

# واحد loop واحد ب object وكيضغطهم ف objects لي كيدير وهو انه كتعطيه
# ويحطهم مع بعض ويدوز للعنصر التاني من كل واحد وهي غادة object واحد. كياخذ العنصر اللول من كل loop يعني كيدير

# ديال اصغر واحد فدوك لي عطيتيته length هو ال zip ديال length متفاوت. كيولي ال length ب objects ملي كتعطيه

myStr = "abcdef"
myList = [1, 2, 3, 4, 5, 6]
myTuple = ("A", "B", "C", "D", "E", "F")


myZip = zip(myStr, myList, myTuple)


print(myZip) # <zip object at 0x000001EFD7453C00>
print(tuple(myZip)) 
# (('a', 1, 'A'), ('b', 2, 'B'), ('c', 3, 'C'), ('d', 4, 'D'), ('e', 5, 'E'), ('f', 6, 'F'))

for el in myZip:
    print(el)

# ('a', 1, 'A')
# ('b', 2, 'B')
# ('c', 3, 'C')
# ('d', 4, 'D')
# ('e', 5, 'E')
# ('f', 6, 'F')




print("*" * 40)


# الاصغر length كياخذ ال zip ديالو صغير على لوخرين. ال length ال object كما قلنا فاش كيكون عندك


ls = [1, 2, 3, 4, 5, 6, 7, 8]
st = "abc"
tp = (10, 20, 30, 40)

myZip2 = zip(ls, st, tp)


for l in myZip2:
    print(l)

# (1, 'a', 10)
# (2, 'b', 20)
# (3, 'c', 30)
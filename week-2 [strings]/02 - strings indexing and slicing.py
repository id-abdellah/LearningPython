# -----------------------------
# Indexing and slicing
#
# [1] all data in python is object
# [2] object contains many elements or single
# [3] every element has its own index
# [4] python use zero based index (index starts from 0)
# [5] use [] square brackets to access elements
# -----------------------------


# indexing (Access single item)
# 
# syntax:
#   string[n]

myString = "Obito Uchiha"

print(myString[0]) # O
print(myString[6]) # U

print(myString[-1]) # a
print(myString[-3]) # i



# --------------------------------------------



# slicing (Access multiple sequence items)
#  
# syntax:
#   string[start:end] *the end not included
#   string[start:end:steps] 

print(myString[9:12]) # iha
print(myString[1:5]) # bito

# كما العادة الا مدرتيش منين يبدا غيبدا افتراضيا من الزيرو
print(myString[:5]) # Obito

# ويلا مدرتيش تالفين ايوقف فغيبدا من البداية لي عطيتي ليه تاللخر ديال السترينغ
print(myString[6:]) # Uchiha

# كامل string ويلا مدرتيش لابداية ولا نهاية غيرد ليك ال
print(myString[:]) # Full string



# كتكون 1 by default فهي steps بالنسبة لقضية ال
# steps ف كيبدا من البداية لي عطيتيه و كينقز الحروف على قد القيمة ديال steps فاش كتزيد قيمة ال
print(myString[0::1]) # full string
print(myString[::1]) # full string
print(myString[::2]) # OioUhh
print(myString[::3]) # OtUi
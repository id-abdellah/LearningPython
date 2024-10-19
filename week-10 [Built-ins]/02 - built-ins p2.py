# ---------------------------------------------
# ---- Built-in Functions P2 ----
# ---------------------------------------------
#
# sum(iterable, startValue)
# round(num, nDigits)
# range(start, end, step)
# print()
# ---------------------------------------------


# ---------------------------------------------
# sum()

# // وكدير المجوع ديال الارقام لي فيها iterable كتعطيها sum ال
# // التاني فهو بحال لقلتي الرقم لي غيزيدو على داك المجموع param اما بالنسبة لل

a = [1, 22, 10, 20, 40]
print(sum(a)) # 93
print(sum(a, 100)) # 193



# ---------------------------------------------
# round(num, ndigits)

# // هادي باينة كتقرب ليك العدد
# // لي كتخلي شوية الدقة فتقريب تا الجزئ العشري ndigit params غار الحاجة المزيودة هنا وهي ديك ال


print(round(5.499)) # 5
print(round(5.500)) # 6
print(round(5.548, 2)) # 5. 55




# ---------------------------------------------
# range(strt, end, step) 

print(list(range(11))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 3))) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


# ---------------------------------------------
# print()

print("hello", "bruh", "how", "are", "u", sep="@") # hello@bruh@how@are@u
print("hello", "bruh", "how", "are", "u", sep=" /\ ") # hello /\ bruh /\ how /\ are /\ u


print("first line", end=" itsTheEnd ")
print("second line", end="\t\t\t\t")
print("third line")
# first line itsTheEnd second line                                third line
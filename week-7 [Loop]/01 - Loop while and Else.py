# ----------------------------------------------------
# ---- Loop While and Else ----
# ----------------------------------------------------
#
# syntax
#
#   while condition_is_True:
#       Block of Code
#   else
#       Block of code => will run once condition becomes False
# ----------------------------------------------------


# // نفس الكونسبت مكاينش تغيير while loop ال


# // else وهي ديك ال python الحاجة لي مزيودة هنا فال

# // كتخدم مرة وحدة else ال False انفوا كيولي while loop كتخدم الكود لي فيها انفوا كيولي الشرط ديال else ال


a = 0

while a <= 10:
    print(a)
    a += 1
else:
    print("count till 10 is done.")



print("#" * 50)


# -------------------------
# ---- Training
# -------------------------

myFriend = ["Simo", "Ahmed", "Sara", "Mahmoud", "Khaled", "Ziko", "Firdaous", "Arinas", "Yassmine", "Obito"]

i = 0
while i < len(myFriend):
    print(f"#{str(i + 1).zfill(2)} - {myFriend[i]}")
    i += 1
else:
    print("All friends are printed to screen.")

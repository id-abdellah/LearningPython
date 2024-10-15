# ----------------------------------------------------
# ---- Membership operators ----
# ----------------------------------------------------
#
# in
# not in
# ----------------------------------------------------

# الخاصين بالعضوية operators كيتسماو ايضا ال

# علاش سماوها العضوية

# وبغيتي تشوف واش شي عنصر عضو فيها اولا لا زعما واش كاين فيها list حيت مثلا كتكون عندك



# strings (case sensetive)

name = "Obito"

print("O" in name) # True
print("i" in name) # True
print("j" in name) # False




print("#" * 40)



# list

friends = ["osama", "reda", "simo"]

print("simo" not in friends) # False
print("osama" in friends) # True



print("#" * 40)


# Tuple
print(10 in (1, 2, 3, 4, 10)) # True

# Dict
print("key6" in {"a": 1, "key1": 2, "key6": 0}) # True

# set
print("A" in {1, 2, 20, "a"}) # False
print("A" not in {1, 2, 20, "a"}) # True
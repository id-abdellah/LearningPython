# --------------------------------------
# ---- Practical Email Slice ----
# --------------------------------------
#
# --------------------------------------

email = input("your email here please: ")

firstPart = email[0:email.index("@")]
secondPart = email[email.index("@") + 1:email.index(".")]
lastPart = email[email.index(".") + 1:] 

print(firstPart)
print(secondPart)
print(lastPart)
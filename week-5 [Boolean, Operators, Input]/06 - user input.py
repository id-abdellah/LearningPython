# --------------------------------------
# ---- User Input ----
# --------------------------------------
#
# retruns string
# --------------------------------------



# باينة كطلب من اليوزر يدخل قيمة معينة user input ال

# ديال الكود تادخل قيمة عاد كتكمل execution كتوقف ال input ولكن لي خاص تعرف ان ال



fName = input("What is your first name: ")
mName = input("What is your middle name: ")
lName = input("What is your last name: ")
age = input("your age is: ")


fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello sir: {fName} {mName:.1s} {lName} {age} years old Happy to see u again")
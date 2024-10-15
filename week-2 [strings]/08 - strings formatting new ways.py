# ------------------------------------
# --- string Formatting new ways ---
# ------------------------------------
#
# باختصار الطريقة لي دوينا عليها قبل كتعتابر قديمة و غير مستعملة دبا
# باقين جوج طرق جداد هوما لي كيتستعملو بزاف وهوما هادو لي فلتحت
#
# "str {} {}".format(a, b)
# f"str {var} {var}" => version 3.6+
# 
#
#  مكملش هنا وانما هو موضوع كبير وباقي فيه ميتقال string formatting موضوع ال
# pyFormat.info
#  دخل مرة مرة باش تعلم حوايج جداد string formatting هادا موقع مختص فقط فقضية ال
# ------------------------------------


# --------------------------------------------
# str.format()
# {:d}
# {:f}
# {:s}

# curly brackets {} بالنسبة لهذه الطريقة ف بحالها بحال اللولة غار هادي كنتعملو فيها

name = "mohamed"
age = 21
language = "python"

print("name is: {:s} and age is: {:d} and lang is: {:s}".format(name, age, language))


# controle floating numbers

height = 1.734958

print("my height is: {:.2f}".format(height)) # my height is: 1.73


# Truncate strings

print("hello {:.4s}".format("abcdefgh")) # hello abcd


# format money

myMoney = 593928442343

print("money in the bank is: {:_d}".format(myMoney)) # money in the bank is: 593_928_442_343
print("money in the bank is: {:,d}".format(myMoney)) # money in the bank is: 593,928,442,343


# reArrange items
# عندك الامكانية انك تغير ترتيب

a, b, c = 1, 2, 3

print("hello {:d} {:d} {:d}".format(a, b, c)) # hello 1 2 3
print("hello {2} {1} {0}".format(a, b, c)) # hello 3 2 1
print("hello {2} {0} {1}".format(a, b, c)) # hello 3 1 2

e, f, g = 10, 20, 30

print("hello {1:d} {2:d} {0:d}".format(e, f, g)) # hello 20 30 10
print("hello {:d} {:f} {:f}".format(e, f, g)) # hello 10 20.000000 30.000000
print("hello {2:.2f} {0:.1f} {1:.3f}".format(e, f, g)) # hello 30.00 10.0 20.000



# --------------------------------------------
# f"str"

animeName = "sosou no freiren"
releaseDate = 2023
langs = ["japanes", "english", "arabic"]

fullInfos = f"""
anime name: {animeName}.
release date: {releaseDate}.
languages: {", ".join(langs)}
"""

print(fullInfos)

#anime name: sosou no freiren.
# release date: 2023.
# languages: japanes, english, arabic
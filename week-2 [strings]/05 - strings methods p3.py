# ------------------------------------
# --- string methods p1 ---
# -------------------------
# 
# index(subs: mand, start, end) throws an error when fail
# find(subs: mand, start, end) return -1 when fail

# rjust(width, fillChar)
# ljust(width, fillChar)

# splitlines(keepEnd = False)
# expandtabs(tabSize)

# isalpha() [a-z A-Z]
# isidentifier()
# isdigit() [0-9]
# islower()
# isupper()
# isspace()
# isalnum() [a-z A-Z 0-9]
# ------------------------------------



# ----------------------------------------------------
# index() & find()

# بجوجهم كيديرو نفس الخدمة بالضبط index وال find ال
# لي باغي تقلب عليها substring ديال ال index وهي انهم كيردو ليك ال

# الفرق بيناتهم وهو
# يعني الكود غيدار ليه بلوك error فاش مكيلقاش الحاجة لي بغيتي تقلب عليها غيلوح index ان ال
# غترجع ليك -1 find اما ال

a = "i love python"

print(a.index("p")) # 7
# print(a.index("p", 0, 5)) # 7 => will throw an Error

b = "i love python"
print(b.find("p")) # 7
print(b.find("p", 0, 5)) # -1



# ----------------------------------------------------
# rjust(width, fillChar) & ljust(width, fillChar)

# كيخدم على الجناب بجوج zfill بالضبط غا ال zfill بحالهم بحال ال
# وهادو وحدة كتخدم على الليمن وحدة على الليسر

c = "obito"

print(c.rjust(len(c) + 5, "*")) # "*****obito"
print(c.ljust(len(c) + 5, "*")) # "obito*****"



# ----------------------------------------------------
# splitlines(keepEnd = False)

# فيها كتر من سطر string هادي فحالة عندك
# list فال element كل سطر كترجعو ليك ف

d = """first line
second line
third line
fourth line
"""

print(d.splitlines()) # ['first line', 'second line', 'third line', 'fourth line']
print(d.splitlines(True)) # ['first line\n', 'second line\n', 'third line\n', 'fourth line\n']



# ----------------------------------------------------
# expandtabs(tabSize)

# string لي فال tabs هادي باينة, وهي انها فاش تقدر تحكم فعدد المسافات لي غتكون فال

e = "obito\tuchiha\tmadara"

print(e) # obito   uchiha  madara
print(e.expandtabs(2)) # obito uchiha  madara
print(e.expandtabs(10)) # obito     uchiha    madara



# ----------------------------------------------------
#  boolean كيرجعو methods هاد ال
# ونتا غادي digite اولا upper اولا lowe اولا title واش هيا string على ال check من خلالهم كتقد تدير

# istitle()
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # True
print(two.istitle()) # False

# isalpha() => is alphabetic string
print("abc".isalpha()) # True
print("abc1".isalpha()) # False

# isidentifier()
# صالح بحال انه ميبداش بالارقام الخ variable هي المعايير لي خاص تكون باش يكون شي identifier ال
print("obito".isidentifier()) # True
print("obito_var".isidentifier()) # True
print("obito100var".isidentifier()) # True
print("obito--var".isidentifier()) # False

# isdigit() => if all string is digits
print("1234".isdigit()) # True
print("1234B".isdigit()) # False

# islower() & isupper()
print("abc".islower()) # True
print("ABC".isupper()) # True

# isspace()
print(" ".isspace()) # True

# isalnum() [a-z A-Z 0-9]
print("ab12".isalnum()) # True
print("abc".isalnum()) # True
print("123".isalnum()) # True
# ----------------------------------------------------
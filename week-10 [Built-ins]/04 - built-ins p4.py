# ---------------------------------------------
# ---- Built-in Functions P4 ----
# ---------------------------------------------
#
# enumerate(iterable, start)
# helpe(method)
# reversed(iterator)
# ---------------------------------------------


# enumerate()

# بحال الا قلتي هو عداد enumerate ال
# iterables وكخدم على ال
# ولي كيعني الرقم لي غيبدا منو العد start لي هو second arg وعندو

# معاه ال العدد ديالو tuple فيه كيديرو ف element لي كتعطيه كل iterator بنسبة لطريقة العمل وهو انه ال

# enumerate كيقول ليك هو enumeratedIterator فاش كدير نوع البيانات ديال

mySkills = ["html", "css", "js", "sass"]

mySkillsEnumerated = enumerate(mySkills, 10)
print(type(mySkillsEnumerated)) # <class 'enumerate'>
print(list(mySkillsEnumerated)) # [(10, 'html'), (11, 'css'), (12, 'js'), (13, 'sass')]
for n, sk in mySkillsEnumerated:
    print(n, sk, sep=" => ")



# helpe(method)

# وكترد ليك المعلومات دالاستخدام ديالها method name هادي باينة الفكرة ديالها وهي انك كتعطيها


# reversed(iterator)

# لي كتعطيها iterator لل reverse هادي كدير
# عليه loop غار هو مكتمكنكش طبعو نيشان و انما باش تلاحظ بلي معكوس خاص

# في العناصر معكوسين iterator object يعني كترد

# list method تخدم بال list يعني خاص لبغيتيهم ف

mystr = "Obito"
s = reversed(mystr)

print(s) # <reversed object at 0x000001AE2A825E70>
print(list(s)) # ['o', 't', 'i', 'b', 'O']
for l in s:
    print(l)

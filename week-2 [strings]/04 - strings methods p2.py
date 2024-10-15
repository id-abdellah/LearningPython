# ------------------------------------
# --- string methods p2 ---
# -------------------------
# 
# split(sep, maxSplit) & rsplit(sep, maxSplit)
# center(width: Mand, fillChar: opt)
# count(substring, start, end) 
# swapcase()
# startswith(subs: mand, start: opt, end: opt)
# endswith(subs: mand, start: opt, end: opt)
# ------------------------------------




# ------------------------------------------------------
# split(sep, maxSplit) & rsplit()

# لي تعطيها separator بناء على ال string فالجافاسكريبت وهي انها كتقسم ليك ال split() بحالها بحال ال
# list وتردها ليك ك

# لي بغيتي split التاني كيعني شحال الماكس ديال ال arg ال
# كيردو كامل كعنصر واحد string 2 مرات وما تبقى من ال split مثلا درتي 2 كيدير

# فاش مكتحددوش كيقسم من المسافات sep بالنسبة لل

a = "i love js and react and nodeJS"
b = "i-love-js-and-react-and-nodeJS"

print(a.split()) # ['i', 'love', 'js', 'and', 'react', 'and', 'nodeJS']
print(b.split("-")) # ['i', 'love', 'js', 'and', 'react', 'and', 'nodeJS']

print(a.split(" ", 3)) # ['i', 'love', 'js', 'and react and nodeJS']

print(a.rsplit(" ", 3)) # ['i love js and', 'react', 'and', 'nodeJS']



# ------------------------------------------------------
# center(width: Mand, fillChar: opt)

# بالكراكتر لي اتعطيها string كما كتشوف المثال التحت ف هي كتعمر لك الجناب ديال ال
# اللول ضروري انك ديرو, ديال الطول الكلي argument ولكن ال

# طويلة بلا متبقا تحسب شحال فيها string باش لكانت شي len(c) كما كتلاحظ التحت درت

c = "Obito"

print(c.center(len(c) + 6)) # if no fillChar, will be filled by spaces "   c   "

print(c.center(len(c) + 6, "#")) # "###Obito###"



# ------------------------------------------------------
# count(word | letter, start, end)

# string هادي كتعطيها شي حرف اولا كلمة و كتحسب شحال كاين منها فال
# الحروف حساسة
# ديال من فين اتبدا الحساب و تالفين, ولكن اختياريين argument وعندها

d = "i love python and php because php is so easy"

print(d.count("php")) # 2
print(d.count("p")) # 5


# ------------------------------------------------------
# swapcase()

# و العكس small غيردو capital هادي باينة, الحرف لي

e = "ObItO"

print(e.swapcase()) # oBiTo



# ------------------------------------------------------
# startswith(subs: mand, start: opt, end: opt)

# كتبدا بهاد الجملة اولا هاد الحرف ولا لا string يعني واش هاد ال boolean, هادي باينة, كترد
# و كتقبل ايضا موضع البداية و النهاية

f = "i love my mom and my dad so much"

print(f.startswith("i")) # True
print(f.startswith("i lovee")) # False

print(f.startswith("i", 10)) # False
print(f.startswith("mom", 10)) # True



# ------------------------------------------------------
# endswith(subs: mand, start: opt, end: opt)

# كتكمل بهاد الحرف اولا هاد الجملة string واش هاد المقطع اولا هاد ال

print(f.endswith("much")) # True
print(f.endswith("and", 10, 17)) # True
print(f.endswith("o", 0, 3)) # False => "l"
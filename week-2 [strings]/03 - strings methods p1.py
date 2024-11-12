# ------------------------------------
# --- string methods p1 ---
# -------------------------
#
# len(obj) => return the length of given data type. str, list, tuple, dict. but "int" not
#
# .upper() => Convert string to upperCase
# .lower() => convert string to lowerCase
# .strip(chars) => return copy of string with leading and trailing whitspaces removed if no chars was provided
#                 if chars was provided it will remove the leading and trailing chars instead
# .rstrip(chars) & lstrip(charts)
# .title() => return copy of string with every word is capitalized, letter after nums are included
# .capitalize() => return copy of string capitalize only the first letter of it
# .zfill() => Pad a numeric string with zeros on the left, to fill a field of the given width.
# ------------------------------------


# len() => return the length of a string, list, tuple, dictionary
# print(len("Obito Uchiha")) # 12
# print(len([1,2,3,4,5,6,7])) # 7
# print(len((1,2,3,4,5,6,7,8))) # 8
# print(len({"a": 1, "b": 2, "c": 3})) # 3


# -------------------------------------------
# strip(char) rstrip(char) lstrip(char)


# فالجافاسكريبت trim() كاملهم كيديرو نفس الوظيفة وبحالهم بحال ال
# و حدة غا من الليمن ووحدة غامن الليسر string يعني وحدة كتحيد المسافات من الجناب ديال ال
# عطيتيه ليه character ولكن هادي عندها خاصية زيادة وهي مكتحيد غا المسافات وانما اي
# وفاش مكتعطيها والو كتحيد المسافات

a = "    Obito uchiha    "
print(a.strip()) # "a"
print(a.rstrip()) # "    a"
print(a.lstrip()) # "a    "

a = "####Obito uchiha####"

print(a.strip("#")) # "a"
print(a.rstrip("#")) # "####a"
print(a.lstrip("#")) # "a####"

a = "@#@#Obito uchiha@#@#"
print(a.strip("@#")) # "a"
print(a.rstrip("@#")) # "#@#@a"
print(a.lstrip("@#")) # "a@#@#"



# -------------------------------------------
# title() & capitalize()

# upperCase لل string كتحول لك الحرف اللول من كل كلمة فال title() هاد ال
# و ايضا الحروف لي بعد الارقام

# lowerCase ماتبقا كتردو upperCase كامل string فهي كتخلي فقط الحرف اللول من capitalize() اما بالنسبة لل
# الحرف اللول من السترينغ كامل capitalize كتحول الحرف اللول من كل كلمة اما ال title يعني ال

b = "i love 2d graphics and 4g telecom tech"

print(b.title()) # I Love 2D Graphics And 4G Telecom Tech

print(b.capitalize()) # I love 2d graphics and 4g telecom tech



# -------------------------------------------
# zfill(width)

# لي عطيتيها width تا تقاد مع ال 0 بال string هادي من المثال التحت باينة وهي انها كتعمرلك ال
# كبر اولا كيساوي لي عطيتيها ف مكدير والو width ديجا عندها string ولكن فحالة كانت ال

c, d, e, f = "1", "11", "111", "1111"

print(c.zfill(4)) # 0001
print(d.zfill(4)) # 0011
print(e.zfill(4)) # 0111
print(f.zfill(4)) # 1111



# -------------------------------------------
# upper() & lower()

g = "mohamed"

print(g.upper()) # MOHAMED

h = "MOHAMED"

print(h.lower()) # mohamed
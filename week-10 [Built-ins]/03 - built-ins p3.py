# ---------------------------------------------
# ---- Built-in Functions P3 ----
# ---------------------------------------------
#
# abs(num) 
# pow(base, exp, modulus)
# min(item, item, item, ... or Iterator)
# max(item, item, item, ... or Iterator)
# iterator[slice(start, stop, step)]
# ---------------------------------------------


print(abs(100)) # 100
print(abs(-2.99)) # 2.99



print("#" * 40)


# pow()

# pow ولي كترجع باقي القسمة ديال الناتج modulus الحاجة المزيودة هنا وهي ديك ال

print(pow(2, 5)) # 32
print(pow(2, 5, 10)) # (32) % 10 => 2




print("#" * 40)



# min() & max()

# وتانية اكبر رقم iterator هادو كيخدمو بنفس الطريقة ولكن وحدة كتعطي اصغر رقم فال

# كيخدمو على الارقام و الحروف غار خاص ميكونوش مخلطين'

mynums = (1, 20, -1, 30, 81, 100)

print(max(mynums)) # 100
print(min(mynums)) # -1

print(min("a", "b", "c", "x")) # a
print(max("a", "b", "c", "x")) # x




print("#" * 40)

# slice()

# مكاين لاش نعاودو نشرحو الاستخدام ديالها حيت معروف وفايت دزنا عليه

myStr = "abcdefgh"

print(myStr[2:5]) # cde
print(myStr[slice(2, 5)]) # cde
# -----------------------------------------------
# ---- Function - Default Params ----
# -----------------------------------------------
# 
# def fnc(n1, n2, n3):
#   print(n1, n2, n3)
# -----------------------------------------------


# // كيعتامد على الافتراضية function args نفس الكونسبت. كتحط قيمة افتراضية باش لمدخلتيش شي قيمة فال

# غار هو كاينين بعض القوانين ضروريين
# واحد فقط خاص يكون هو اللخر arg ل default value لكنتي غدير
# default value دير ليهم arg اللول خاص غاع ال arg لل default value لكتي باغي دير

def hi(name = "someone", age = 10, country = "unknown"):
    print(f"hello {name} ur age is {age} u live in {country}")


hi("Obito", 200, "Morocco") # hello Obito ur age is 200 u live in Morocco

hi() # hello someone ur age is 10 u live in unknown

hi("moha") # hello moha ur age is 10 u live in unknown
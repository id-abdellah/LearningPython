# ---------------------------------------------
# ---- Modules: intro and built in modules ----
# ---------------------------------------------
# 
# syntax:
#
# import moduleName
# from "moduleName" import aModuleFunction 
# ---------------------------------------------

# // javascript نفس الكونسيبت لي تعودنا عليه فال

# // كامل module ال import هنا تقد ت
# // بلا متجيبو كامل module بوحدها من شي function لشي import اولا تقد دير
import os
from random import random, randint, shuffle


# random module من ال functions التحت هنا خدمت ب
# وبطبيعة الحال كاينين بزاف غير هادو

x = [1, 2, 3, 4, 5, 5, 6, 2, 9]
print(f"Random Float num => ", random())
print(f"Random Int num => ", randint(100, 1000))
shuffle(x)
print(x) # [5, 3, 6, 4, 5, 2, 2, 9, 1]


# لي فيه functions وال methods وبغيتي تعرف غاع ال module فاش كيكون عندك
# كتعاونك فهادشي dir() ال

print(dir(os))
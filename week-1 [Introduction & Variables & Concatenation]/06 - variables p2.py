# ---------------------------------
# -- Variables --
# --------------- 
#
# 
# Some general infos:
#
# Source code : Original code you write it in computer
# Translation : Converting source code into machine code
# Compilation : Translate code before run-time
# Run-Time : Period that app take to executing commands
# Interpreted : Code translate on the fly during execution 
# ---------------------------------

# اي انها مكتفرضش عليك تحدد نوع البيانات فشي متغير dynamically typed language كتعتابر python ال

# reserved keywords كما هو متعارف عليه وهو ان كل لغة عندها
# reserved keywords بشي سمية من دوك ال variables يعني انك متقدش تسمي ال
# لي فالبايثون reserved keywords كترجع لك ال help() سميتها python فال function كاينة
# str tuple list ... لي كتعطيها بحال ال arg كترجع ليك معلومات على ال help() هاد ال

help("keywords")
# Output: 
# False               class               from                or    
# None                continue            global              pass  
# True                def                 if                  raise 
# and                 del                 import              return
# as                  elif                in                  try   
# assert              else                is                  while 
# async               except              lambda              with  
# await               finally             nonlocal            yield 
# break               for                 not



# -----------------------------------------------
# -----------------------------------------------

# ايضا كما هو متعارف عليه فمعظم لغات البرمجة تقد تدكلاري باكثر من متغير فنفس السطر

a, b, c, d = 1, "A", 2, "B"

print(a, b, c, d) # 1 A 2 B
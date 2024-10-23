# ---------------------------------------------
# ---- Modules: Create your own ----
# ---------------------------------------------
# 
# ---------------------------------------------

# منهم import فيه المسارات لي تقد ت sys سميتو module اول حاجة خاص نعرفوها وهو انه كاين
# ومن ضمينهم ال المسار الحالي لي فيه دبا نتا
# sys.path بالضبط كاين فال

# import متقدش تدير منو sys.path يعني المسار لي مكاين فال

import sys

# ['d:\\programming\\VsCode-Workspace\\Courses\\Python\\week-11 [Modules, Date, Decorators]', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']



# // جديد ودير فيه الاكواد وصاف py ديالك ساهلة معليك غا دير ملف module اما بالنسبة لكيفاش دير
# // بسمية الملف import وجي هنا ودير


import myOwnModule as mOwn
# form myOwnModule import x
# form myOwnModule import sayHi

print(dir(mOwn))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sayHi', 'sum', 'x']

print(mOwn.x) # 100
mOwn.sayHi("Obito") # hello sir...
mOwn.sums(1, 2, 4, 1, 2, 90, 29, 12) # 141
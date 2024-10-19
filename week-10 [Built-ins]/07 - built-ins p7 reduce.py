# ---------------------------------------------
# ---- Built-in Functions P7 (reduce) ----
# ---------------------------------------------
#
# ---------------------------------------------
from functools import reduce

# higher order func حيت كتعتابر functools module فالاصدارات الجديدة حولوها لل reduce اول حاجة خاص تعرفها ان
# reduce باش تستعمل ال functools لل import يعني خاص دير


# iterator و function تاني حاجة خاص تعرفها وهي انها نفس الكونسيب كتقبل

# function وكدير نفس الخدمة وهي انها فلول كتاخد اول عنصرين وكطبق عليهم ال
# وهي غادة func من بعد كتاخذ النتيجة ديالهم و كتاخد العنصر التالت و كطبق تاني ال
# reduce js المهم نفس الفكرة ديال


def sumAll(n1, n2):
    return n1 + n2

myNums = [1, 2, 3, 9, 10, 29, 83]

sall = reduce(sumAll, myNums)

sall2 = reduce(lambda n1, n2 : n1 + n2, myNums)

print(sall, sall2) # 137 137

# ((((((1 + 2) + 3) + 9) + 10) + 29) + 83)
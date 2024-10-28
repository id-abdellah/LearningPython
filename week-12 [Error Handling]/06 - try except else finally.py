# -------------------------------------------------------
# ---- Exceptions Hanlding : Try Except Else Finally ----
# -------------------------------------------------------
#
# try => try and test for errors
# except => handle the error
# else => if there is no errors
# finally => run its code whatever happens
# -------------------------------------------------------

# // js كيما العادة مع ال
# // فقط كاينين شي تغييرات صغار

# // error وكتجربو واش فيه شي code كتخدم ال try ال
# // وكيعالجو try لي طرا فال error كياخذ ال except ال
# // error كتخدم فحالة مكانش تا else ال
# // error تخدمو فاش مكيكونش try تقد متحتاجهاش بزاف حيت الكود لي غتشغل هي تقد ال else ال
# // غتخدم في جميع الحالات finally اما ال

# // هوما لي ضروري تكتبهم بجوج اما لوخرين اختياريين try except ال


try:
    name = int(input("please enter ur age: "))
    print("[from try block] ur age is: ", name)
except:
    print("Wrong. only digits allowed")
else:
    print("[from else block]ur age is: ", name)
finally:
    print("Finally block will Run whatever happens")

# input = 20
# [from try block] ur age is:  20
# [from else block]ur age is:  20
# Finally block will Run whatever happens


# input = obito
# Wrong. only digits allowed
# Finally block will Run whatever happens




# // حاجة خرا

# // تقد تستعملها اكثر من مرة except ال
# // و تعامل معاه error لنوع محدد من ال except مما يعني انك تقد دير

try:
    print(10 / 0) # ZeroDivisionError
    # print(noVar) # NameError
    # print(int("Ohoo")) # ValueError
except ZeroDivisionError:
    print("cant divide on 0")
except NameError:
    print("identifier not found")
except ValueError:
    print("A value error occured")
except:
    print("something happened")
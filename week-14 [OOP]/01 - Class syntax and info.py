# ----------------------------------------------------------
# ---- Class Syntaxt and Infos ----
# ----------------------------------------------------------
#
# [1] class is blueprint of constructor of the object
# [2] Class instantiate means create instance of a class
# [3] Instance => Object created from Class and have their methods and attributes
# [4] Class defined with keyword "class"
# [5] Class name written "PascalCase" style
# [6] Class may contains methods and attributes and may not
# [7] When creating object from a class, python look for __init__ method
# [8] __init__ method called every time u create object from a class
# [9] __init__ method initialize data for the created object
#
# [10] Any method with two Underscore in both start and end. Called "Dunder" or "Magic" methods 
# [11] "Self" refers to the current instance created from the class and must be first param
# [12] "Self" can be named anyThing
# [13] In python u dont need "new" keyword to create instantiated object from a class
# ----------------------------------------------------------

# __init__ سميتها method معين. اللغة كتقلب نيشان على class من شي object كل مرة كتنشئ python فال
# كتخدم اوتوماتيكيا __init__ يعني كل مرة كتنشئو هاد ال

# لي غتنشئو object لل data او كتهيأ ال init كدير ال __init__ هاد ال

# magic methods اولا dunder method كتسما underscore فيها فاللول واللخر method قالك ال


# الحالي لي فيها نتا دبا object ولي كيعود على ال self وهو param خاص ضروري واحد ال __int__ method فال
# تقد تسميه اي حاجة self param هاد ال
# اللول param وخاص يكون هو ال
# js فال this بحال الا قلتي


# من شي كلاس object باش ندير new keyword مكنحتاجوش python فال

class MemberBlueprint:
    def __init__(self):
        print("new member has been added")


mOne = MemberBlueprint() # new member has been added
mTwo = MemberBlueprint() # new member has been added
mThree = MemberBlueprint() # new member has been added


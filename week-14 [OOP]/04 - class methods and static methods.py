# --------------------------------------------------------------
# ---- Class Methods and Static Methods ----
# --------------------------------------------------------------
#
# Class methods:
#   - Marked with "@classmethod" decorator to flag it as class method
#   - It takes "Cls" parameter not "self" to point to the class
#   - It doesnt require creation of a class instance
#   - Used when u wanna to do something with class itself
# Static methods:
#   - It takes no parameters
#   - Its bount tho the class not instance
#   - Used when doing something doesnt have access to object or class but related to class
# --------------------------------------------------------------


# // نفسو class خاصة او مرتبطة بال method يعني class methods
# // لي غتنشئو من الكلاس object لي كتكون خاصة بال instance methods ماشي بحال ال

# // خاصة بالكلاس method ديكوريتور باش تقوليه بلي هادي @classmethod خاص دير
# // باش تأشر على الكلاس ديالها self ماشي ال Cls param كتاخذ

# // من الكلاس باش تخدم بيهم instance مكيحتاجوش انك تقاد classmethods ال

class Member: 

    # class attribue
    members_count = 0

    def __init__(self, name, surename, age, isHired):
        self.name = name
        self.surename = surename
        self.age = age
        self.isHired = isHired
        Member.members_count += 1
    
    # instance method
    def getFullName(self):
        return f"{self.name} {self.surename}"
    
    @classmethod
    def getUsersCount(cls):
        print(f"we have {cls.members_count} users")

    @staticmethod
    def sayHi():
        print("Hi from static method")


memberOne = Member("Mohamed", "ID-ABDELLAH", 21, False)
memberTwo = Member("Mustafa", "ID-ABDELLAH", 21, False)
memberThree = Member("Mahmoud", "ID-ABDELLAH", 21, False)

Member.getUsersCount() # 1



# --------------- Static Methods ----------------

# // parameters ماشي بالضرورة تحط فيها static method ال
# // لي كتنشئها منو instance ماشي بال class هي عندها علاقة بال

Member.sayHi()







# little tip
# this two lines of code are same
# when u use this line of code below
print(memberOne.getFullName())
# python does this in the background
print(Member.getFullName(memberOne))

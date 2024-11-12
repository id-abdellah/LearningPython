# --------------------------------------------------------------
# ---- Class Attributes ----
# --------------------------------------------------------------
#
# Class attributes => Attributes Defined outside the constructor
# --------------------------------------------------------------



# constructor كتكون داخل ال instace الخاصة بال attributes ال
# constructor كتكون برا ال class اما الخاصة بال

# attribute كدير سمية الكلاس نقطة عاد سمية ال class atrributes باش توصل لل

class Member:

    # Class Attributes
    # To use it => ClassName.attr
    not_allowed_names = ["boobs", "shit", "fuck"]
    users_count = 0


    # Constructor
    def __init__(self, fName, mName, lName):
        self.firstName = fName
        self.middleName = mName
        self.lasteName = lName
        Member.users_count += 1
    

    # methods
    def getFullName(self):
        if self.firstName.lower() in Member.not_allowed_names:
            raise ValueError("Your first name is considered as not allowed names")
        else:
            return f"{self.firstName} {self.middleName[0].upper()}. {self.lasteName}"

    def sayHi(self):
        return f"Hello Mr. {self.getFullName()}"



mem = Member("shit", "mohamed", "ob")
mem2 = Member("john doe", "mohamed", "ob")
mem3 = Member("john doe", "mohamed", "ob")
mem4 = Member("john doe", "mohamed", "ob")
mem5 = Member("john doe", "mohamed", "ob")

# print(mem.getFullName()) # ValueError

print(Member.users_count) # 5
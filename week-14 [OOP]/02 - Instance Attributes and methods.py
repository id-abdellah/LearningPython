# ----------------------------------------------------
# ---- Instance Attributes and Methods ----
# ----------------------------------------------------
#
# ----------------------------------------------------


class Member:

    def __init__(self, fName, mName, lName):
        self.firstName = fName
        self.middleName = mName
        self.lasteName = lName
    
    def getFullName(self):
        return f"{self.firstName} {self.middleName[0].upper()}. {self.lasteName}"

    def sayHi(self):
        return f"Hello Mr. {self.getFullName()}"



memberOne = Member("Mohamed", "Brahim", "ID-ABDEELAH")
memberTwo = Member("Obito", "Konoha", "Uchiha")
memberThree = Member("Ahmed", "Junior", "Mahmoud")


# props
print(memberOne.firstName, memberOne.middleName, memberOne.lasteName) # Mohamed Brahim ID-ABDEELAH
print(memberTwo.firstName) # Obito
print(memberThree.firstName) # Ahmed


# methods
print(memberOne.getFullName()) # Mohamed B ID-ABDEELAH
print(memberTwo.getFullName()) # Obito K Uchiha
print(memberThree.getFullName()) # Ahmed J Mahmoud


print(memberOne.sayHi()) # Hello Mr. Mohamed B. ID-ABDEELAH
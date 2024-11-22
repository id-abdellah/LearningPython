#--------------------------------------------------------------------
# ---- Getters and Setters ----
# --------------------------------------------------------------------
# 
# --------------------------------------------------------------------


class Member:

    def __init__(self, name) -> None:
        self.__name = name # Private prop

    def getName(self) -> str:
        return self.__name
    
    def setName(self, newName) -> None:
        self.__name = newName


person = Member("Obito")

print(person.getName()) # Obito
person.setName("Uchiha")
print(person.getName()) # Uchiha
#--------------------------------------------------------------------
# ---- @Property Decorator ----
# --------------------------------------------------------------------
# 
# --------------------------------------------------------------------


# argument ك self كتقبل فقط ال method البلان وما فيه وهو انه الا عندك شي
# خرين argument يعني مفيهاش
# معين action ومكدير شي
# الخدمة ديالها انها كترجع ليك قيمة وصاف method يعني

# propery تقد تخليها تتعامل معاملة ال
# عادي property يعني فاش تنادي عليها مغديش دير القوسين. غتناديها وكأنها

class Member:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sayHi(self):
        return f"Hello Mr. {self.name}"
    
    @property
    def ageInDays(self):
        return self.age * 365


person = Member("Mohamed", 21)

print(person.sayHi())
# print(person.ageInDays()) # TypeError: 'int' object is not callable
print(person.ageInDays) # 7665


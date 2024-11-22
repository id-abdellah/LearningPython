#--------------------------------------------------------------------
# ---- Multiple Inheritance & Methods override ----
# --------------------------------------------------------------------
# 
# Method override => Derived class method overrides parent class method
#                       if they have the same name
# mro => Methods resolution order
# Multiple inheritance
# --------------------------------------------------------------------

class Food:

    def cook(self):
        print("This food is cooking")

    def eat(self):
        print("This food is been eating")


class Apple(Food):
    def cook(self):
        print("Apple is being cooking now")


parentFood = Food()

appleFood = Apple()

# كطبع حاجة parent class فال cook method هي مثلا كما كتشوف التحت Method override ال
# كطبع حاجة خرا apple classs وفال
# على لي فالكلاس الاب override فالكلاس الابن بنفس السمية كدير method وهي انك فاش كدير method overrid هادي هيا ال

parentFood.cook() # This food is cooking
appleFood.cook() # Apple is being cooking now


# --------------------------------
# mro => methods resolution order
# --------------------------------

class BaseOne:
    def __init__(self) -> None:
        print("from BaseOne")
    
    def func_one(self):
        print("one")

class BaseTwo:
    def __init__(self) -> None:
        print("from BaseTwo")
        
    def func_two(self):
        print("two")

class Derived(BaseOne, BaseTwo):
    pass


myVar = Derived() # from BaseOne
myVar.func_one() # one
myVar.func_two() # two

# baseone and basetwo ديال ال methods ف خاذ ال methods دبا كما كتشوف الفوق بالنسبة لل

# ديال اللول وماشي الثاني __init__ ولكن علاش طبع الرسالة لي فال
# BaseOne ديال الوراثة كيلعب دور. حيت اول واحد هو ال order حيت ال

# كتبين لي الترتيب ديال الوراثة وصاف mro يعني ال

print(Derived.mro()) 
# [<class '__main__.Derived'>, <class '__main__.BaseOne'>, <class '__main__.BaseTwo'>, <class 'object'>]



# --------------------------------
# Multiple inheritance
# --------------------------------

# ساهل multiple inheritance الكونسيب ديال ال

# methods فيه شي Base class وهو مثلا عندك
# Base class كيورث من ال DerivedOne class وعندك واحد
# DerivedOne class كيورث من ال DerivedTwo class وعندك

# حيت واحد كيعطي لواحد DerivedTwo class غتلقاهم عند ال Base class ديال ال methods ف المقصد هنا ان ال
#--------------------------------------------------------------------
# ---- Inheritance ----
# --------------------------------------------------------------------
# 
# --------------------------------------------------------------------

class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        print(f"{self.name} is created from 'Base' class")

    def eat(self):
        print("Eat method from 'Base' class")


class Apple(Food):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)
        print(f"{self.name} is created from 'Derived' class price is {self.price}")
    
    def saHi(self):
        print("hi from derived class")


# parent class على الخواص لي كانو فال override ف كدير derived class ديال ال init قالك اسيدي فاش كدير ال

# كلاس هي كالتالي parent الطريقة اللولة باش دير وراثة للخواص لي كانو فال
# Food.__init__(self, ...props) انك دير

# sef وكتمكنك انك بلا متكتب سمية الكلاس لي كتورث منو. و ايضا بلا متكتب super الطريقة الثانية انك كتخدم بال
# super().__init__(...props) وهي انك دير



# food = Food("Pizza", 180)
food_apple = Apple("Pizza", 200)
food_apple.eat()


food_apple.saHi()

# Food class يعني خاصية زيادة على داكشي لي خديناه من ال derived class خاصة بال saHi دبا هاد ال
# Food class ولكن مغتكونش متاحة من ال

# ولي غنشوفوه من بعد multiple inheritance هنا فين غيجي مصطلح اخر سميتو



# لي فالكلاس الاب class methods وال methods ال الكلاس الابن ديالك كيورث كاع ال inheritance. دبا كخلاصة. فاش كدير
# super().__init__(..props) فال كلاس الابن داكشي علاش خاص دير override كيدار ليها __init__ ولكن ال
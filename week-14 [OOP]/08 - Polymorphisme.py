#--------------------------------------------------------------------
# ---- Polymorphisme ----
# --------------------------------------------------------------------
# 
# a same method with same name, but do different job with each derived 
# class
# --------------------------------------------------------------------

# بنفس الاسم فكل بلاصة كدير خدمة مختالفة method ببساطة هي polymorphisme ال
# فكل بلاصة كدير خدمة مختالفة method هادشي علاش تسمات تعدد الاوجه, يعني نفس ال


# التحت خاص دير خدمة مختالفة فكل كلاس كياخذها من الاب doSomething دبا كما كتشوف التحت هاد ال

# عادي method كل كلاس غادي ياخذ ال raise noImplementedError فالحالة العادية لمدرناش ديك
# ولكن الخدمة ديالها غتكون نفسها نفس ديال الكلاس الاب

# باش دير خدمة مختالفة method لهاد ال implement بحالا كتقوليه خاص دير raise noImplementedError داكشي علاش ديك ال

# polymorphisme ولي كيدعم فكرة ال

class A:
    def doSomething(self):
        print("From class A")
        raise NotImplementedError("Derived classes must implement this method")

class B(A):
    pass

class C(A):
    def doSomething(self):
        print("From class C")


# myInstanceB = B()
# myInstanceB.doSomething() # NotImplementedError: Derived classes must implement this method


myInstanceC = C()
myInstanceC.doSomething()


# implement دير ليها method بحالا كتفورسي عليك لبغيتي تخدم بديك ال noImplementedError يعني كخلاصة ديك ال
# فالكلاس الابن باش دير خدمة مختالفة على الكلاس الاب

# polymorphisme ولي كيخدم فكرة ال
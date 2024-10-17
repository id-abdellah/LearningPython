# -----------------------------------------------------------
# ---- Function - scope ----
# -----------------------------------------------------------
# 
# -----------------------------------------------------------

x = 100 # Global scope

def funcOne():
    x = 1
    print(f"Print x var from function scope => {x}")


print(f"print x var from global scope => {x}") # print x var from global scope => 100
funcOne() # Print x var from function scope => 1


# js نفس الكونسيب من ال
# خاص بيها scope عندها function خاص بيه بحال ال scope عندو block of code وهو ان كل

# ديالها scope من ال x لفوق خدات قيمة ال function ف كما كتشوف ال





# وتبد قيمتو function scope من global var لشي override هنا فالبايثون تقد دير
# global x value لل override دارت funcTwo كما كتشوف التحت
# global keyword عن طريق ال


def funcTwo():
    global x
    x = 99
    print(f"print x var from functionTwo scope => {x}")


funcTwo() # 99
print(f"print x var from global scope again after overriding => {x}") # 99





# global وخا ميكونش المتغير من قبل هي كتنشئ داك المتغير وتخليه global keyword خاص تعرف ال

# accessebile globaly ودبا غيولي globale نشئات متغير وخلاتو funcThree كما كتشوف التحت, ال

def funcThree():
    global v
    v = 77

funcThree()
print(f"global var created by 'global' keyword from functionThree => {v}")
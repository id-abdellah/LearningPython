# -----------------------------------------------
# ---- Generators - Practical speed test ----
# -----------------------------------------------
# 
# -----------------------------------------------

from time import time


# باش تكمل الخدمة لي عليها function الفكرة وهي اننا غنحسبو شحال دالوقت غتدي شي

# epoch time منذ seconds ولي كيرد الوقت الحالي بال time خارجي سميتو module غنستعملو


def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"The function running time takes => {end - start}s")
    return wrapper
    

@speedTest
def bigLoop():
    x = 0
    while x < 10000:
        print(x)
        x+=1


bigLoop()
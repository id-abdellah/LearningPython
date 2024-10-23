# -----------------------------------------------
# ---- Generators - Function with parameters ----
# -----------------------------------------------
# 
# --------------------------------------------


# معندكش مشكل function لل decorator اول حاجة وهي انك تقد دير اكثر من

# func ماشي غا كطبع رسائل وانما كتحسن السلوك ديال decoration تاني حاجة نعاودو نقولوها وهي ان ال
# كيشوف واش الارقام فيها شي رقم سالب decorator كتجمع الارقام. تقد دير function مثلا عندك
# وبناء عليه دير اجراء معين


def aDecorator(func):
    def nestedFn(*nums):
        isThereNegativeValue = False
        for n in nums:
            if n < 0:
                isThereNegativeValue = True
                break
        if isThereNegativeValue:
            print("a decorator function founds a negative value between num")
        print(func(*nums))
    return nestedFn


def aDecoratorTwo(func):
    def nestedFn(*nums):
        print("Coming From second decorator")
        func(*nums)
    return nestedFn


@aDecoratorTwo
@aDecorator
def calculateNums(*ns):
    result = 0
    for n in ns:
        result += n
    return result


calculateNums(10, 10, 20, 30, 40, 100) 
# Coming From second decorator
# 210

calculateNums(10, -10, 20, 30, 40, 100) 
# Coming From second decorator
# a decorator function founds a negative value between num
# 190
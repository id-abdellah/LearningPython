# ---------------------------------------------
# ---- Generators ----
# ---------------------------------------------
# 
# ---------------------------------------------

# js generators تقريبا نفس المعلومات من ال
# تاني هه syntax لي مبدل تقريبا غار ال


# return عوض ال yield كتستعمل ال generator كما كنعرفو ال
# كترجع قيمة وحدة return كتنتج بيانات في حين ان ال yield ال


# yield هنايا كنعرفوها بال generator func ال js على عكس ال
# function* بحال هكا func keyword كنزيدو نجمة حدا js اما فال

# وكل مرة كنستعملوها كتكمل على فين وقفات اخر مرة next() method با ترد البيانات المنتجة كنستعلمو
# يعني مكتعاودش من اللول

# يعني فاش نساليوهم مغتبقا ترد لينا والو genfunc وكما كنعرفو ان البيانات لي كنرجعو مكبقاوش كاينين فال

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

myGen = myGenerator()

# print(myGenerator()) # <generator object myGenerator at 0x000002B847E94B40>

print(next(myGen)) # 1
print(next(myGen)) # 2
print(next(myGen)) # 3
print(next(myGen)) # 4
print(next(myGen)) # 5


def myGenerator2():
    yield "a"
    yield "b"
    yield "c"
    yield "d"
    yield "e"

myGen2 = myGenerator2()

# loop كتقبل حتا ال

for l in myGenerator2():
    print(l)

# a
# b
# c
# d
# e


# Generate infinite numbers

def generateInfinteNumbers():
    num = 0
    while True:
        yield num
        num += 1


xx = generateInfinteNumbers()

print(next(xx)) # 0
print(next(xx)) # 1
print(next(xx)) # 2
print(next(xx)) # 3
print(next(xx)) # 4
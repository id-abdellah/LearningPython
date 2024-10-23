x = 100
def sayHi(name):
    print(f"Hello sir {name} how are you")

def sums(*ns):
    res = 0
    for n in ns:
        res += n
    print(res)
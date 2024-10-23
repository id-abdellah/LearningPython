# Modules assignments

# assign 1

from random import randint, randrange, random

randomNum = randint(10, 50)
randomEven = randrange(2, 10, 2)
randomOdd = randrange(1, 9, 2)

print("random nubmer", randomNum)
print("random even number",randomEven)
print("random odd number",randomOdd)


print("+" * 40)

# Date and Time assignments

from datetime import datetime

# assign 1

firstDate = datetime(2021, 6, 25)
dateNow = datetime.now()

print(f"Number of days between 2021-6-25 and Now is => {(dateNow - firstDate).days}")

# assign 2

d = datetime(2021, 8, 10)

print(f"{d.year}-{d.month}-{d.day}")
print(f"{d.strftime("%b")} {d.day}, {d.year}")
print(f"{d.day} - {d.strftime("%b")} - {d.year}")
print(f"{d.day} / {d.strftime("%b")} / {d.strftime("%y")}")
print(f"{d.strftime("%a")}, {d.strftime("%d")} {d.strftime("%b")} / {d.strftime("%Y")}")

# 2021-8-10
# Aug 10, 2021
# 10 - Aug - 2021
# 10 / Aug / 21
# Tue, 10 Aug / 2021



print("*" * 40)

# Generators assignments

# assign 1

def reverse_str(string):
    n = len(string) - 1 
    while n >= 0:
        yield string[n]
        n -= 1

myGen = reverse_str("Obito")

for c in myGen:
    print(c)


print("*" * 40)

# Decorators assignments

def aDecorator(func):
    def wrapper():
       print("Sugar added from decorator")
       func()
       print("#" * 20)
    return wrapper
    
@aDecorator
def make_tea():
  print("Tea Created")
  
@aDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
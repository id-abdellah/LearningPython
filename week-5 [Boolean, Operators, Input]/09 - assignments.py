# ----------------------------------
# Assignments 01 - 05
# ----------------------------------

# Ex 1

print(bool(1))
print(bool("s"))
print(bool([1, 2]))
print(bool(True))

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))


print("*" * 10)


# Ex 2

html = 100
css = 90
js = 70

print(html > 50 and css > 50 and js > 50) # true


print("*" * 10)


# Ex 3

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


print("*" * 10)


# Ex 4

num1 = 10
num2 = 20

result = num1 + num2

print(result)

result **= 3

print(result)

result %= 26000

print(result)

result /= 5

print(result)

print(type(result))

result = str(result)

print(type(result))



print("#" * 50)


# ----------------------------------
# Assignments 06 - 08
# ----------------------------------


# Ex 1

name = input("your name please: ")

print(f"hello {name.strip().capitalize()} happy to see u again")


print("*" * 10)


# Ex 2

age = input("ur age: ")

int(age) > 16 and print("articles are suitable fo you")

int(age) <= 16 and print("articles are not")


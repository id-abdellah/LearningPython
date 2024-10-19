from functools import reduce

# assign 1

values = (0, 1, 2)

if any(values):

    my_var = 0
# my_var = 0 => because there is two truthy elements
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]  # my_var = 0


if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):  # true false  false

    print("Good")

else:

    print("Bad")

# final output => "Good"


# assign 4


def my_all(iterable):
    allTrue = True
    for item in iterable:
        if bool(item):
            allTrue = True
        else:
            return False
    return allTrue


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False


def my_any(iterable):
    allFalse = False
    for item in iterable:
        if bool(item):
            return True
        else:
            allFalse = False
    return allFalse


print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False


def my_min(iterable):
    m = iterable[0]
    for n in iterable:
        if n < m:
            m = n
    return m


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -1, 50)))  # -20


def my_max(iterable):
    m = iterable[0]
    for n in iterable:
        if n > m:
            m = n
    return m


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 2)))  # 100


print("#" * 50)

# assign 5

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = list(map(lambda s: s[1:-1], friends_map))

print(cleaned_list)  # ['Eman', 'Ahmed', 'Sameh', 'Osama']


print("#" * 50)

# assign 6

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def getName(n):
    return n.endswith("m")


filteredList = list(filter(getName, friends_filter))
filteredList = list(filter(lambda n: n.endswith("m"), friends_filter))  # the same

print(filteredList)  # ['Wessam', 'Essam']


print("#" * 50)

# assign 7

nums = [2, 4, 6, 2]

print(reduce((lambda n1, n2: n1 * n2), nums))  # 96

print("#" * 50)

# assign 8

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for en, sk in enumerate(skills, 50):
    if type(sk) == int:
        continue
    print(f"{en} - {sk}")

# 50 - HTML
# 51 - CSS
# 53 - PHP
# 54 - Python
# 56 - JavaScript

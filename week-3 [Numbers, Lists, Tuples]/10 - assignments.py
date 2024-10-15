# assign 1

a = "Osama",

print(a[0]) # "osama"
print(type(a)) # tuple


# assign 2

friends_1 = ("Osama", "Ahmed", "Sayed")

b, c, d = friends_1

b = "Elzero"

friends_1 = (b, c, d)

print(friends_1) # ('Elzero', 'Ahmed', 'Sayed')
print(type(friends_1)) # tuple
print("{:d} elements".format(len(friends_1))) # 3 elements



# assign 3

nums = (1, 2, 3)
letters = ("A", "B", "C")

newTub = nums + letters

print(f"nums_and_letters_one = {newTub}") # nums_and_letters_one = (1, 2, 3, 'A', 'B', 'C')
print(f"{len(newTub)} elements")



# assign 4

my_tuple = (1, 2, 3, 4)

aa, bb, _, cc = my_tuple
print(aa, bb, cc) # 1 2 4
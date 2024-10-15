# assignment 1

my_list1 = [1, 2, 3, 3, 4, 5, 1, 1, 1, 2, 3, 3, 3]

uniqueList = list(set(my_list1))

print(uniqueList) # [1, 2, 3, 4, 5]
print(type(uniqueList)) # list
print(uniqueList[0:-1]) # [1, 2, 3, 4]



# assignment 2

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters)) # {1, 2, 3, 'A', 'B', 'C'}
print(nums | letters) # {1, 2, 3, 'A', 'B', 'C'}
nums.update(letters)
print(nums) # {1, 2, 3, 'A', 'B', 'C'}



print("#" * 50)



# assignment 3


my_set = {1, 2, 3}
letters2 = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set) # set()
my_set.add("A")
my_set.add("B")
print(my_set) # {'B', 'A'}
my_set.discard("C")




# assignment 4

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two)) # True



print("#" * 50)



# assignment 5

mySkills = {
    "html/Css": 100,
    "js": 80,
    "reactJS": 60
}

print("Html/Css progress is {:d}%".format(mySkills["html/Css"])) # Html/Css progress is 100%
print("JS progress is {:d}%".format(mySkills["js"])) # JS progress is 80%
print(f"JS progress is {mySkills["reactJS"]}%") # JS progress is 80%

mySkills["Sass"] = 200

print(f"Sass progress is {mySkills["Sass"]}")
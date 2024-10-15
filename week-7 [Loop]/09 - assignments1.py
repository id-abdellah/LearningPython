# when u returning back to revising this assignments code. 
# make sure to uncomment only one assignment and comment the others



# assign 1

num = int(input("please inter a number > 5: "))

if (num > 5):
    x = 0;
    while num > 0:
        num -= 1
        if num == 5 or num == 6: continue
        print(num)
        x += 1
    else:
        print(f"{x} number are printed")
else:
    print(f"Number {num} is not Larger than 5")





# assign 2

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif", "Simo", "sara", "khaled"]

i = 0
ignored = 0
while i < len(friends):
    if (friends[i] == friends[i].lower()):
        ignored += 1
    else: 
        print(friends[i])
    i += 1
else:
    print(f"completed. {ignored} names are ignored")





# assign 3

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))




# assign 4


my_friends = []
maximum = 5


while maximum > 0:
    fName = input("Enter ur Name: ").strip()

    if fName.isupper():
        print("Invalid name")
        continue
    elif fName.islower():
        my_friends.append(fName.capitalize())
        maximum -= 1
        print("--Name is added after capitalize him")
    elif fName == fName.capitalize():
        my_friends.append(fName)
        maximum -= 1
        print("--Name added directly")
    
    print(f"u have {maximum} places left")
else:
    print(my_friends)
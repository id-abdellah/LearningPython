# assignment 1

myFriends = ["Atiqe", "Laayal", "Ziko", "Youness", "Ahmed"]

print(myFriends[0]) # atiqe
print(myFriends.pop(0)) # atiqe
print(myFriends[-1]) # ahmed
print(myFriends.pop(-1)) # ahmed




# assignment 3

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(", ".join(friends[2:5])) # Sayed, Ali, Mahmoud
print(", ".join(friends[-2:])) # Ali, Mahmoud



# assignment 4

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[-2:] = ["Elzero", "Elzero"]

print(friends) # ['Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero']



# assignment 5

friends_2 = ["Osama", "Ahmed", "Sayed"]

friends_2.insert(0, "NewOne")
friends_2.append("NewOne")

print(friends_2) # ['NewOne', 'Osama', 'Ahmed', 'Sayed', 'NewOne']



# assignment 6

friends_3 = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends_3.pop(0)
friends_3.pop(0)
print(friends_3) # ['Ahmed', 'Sayed', 'Salem']

friends_3.pop(-1)
print(friends_3) # ['Ahmed', 'Sayed']




# assignment 7

friends_4 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends_4.extend(employees)
friends_4.extend(school)

print(friends_4) # ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']




# assignment 8

friends_5 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends_5.sort()
print(friends_5) # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']

friends_6 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends_6.sort(reverse=True)
print(friends_6) # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']



# assignment 9

print(len(friends_6)) # 6




# assignment 10

technologies = ["Html", "CSS", "JS", "Python", ["Django", "React", "Flask", "Web"]]

print(technologies[-1][0]) # Django
print(technologies[-1][-1]) # Web
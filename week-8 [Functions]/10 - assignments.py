# assign 1

def calculate(n1, n2, op = "add"):
    if op.lower() == "a" or op.lower() == "add":
        return n1 + n2
    elif op.lower() == "s" or op.lower() == "substract":
        return n1 - n2
    elif op.lower() == "m" or op.lower() == "multiply":
        return n1 * n2

print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subsTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200




print("*" * 50)

# assign 2

def addition(*nums):
    result = 0
    for n in nums:
        if n == 10: continue
        if n == 5:
            result -= n
        result += n
    return result

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160




print("*" * 50)

# assign 3

def showSkills(name, *skills):
    print(f"Hello {name} ur skills are: " if skills else f"Hello {name} u have no skills")
    for s in skills:
        print(f"- {s}")

showSkills("Obito", "htmls", "css", "js", "sass")
showSkills("Madara")






print("*" * 50)

# assign 4

def get_score(**scors):
    for key, value in scors.items():
        print(f"{key} => {value}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)







print("*" * 50)

# assign 5

def get_people_scores(name = "", **scores):
    if name:
        print(f"Hello {name} this is your scores: ")

    if not scores:
        print("no scores :(")
    for key, value in scores.items():
        print(f"{key} => {value}")
    
get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")






print("*" * 50)

# assign 6

scoreList = {
    "Html": 90,
    "css": 80,
    "js": 100,
    "sass": 200
}

def get_the_scores(name = "", **scores):
    if name and scores:
        print(f"hello {name} this is your scores: ")
        for k, v in scores.items():
            print(f"{k} => {v}")
    elif name and not scores:
        print(f"hello {name} there is no scores")
    else:
        for k, v in scores.items():
            print(f"{k} => {v}")

get_the_scores("Osama", **scoreList)
get_the_scores("Osama")
get_the_scores(**scoreList)


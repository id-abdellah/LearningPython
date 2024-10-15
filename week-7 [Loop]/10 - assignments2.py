# assign 1

my_nums = [15, 81, 5, 17, 20, 21, 13]
x = []
for num in my_nums:
    if num % 5 == 0:
        x.append(num)
else:
    x.sort(reverse=True)
    for n in x:
        print(f"{x.index(n) + 1} => {n}")
    print("All numbers printed")




# assign 2

for n in range(1, 21):
    if n == 6 or n == 8 or n == 12:
        continue
    print(str(n).zfill(2))



# ranksConverted = {
#     "A": 100,
#     "B": 80,
#     "C": 40
# 

# assign 3

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

ranksConverted = {
    "A": 100,
    "B": 80,
    "C": 40
}

for m in my_ranks:
    print(f"My Rank in {m} is {my_ranks[m]} and this equal {ranksConverted.get(my_ranks[m])}")
else:
    result = 0
    for m in my_ranks:
        result += ranksConverted.get(my_ranks[m])
    print("Total points is: " + str(result))





# assign 4


students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

ranksConverted2 = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

for student in students:
    print("-" * 40)
    print((" student name => " + student + " ").center(40, "-"))
    print("-" * 40)

    hisRanks = students.get(student)
    
    for matier in hisRanks:
        print(f"- {matier} => {ranksConverted2[hisRanks.get(matier)]} Points")
    else:
        sum_ = 0
        for m in hisRanks:
            sum_ += ranksConverted2.get(hisRanks[m])
        print(f"{student}'s Total Points is {sum_}")
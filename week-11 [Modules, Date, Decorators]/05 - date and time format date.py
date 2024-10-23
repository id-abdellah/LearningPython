# ---------------------------------------------
# ---- Date and Time: Format Date ----
# ---------------------------------------------
# 
# datetime.datetime.strftime(str)
#
# the reference of all strftime directives:
#   https://strftime.org
#   or just google it :D
# ---------------------------------------------

# كل واحد وشنو كيدير directives باستعمال date لل format وهي انها كدير strftime ال فكرة ديال ال

# كيرجع ليك سمية النهار بشكل مختصر %a مثلا عندك
# كيرجع ليك سمية النهار كاملة %A في حين ان ال
# تختار منهم لي تناسب الفكرة ديالك directives وهي غادة. عندك مجموعة ديال ال


from datetime import datetime


myBirthDay = datetime(2002, 12, 16, 9, 30, 32, 9342)

print(myBirthDay) # 2024-10-21 11:56:49.792797


# name of the day
print(myBirthDay.strftime("%a")) # Wed
print(myBirthDay.strftime("%A")) # Wednesday

# week day (0 => sunday, 6 => saturday)
print(myBirthDay.strftime("%w")) # 3

# day of the month
print(myBirthDay.strftime("%d")) # 16

# Month name
print(myBirthDay.strftime("%b")) # Dec
print(myBirthDay.strftime("%B")) # December

# Month number
print(myBirthDay.strftime("%m")) # December

# year
print(myBirthDay.strftime("%y")) # 02
print(myBirthDay.strftime("%Y")) # 2002

# hour => (H 24-hour clock) (I 12-hour clock)
print(myBirthDay.strftime("%H")) # 09
print(myBirthDay.strftime("%I")) # 09

# minute, second
print(myBirthDay.strftime("%M")) # 30
print(myBirthDay.strftime("%S")) # 32

# pm or am
print(myBirthDay.strftime("%p")) # AM

# ... etc


# you can combin theme in one

print(myBirthDay.strftime("[%y - %b - %a]")) # [02 - Dec - Mon]
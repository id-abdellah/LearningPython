# ---------------------------------------------
# ---- Date and Time ----
# ---------------------------------------------
# 
# datetime.now() => return the current date and time
# datetime.now().date() => return the current date
# datetime.now().time() => return the current time
# datetime.now().year
# datetime.now().month
# datetime.now().day
# datetime.now().hour
# datetime.now().minute
# datetime.now().second
# datetime.now().microsecond
#
# datetime(year, month, day, hour, minutes?, second?, micros?) => return specific date and time
# ---------------------------------------------

import datetime


# print current date and time

print(datetime.datetime.now()) # 2024-10-21 11:11:18.359461

# print current date

print(datetime.datetime.now().date()) # 2024-10-21

# print current time

print(datetime.datetime.now().time()) # 11:12:08.498156


# print date and time in parts

print(datetime.datetime.now().year) # 2024
print(datetime.datetime.now().month) # 10
print(datetime.datetime.now().day) # 21
print(datetime.datetime.now().hour) # 11
print(datetime.datetime.now().minute) # 13
print(datetime.datetime.now().second) # 38
print(datetime.datetime.now().microsecond) # 124179



print("*" * 20)

# print specific date
# datetime.datetime(year, month, day, hour?, minute?, second?, microsecond?)

print(datetime.datetime(2002, 12, 16)) # 2002-12-16 00:00:00


print("*" * 20)

# difference between two dates


myBirthDay = datetime.datetime(2002, 12, 16)
dateNow = datetime.datetime.now()

print("i lived", dateNow - myBirthDay) # 7980 days, 11:30:10.932822
print("i lived", (dateNow - myBirthDay).days) # 7980 days
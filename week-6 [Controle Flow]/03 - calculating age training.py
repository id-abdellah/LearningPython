# ----------------------------------------------------
# ---- Practice: Calculating age advanced version ----
# ----------------------------------------------------
#
# ----------------------------------------------------

print("++++ u can write the first letter or full name of the time unit ++++")

age = int(input("pleas enter your age: ").strip())

unit = input("time unit? days, weeks, months: ").strip().lower()

ageInMonths = age * 12
ageInWeeks = ageInMonths * 4
ageInDays = age * 365

if unit == "days" or unit == "d": print(f"ur age in days is: {ageInDays:,d}")
elif unit == "weeks" or unit == "w": print(f"ur age in weeks is: {ageInWeeks:,d}")
elif unit == "months" or unit == "m": print(f"ur age in months is: {ageInMonths:,d}")
else : print("sorry something went wrong; either u entered a wrong arg or u kept the input empty")
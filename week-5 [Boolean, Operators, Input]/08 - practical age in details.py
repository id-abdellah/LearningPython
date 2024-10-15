# --------------------------------------
# ---- Practical age in details ----
# --------------------------------------
#
# --------------------------------------

urAge = int(input("your age please: "))


months = urAge * 12
weeks = months * 4
days = urAge * 365
hours = days * 24
minuts = hours * 60
seconds = minuts * 60

print(f"You lived \
{urAge} Years \n\
{months} months \n\
{weeks} weeks \n\
{days:,d} days \n\
{hours:,d} hours \n\
{minuts:,d} minuts \n\
{seconds:,d} seconds \n\
")
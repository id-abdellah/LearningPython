# -------------------------------------------
# ---- Ternary Conditional Operator ----
# -------------------------------------------
#   
# Syntax:
#
#   when it's True | if condition | when it's False
# -------------------------------------------


movieRate = 18
age = 12

# normal if condition

if age < movieRate : print("The movie is not suitable for u")
else : print("U'r good :)")


# Ternary condition operator

print("u are not suitable to watch this" if age < movieRate else "U'r all good")

print("i am moroccan boy" if False else "iam not moroccan boy")



# in JS
# a > b ? "when true" : "when false"

# in PY
# "when true" if a > b else "when false"
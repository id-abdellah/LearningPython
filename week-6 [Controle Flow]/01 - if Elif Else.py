# -------------------------------------------
# ---- if Elif Else ----
# -------------------------------------------
#
# Syntax:
#   if Condition :
#       Code Block Here
#   elif condition :
#       code block
#   else :
#       code block
#
# or
#   if Condition : code  => if u have on line code
#   elif condition: code
#   else : code
# -------------------------------------------

# لي مبدل شوية syntax فكرتها باينة غار ال if condition ال


name = "Mohamed ID-ABDELLAH"
country = "morocco"
haveDiscount = True


if country == "morocco" and haveDiscount: 
    print(f"hello {name}")
    print(f"you are from morocco so we'll give you a \"80%\" discount")
elif country == "ksa":
    print(f"hello {name}")
    print(f"you are from ksa so we'll give you a \"50%\" discount")
elif country == "eg":
    print(f"hello {name}")
    print(f"you are from egypte so we'll give you a \"10%\" discount")
else:
    print(f"hello {name}")
    print("sorry we decide to not give you a discount")


    
# -----------------------------------------------
# ---- Function - Parameters & Arguments ----
# -----------------------------------------------
# 
# -----------------------------------------------


def fullName(first, middle, second):
    print(f"{first.capitalize()} {middle.upper():.1s}. {second.capitalize()}")

fullName("Mohamed", "brahim", "id-abdellah")



def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers are allowed")
    else:
        print(n1 + n2)


addition(100, 200) # 300
addition("100", 10) # Only ...
addition(1, 2) # 3
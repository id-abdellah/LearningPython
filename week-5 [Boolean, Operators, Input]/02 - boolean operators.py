# --------------------------------------
# ---- Boolean Operators ----
# --------------------------------------
#
# and   => "condition1" and "condition2"
# or    => "condition1" or "condition2"
# not   => not "condition"
# --------------------------------------

age = 20
country = "MR"
rank = 10



# && لي كتكون js على عكس ال keyword كتكتب هكا ك and ال
# False ولكان واحد متحققش غترجع True وبطبيعة الحال هي كتطلب ان غاع الشروط يتحققو باش ترجع

print(age >= 20 and country == "MR" and rank > 0) # True
print(age >= 20 and country == "EG" and rank > 0) # False





# False اما لمتحققش ولا شرط كترجع True تاهي باينة. الا تحقق شرط واحد كترجع or ال

print(age > 40 or country == "KSA" or rank > 10) # False
print(age > 40 or country == "MR" or rank > 10) # True




# تاهي باينة. حيت كتعكس اللوجيك not ال

print(age > 100) # False
print(not age > 100) # True
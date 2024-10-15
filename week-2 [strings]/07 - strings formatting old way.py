# ------------------------------------
# --- string Formatting old way ---
# ------------------------------------
#
#
# uses placeholders => "bla bla bla %s bla bla bla %d" % (stringVlue, numValue)
#
# %s => strings
# %d => numbers
# %f => floating point numbers
# ------------------------------------


# لا integers يعني ال strings فالبايثون كتربط فقط ال concatenation دبا حنا عارفين ان ال
# js فال template literals ولي تقريبا كتلعب الدور ديال ال string formatting لهذا كاينة حاجة سميتها ال

# placeholders دبا غنشوفو الطريق القديمة ولي كتستعمل ال
# c هي الي كتستعملها لغة ال placeholder على فكرة هاد الطريقة ديال ال


# ---------------------------------------------

# واحد كديرو نيشان placeholder فحالة عندك
# وتحط القيم بالترتيب () حيت فاش كيكون عندك بزاف كتجمعهم فال

a = "uchiha"

print("Obito %s" % "uchiha") # Obito uchiha
print("Obito %s" % a) # Obito uchiha



# ----------------------------------------------

firstName = "Mohamed"
lastName = "ID-ABDELLAH"
age = 21
height = 1.719876

fString = "my firstname is %s and my lastname is %s i am %d yrs old and my height is %f" % (firstName, lastName, age, height) 

print(fString)
# my firstname is Mohamed and my lastname is ID-ABDELLAH i am 21 yrs old and my height is 1.719876


# ----------------------------------------------
# controling floating point number

# تقد تحكم فعدد الارقام بعد الفاصلة

print("my height is: %f" % height) # my height is: 1.719876
print("my height is: %.1f" % height) # my height is: 1.7
print("my height is: %.2f" % height) # my height is: 1.71
print("my height is: %.3f" % height) # my height is: 1.720



# ----------------------------------------------
# truncate strings

# placeholder لي باغي تاخذ من ال chars تقد تحكم فعدد ال

print("hello %.2s" % "abcdefghlmn") # ab
print("hello %.1s" % "abcdefghlmn") # a
print("hello %.6s" % "abcdefghlmn") # abcdef
# -------------------------------------------------------
# ---- Errors and Exceptions raising ----
# -------------------------------------------------------
#
# Exceptions is a runtime error reporting mechanism
# Exceptions give you a message to understand the problem
# Traceback gives you the line to look for the code in this line
# Exceptions type are (ValueError, SyntaxError, KeyError, etc...)
# 
# "raise" keyword used to raise you own exception
# -------------------------------------------------------


# Error ملي كيكون شي terminal لي كنا كنشوفو فال traceback دبا ال
# وقع وكتمشي ليه نيشان line ف انا error الخدمة ديالو انه كيقول ليك هاد ال traceback هاد ال


# // انا نوع و رسالة فيها شرح المشكل Error كيعطيوك معلومات على ال exceptions اما ال

# // خاص بيك Exception تقد دير raise keyword باستعمال ال


# مع النوع ديالو مع رسالة Exception عادي مع رسالة. اولا تلوح Exception تقد تلوح
# raise Exception("a message")
# raise ValueError("a message")


y = 20

if type(y) != int:
    print("booyah. it is string")
    print(y)
else:
    raise ValueError("must be a string :(")


# Traceback (most recent call last):
#   File "d:\programming\VsCode-Workspace\Courses\Python\week-12 [Error Handling]\05 - Errors and Exceptions raising.py", line 34, in <module>
#     raise ValueError("must be a string :(")
# ValueError: must be a string :(
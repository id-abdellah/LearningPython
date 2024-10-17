# -----------------------------------------------------------
# ---- Function - Lambda (anonymous function) ----
# -----------------------------------------------------------
#
# Syntax:
#
#   funName = lambda agr1, agr2 : oneExpressionCode
#
# [1] it has no name
# [2] u can call it inline without defining it
# [3] u can use it as returned data from another function
# [4] Lambda used for simple functions and "def" handle large tasks
# [5] Lambda is one single expression not block of code
# [6] Lambda type is Function 
# -----------------------------------------------------------


# صاف syntax فالجافاسكريبت لي مبدل هو ال anonymous functions نفس الكونسيب ديال

# يعني سطر واحد ديال الكود one expression كتقبل فقط
# block of code مكتعتابرش


def sayHi(name, age):
    print(f"hello {name}")
    print(f"ur age is: {age}")

sayHi("obito", 200)



sayHiAnon = lambda name, age : print(f"hello {name} ur age is: {age}")

sayHiAnon("Naruto", 20) # hello Naruto ur age is: 20

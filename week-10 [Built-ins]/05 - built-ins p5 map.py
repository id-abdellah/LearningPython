# ---------------------------------------------
# ---- Built-in Functions P5 (map) ----
# ---------------------------------------------
#
# [1] Map takes a Function + iterator
# [2] Called map because it "Map" the function on every iterator element
# [3] The function can be pre-defined function or lambda function
# ---------------------------------------------


# لي مبدل syntax غار ال js تقريبا نفس الكونسيب ديال

# Using pre-defined function

def formatNames(name):
    return f"-{name.capitalize().strip()}-"


myNames = ["obito ", "  madara", "   naruto   ", "kakashi"]

formatedNames = map(formatNames, myNames)

print(formatedNames) # <map object at 0x000001984B495C30>
print(list(formatedNames)) # ['-Obito-', '-madara-', '-naruto-', '-Kakashi-']




formatedNames2 = map((lambda name: f"{name.strip().capitalize()}-fromLambda"), myNames)

print(list(formatedNames2))
#['Obito-fromLambda', 'Madara-fromLambda', 'Naruto-fromLambda', 'Kakashi-fromLambda']
# ---------------------------------------------
# ---- Built-in Functions P6 (filter) ----
# ---------------------------------------------
#
# [1] Map takes a Function + iterator
# [2] Called map because it "Map" the function on every iterator element
# [3] The function can be pre-defined function or lambda function
# [4] The function needs to return Boolean Value
# ---------------------------------------------

# js تاهي نفس الفكرة لي كنا خدامين فيها فال
# ولي كيتحقق فيه الشرط كتردو element فيها شرط معين كتقارنو مع غاع ال function يعني كتكون عندك

# ماشي شي قيمة bool ترجع filter function و خاص ال


def checkNums(n):
    return n % 2 == 0


myNumbers = [1, 2, 9, 8, 10, 22, 83, 21, 12]

checkedNums = list(filter(checkNums, myNumbers))

print(checkedNums) # [2, 8, 10, 22, 12]



# --------


myStrs = ["ahmed", "mohamed", "arnab", "asaad", "obito"]

x = filter((lambda str : str[0] == "a"), myStrs)

print(list(x)) # ['ahmed', 'arnab', 'asaad']

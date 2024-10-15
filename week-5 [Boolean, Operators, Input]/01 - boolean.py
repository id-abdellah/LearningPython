# --------------------------------------
# ---- Boolean ----
# --------------------------------------
# bool() => built-in function
# --------------------------------------


# بناء على القيمة لي غتعطيها true or false كترد لك bool() هاد ال


# Truthy Values

print(bool("s")) # True
print(bool(100)) # True
print(bool(10.2)) # True
print(bool(True)) # True
print(bool([1, 2, 3])) # True
print(bool((1, 2, 3))) # True
print(bool({1, 2, 3})) # True
print(bool({"a": 20})) # True


# Falsy Values

print(bool("")) # False
print(bool(0)) # False
print(bool(False)) # False
print(bool(())) # False
print(bool({})) # False
print(bool([])) # False
print(bool(None)) # False



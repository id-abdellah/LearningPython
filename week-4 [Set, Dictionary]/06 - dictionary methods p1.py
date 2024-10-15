# --------------------------------------
# ---- Dictionary Methods p1----
# --------------------------------------
#
# clear()
# update(dic) => obj.update({"key": value})
# copy() => shallow copy
# keys()
# values()
# --------------------------------------


# --------------------------------------
# clear()

user1 = {
    "name": "Mohamed"
}

user1.clear()

print(user1) # {}

# --------------------------------------



# --------------------------------------
# update(dict)

# جداد keys values هادي كضيف بيها
# فيه القيم لي بغيتي ضيف dictionary كتقبل update ولكن هاد ال
# js كاينة طريقة خرا وهي لي كنا كنستعملو فال

member = {
    "name": "Mohamed id-abdellah"
}

member["age"] = 21
member.update({"country": "Morocco", "isHired": False})

print(member) # {'name': 'Mohamed id-abdellah', 'age': 21, 'country': 'Morocco', 'isHired': False}

# --------------------------------------




# --------------------------------------
# copy()

# وفاش كتعدل على الاصلي. النسخة مكيطرا فيها والو dict من ال shallow copy نفس الفكرة وهي انها كتاخذ

a = {
    "name": "Obito"
}

b = a.copy()

a["skill"] = "frontend dev"

print(a) # {'name': 'Obito', 'skill': 'frontend dev'}
print(b) # {'name': 'Obito'}

# --------------------------------------



# --------------------------------------
# keys() & values()

print(a.keys()) # {'name': 'Obito'}
print(a.values()) # dict_values(['Obito', 'frontend dev'])
# --------------------------------------
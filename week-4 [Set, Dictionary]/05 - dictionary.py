# --------------------------------------
# ---- Dictionary ----
# --------------------------------------
#
# [1] Dict items enclosed in curly braces {}
# [2] Dict items are "key : value"
# [3] Dict keys must be immutable => (Number, String, Tuple) List not allowed
# [4] Dict value can have any data types
# [5] Dict key must be Unique (if are there two similar keys, the last one will be choosed)
# [6] Dict is not ordered. Elements are accessed by key
# --------------------------------------


user = {
    "name": "Mohamed",
    "age": 20,
    "country": "Morocco",
    (1, 2, 3): "test 1",
    100: "test 2",
    True: "test 3",
    "skills": ["html", "css", "js"],
    "rating": 9.8
}


print(user)


# get method اولا تستعمل bracket notation باش تجيب شي قيمة خاص تستعمل ال

print(user["country"]) # morocco
print(user.get("country")) # morocco


# values اولا غاع ال keys كيما العادة باش تجيب غاع ال

print(user.keys()) # dict_keys(['name', 'age', 'country', (1, 2, 3), 100, True, 'skills', 'rating'])
print(user.values()) # dict_values(['Mohamed', 20, 'Morocco', 'test 1', 'test 2', 'test 3', ['html', 'css', 'js'], 9.8])



# two-dimensional Dictionary (nested Dictionary)

progLanguages = {
    "one": {
        "name": "JavaScript",
        "da": ["frontend", "backend", "desktopApps", "mobileApps"]
    },
    "two": {
        "name": "Html",
        "da": "frontend"
    },
    "three": {
        "name": "Css",
        "da": "Stylig"
    }
}

# brackets notations القضية باينة كدير قدما بغيتي من ال nested object باش تأكسس لل

print(progLanguages["one"]["name"]) # JavaScript
print(progLanguages["one"]["da"]) # ['frontend', 'backend', 'desktopApps', 'mobileApps']


# Dictionary length


print(len(progLanguages)) # 3 keys
print(len(progLanguages["one"])) # 2 keys
# ----------------------------------------------------
# ---- For Loop - Training ----
# ----------------------------------------------------
# 
# range(start, end)
# ----------------------------------------------------

# range(start, end)
# غير مضمن end كتنشئ ليك مجموع ارقام فنطاق معين مع العلم ان ال range ال

myRange = range(1, 10)

for num in myRange:
    print(num)


# dictionary

mySkills = {
    "html": 80,
    "css": 70,
    "js": 60,
    "sass": 100,
    "python": 30
}

for skill in mySkills:
    print(f"my progress in {skill} is => {mySkills.get(skill)}%")
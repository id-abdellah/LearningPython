# ------------------------------------------------------------
# ---- Function - Packing and Unpacking keyword arguments ----
# ------------------------------------------------------------
# 
# **KWArgs
# ------------------------------------------------------------


# tuple هو func agrs ملي كديرو فال unpacking دبا حنا عارفين ان نوع البيانات لي كيعطيك ال

# unpacking باش يدير ليه args فال dictionary كيولي يطلب منك تعطيه astrics اما هنا فاش كدير جوج


def showSkills(**skills):
    print(type(skills)) # dict
    for key, value in skills.items():
        print(f"{key} => {value}")

showSkills(html = 100, css = 50, js = 80)
# output
# <class 'dict'>
# html => 100
# css => 50
# js => 80


# unpacked عطيه ليه dict فاش تعطيه

mySkils = {
    "sass": 200,
    "less": 0
}

showSkills(**mySkils)
# sass => 200
# less => 0
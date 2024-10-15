# ----------------------------------------------------
# ---- For Loop - nested loop ----
# ----------------------------------------------------
# 
# ----------------------------------------------------

peoples = ["ahmed", "mohamed", "mahmoud", "sara"]

skills = ["html", "css", "js", "sass"]

for persone in peoples:

    print(f"{persone} - skills is: ")
    for skill in skills:
        print(f"\t- {skill}")

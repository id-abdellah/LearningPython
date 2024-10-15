# ----------------------------------------------------
# ---- Loop advanced dict ----
# ----------------------------------------------------
# 
# ----------------------------------------------------

# فنفس الوقت values وال keys وحدهم وانما على ال keys ماشي على ال loop الفكرة هي اننا غادي نديرو
# keys values من ال tuples فيها list ولي كترد لينا dict.items() ولكن باش نديرو هادشي خاصنا نخدمو بال


mySkills = {
    "html": "80%",
    "css": "70%",
    "js": "50%",
    "sass": "100%"
}

for skill_key, skillValue in mySkills.items():
    print(f"{skill_key} => {skillValue}")

# html => 80%
# css => 70%
# js => 50%
# sass => 100%


print("#" * 50)


myUltimatSkills = {
    "html": {
        "main": "20%",
        "Pugjs": "80%"
    },
    "css": {
        "main": "100%",
        "sass": "200%"
    }
}


for skill_key, skill_value in myUltimatSkills.items():
    print(f"{skill_key} the progress is: ")
    for key, value in skill_value.items():
        print(f"\t {key} => {value}")
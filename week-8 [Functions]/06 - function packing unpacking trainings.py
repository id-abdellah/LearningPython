# -----------------------------------------------------------
# ---- Function - Packing and Unpacking args - TRAININGS ----
# -----------------------------------------------------------
# 
# -----------------------------------------------------------


# سواء نجمة وحدة او جوج تقد تكتبو و تقد متكتبو عادي packing اول معلومة وهي انك فاش كدير
# error ومكيدردش لك

# حدا بعضياتهم packing unpacking وتقد دير ال الجوج انواع ديال ال



def showMySkills(name, *skills, **skillsProg):
    print(f"Hello {name} \nur unprogressed skills are")
    for skill in skills:
        print(f"- {skill}")
    
    print(f"ur progressed skills are")
    for key, value in skillsProg.items():
        print(f"- {key} => {value}")



showMySkills("mohamed")
# Hello mohamed 
# ur unprogressed skills are
# ur progressed skills are



showMySkills("Obito", "php", "go", "sass", python = 50, js = 40, css = 80)

# Hello Obito
# ur unprogressed skills are
# - php 
# - go  
# - sass
# ur progressed skills are
# - python => 50
# - js => 40
# - css => 80





tup = ("php", "go", "sass")
dic = {"python" : 50, "js" : 40, "css" : 80}


showMySkills("Obito", *tup, **dic)
# Hello Obito
# ur unprogressed skills are
# - php
# - go
# - sass
# ur progressed skills are
# - python => 50
# - js => 40
# - css => 80

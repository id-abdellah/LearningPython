# --------------------------------------------------------------------
# ---- Magic Methods ----
# --------------------------------------------------------------------
# 
# Magic methods => Dender methods
# 
# EveryThing in Python is Object
#
# __init__          Called automatically when instantiating class
# instance.__class  the class to which a class instance belongs
# __str__           return human readable output of the object
# __len__           return the lentgh of the container
#                       called when we use "len()" on instance object 
# --------------------------------------------------------------------


class MySkills:

    def __init__(self, name) -> None:
        self.skills = ["html", "css", "js/ts", "java", "python"]
        self.name = "Mohamed"
    
    def __len__(self):
        return len(self.skills)
    
    def __str__(self) -> str:
        return f"my skill are => {self.skills}"



me = MySkills("Obito")

# __len__

# // ديالك class لل len() كتخدم ملي كدير __len__ هاد ال

print(len(me))



# __str__

# // بوحدو كيرجع لينا هاد المخرج التحت class دبا ملي كنطبعو ال
# print(me) # <__main__.MySkills object at 0x0000023A720D69C0>
# // object لل human readable info الوظيفة ديالها انها كترجع ليك str يعني هاد ال
print(me) # my skill are => ['html', 'css', 'js/ts', 'java', 'python']


# __class__

# // كينتمي لاي كلاس instance object اما هادي كتقول ليك هاد ال

print(me.__class__) # <class '__main__.MySkills'>
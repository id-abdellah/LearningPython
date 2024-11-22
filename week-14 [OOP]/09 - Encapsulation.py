#--------------------------------------------------------------------
# ---- Encapsulation ----
# --------------------------------------------------------------------
# 
# Encapsulation
#   - Restrict access to the data stored in attributes and methodes
#
# Public
# Protected
# Private
# --------------------------------------------------------------------



# Public
# public لي درنا لحد الان كيتعتابرو attributes وال methods غاع ال
# كيكونو متاحين لكشي و يمكن تعدل عليهم methods وال attributes ال public بالنسبة لل

class Public:
    def __init__(self, name) -> None:
        self.name = name # public 

pub = Public("Obito")
print(pub.name) # Obito
pub.name = 200
print(pub.name) # 200




# Protected
# subClasses وال class كيكونو متاحين فقط لل methods وال attributes كتعني ان ال protected بالنسبة لل
# ليها access هوما الوحيدين لي عندهم الحق يديرو subClass ديالها وال class يعني فقط ال

# protected بالنسبة لل name convention يعني كاين keywords مكدعمش هاد ال python بالنسبة لل
# وحدة underscore وهو اننا كنسبقو السمية ب

class Protected:
    def __init__(self, name) -> None:
        self._name = name # public
    
pr = Protected("Uchiha")
print(pr._name) # Uchiha
    
# keywords عليها حيت اللغة باقي مكدعم هاد ال access دبا فالبايثون تقد تدير
# protected attributes لي معاك بلي هادي developers انك تعلم ال underscore يعني الغرض من ال




# Private
# ديالها class لي كتكون متاحة فقط من ال methods او ال attributes هي ال Private ال
# و متقدش تعدل عليها من برا

# ولكن فهاد الحالة اللغة بصح مكتخليكش تاخدها من برا الكلاس ديالها underscores ديالها هو جوج prefixe ال

class Private:

    def __init__(self, name) -> None:
        self.__name = name # Private

    def getName(self):
        return f"Hello Mr. {self.__name}"

priv = Private("Mohamed ID-ABDELLAH")

# print(priv.__name) # AttributeError: 'Private' object has no attribute '__name'

print(priv.getName()) # Hello Mr. Mohamed ID-ABDELLAH

# حقيقي restriction فمكيكون private protected ديال ال keywords كما قلنا اللغة مكدعمش
# نقدو ندخلو ليها ونجيبو قيمتها كما غتشوف لتحت private حيت حتا ديك ال

print(priv._Private__name) # Mohamed ID-ABDELLAH

# // لي كيتعاملو معاها وصاف attr بين المطورين باش يعرفو نوع name convention كيتعتابرو underscores يعني البلان وما فيه ان دوك ال
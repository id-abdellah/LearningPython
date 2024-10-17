# -------------------------------------------
# ---- File Handling ----
# -------------------------------------------
# 
# Mods:
#
# "a" Append    => Open file for appending values, create file if not exist
# "r" Read      => [Default Value] Open file for read. give error if file not existe
# "w" Write     => Open file for writin, Create the file if its not exist
# "x" Create    => Create File. Give error if file already exist
# -------------------------------------------

import os





# ---------------------------------------------------------------------------


# relative path وال absolute path اول حاجة خاص نساليو منها وهي قضية ال

# لي نتا فيه دبا working dire تاال لل root dir لي كيبدا من ال path هو ال absolute path ال
# C:\Users\hp\Desktop\workingDire

# لي نتا خدام فيه دبا working dire لي البداية ديالو كتكون من ال path هو ال relative path اما ال
# cwd يكفي انك دير سمية الملف فقط وهو غينشئ فال relative path فمثلا لبغيتي تنشأ ملف جديد بال


# ---------------------------------------------------------------------------


# ولي يقد يكون موراها شي حرف خاص backslashes غتلقا فيها بزاف جال paths تاني حاجة وهي ملي غتعامل مع ال
# escape character و تعامل معاه اللغة ك انه
# ديالك يخسر path وبالتالي ال

# escape char تعاملات معاها اللغة ك n ديك ال nFiles خاسر حيت ال path المثال التحت
# "C:\Users\hp\Desktop\nFiles"

# فيها مغيخدمش escape char و اي raw str على انها str لل format باش تفادا هاد المشكل خاص ديرك
# r flag عن طريق ال
# r"C:\Users\hp\Desktop\nFiles"


# ---------------------------------------------------------------------------

# وبيها كنتعاملو مع النظام os سميتها module كاينة واحد ال


# لي نتا فيه دبا current working directory هدا كيرد ليك ال

print(os.getcwd()) # D:\programming\VsCode-Workspace\Courses\Python



# لل ملف لي نتا فيه دبا absolute path هدا كيرجع ليك ال

print(os.path.abspath(__file__))
#d:\programming\VsCode-Workspace\Courses\Python\week-9 [Files Handling]\01 - intro.py




# للملف لي نتا فيه او اي ملف abs path هدا كيرد ليك ال المجلد لي نتا فيه دبا. عن طريق ال

print(os.path.dirname(os.path.abspath(__file__)))
# d:\programming\VsCode-Workspace\Courses\Python\week-9 [Files Handling]




# كما كتشوف التحت open() method كنتعاملو معاها بال file handling بالنسبة لل
# absolute path نشئت ملف جديد فالمجلد ديال الدرس الحالي, يعني ستعملت
# pythone لي هو cwd اي كتبت غا السمية ديال الملف غينشئو فال relative path كون درت غا


myFile = open(f"{os.path.dirname(os.path.abspath(__file__))}\obito.txt", "x")
myFile = open(fr"{os.path.dirname(os.path.abspath(__file__))}\02 - reade files.py", "x")
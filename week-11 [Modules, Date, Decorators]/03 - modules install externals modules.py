# ---------------------------------------------
# ---- Modules: Install external modules ----
# ---------------------------------------------
# 
# pip => Python Package manager
# ---------------------------------------------

# external modules باش ندخلو js فال npm كيما عندنا
# python فال external modules كندخلو بيها pip كذلك عندنا

# pyfiglet ولوخرا termcolor وحدة سميتها packages دبا مثلا غندخلو جوج

# pip install termcolor
# pip install pyfiglet

# معين version بشي package باش دخل شي

# pip install packageName=1.0.3



import termcolor, pyfiglet

# لي غتعطيها بطريقة زوينة text ال terminal كترسم ليك فال pyfiglet ال
# terminal كتكب بالالوان فال termcolor اما ال

print(pyfiglet.figlet_format("Obito Uchiha"))
print(termcolor.colored("Mohamed ID-ABDELLAH", color="light_blue"))


print(termcolor.colored(pyfiglet.figlet_format("ID-ABDELLAH"), color="light_blue"))
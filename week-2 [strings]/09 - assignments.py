# --- assignment 1 ---

name = "Mohamed ID-ABDELLAH"
age = 21
country = "Morocco"

print("hello \"{:s}\" your are \"{:d}\" years old, and you live in \"{:s}\"".format(name, age, country))
# hello "Mohamed ID-ABDELLAH" your are "21" years old, and you live in "Morocco"


# --- assignment 2 ---

print(f"""
Hello "{name}".
you are "{age}" years old.
and you live in "{country}"
""")
# Hello "Mohamed ID-ABDELLAH".
# you are "21" years old.
# and you live in "Morocco"


# --- assignment 3 ---

a = "Elzero"

print(f"\
Second letter is: \"{a[1]}\"\n \
Third letter is: \"{a[2]}\"\n \
Third letter is: \"{a[len(a) - 1]}\"\
")

# --- assignment 4 ---

print(f"\
\"{a[1:4]}\"\n\
\"{a[0::2]}\"\n\
")


# --- assignment 5 ---

b = "#@#@Elzero#@#@"

print(b.strip("#@")) # Elzero


# --- assignment 6 ---

c, d, e, f = "1", "11", "111", "1111"

print(f"""
{c.zfill(4)}
{d.zfill(4)}
{e.zfill(4)}
{f.zfill(4)}
""")
# 0001
# 0011
# 0111
# 1111



# --- assignment 7 ---

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@")) # @@@@@@@@@@@@@@@Osama
print(name_two.rjust(20, "@")) # @@@@@@@@Osama_Elzero



# --- assignment 8 ---

aa = "mOhAmEd"
aaa = "MoHaMeD"

print(aa.swapcase()) # MoHaMeD
print(aaa.swapcase()) # mOhAmEd



# --- assignment 9 ---

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love")) # 2



# --- assignment 10 ---

bbb = "Elzero"

print(bbb.find("z"))


# --- assignment 11 ---

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1)) # I Love Python And Although <3 Elzero Web School


# --- assignment 12 ---

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love")) # I Love Python And Although Love Elzero Web School



# --- assignment 13 ---

name = "Osama"
age = 38
country = "Egypt"

print(f"hello my name is: {name}, and my age is: {age}, and i live in {country}")
# hello my name is: Osama, and my age is: 38, and i live in Egypt
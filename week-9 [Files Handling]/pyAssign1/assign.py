import os

# assign 1

currDire = os.path.dirname(os.path.abspath(__file__))

x = 1
while x <= 50:
    txt = open(fr"{currDire}\{f"{x}txt" if x != 25 else f"{x}special-text"}.txt", "w")
    if x != 25:
        txt.write(f"Elzero Web School => {x}\n")
    txt.close()
    x += 1

print(__file__.split("\\")[-1])

print(len(os.listdir(currDire)))


# assign 2

txt1 = open(fr"{currDire}\1txt.txt", "a")

for n in range(1, 51):
    txt1.write("Appended => Elzero web shcool " + str(n) + "\n")
txt1.close()

# assign 3

txt1 = open(fr"{currDire}\1txt.txt", "r")

txt1Content = txt1.readlines()
print("Nnumber of lines =>: ", len(txt1Content))

wordsCount = 0
chars = 0
iCount = 0
for word in " ".join(txt1Content).split(" "):
    if word != "=>" or word.isalpha():
        wordsCount += 1
        chars += len(word)
        iCount += word.count("l")

print("words Count =>", wordsCount)
print("Chars Count =>", chars)
print("alph i count =>", iCount)



# assign 4



for n in range(41, 51):
    os.remove(fr"{currDire}\{n}txt.txt")
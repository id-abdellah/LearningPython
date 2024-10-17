# -----------------------------------------------------------
# ---- Function - Recursion ----
# -----------------------------------------------------------
# 
# -----------------------------------------------------------

# لي كتنادي راسها فالداخل ديالها function معروفة بلي هي ال recursion function ال
# باش تحبس base case وكتعتامد على


# حيت كتنادي راسها فلداخل ديالها recusion دبا الفنكشن التحت كتعتابر


def cleanWord(word):
    if len(word) == 1: return word

    if word[0] == word[1]:
        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])

print(cleanWord("wwwooorrllllldddd"))
print(cleanWord("mmooohhaameeeedd"))


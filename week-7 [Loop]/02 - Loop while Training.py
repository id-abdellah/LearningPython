# ----------------------------------------------------
# ---- While Loop - Training ----
# ----------------------------------------------------
# Simple bookmark manager
# ----------------------------------------------------


favWebsites = []

maximum = 5

while maximum > 0: 
    newWeb = input("Enter ur favourit website 'without https://': ").strip().lower()
    favWebsites.append("https://" + newWeb)
    maximum -= 1
    print(f"https://{newWeb} => successfuly added to ur favourites list")
    print("u have " + str(maximum) + " websites left to add" if maximum != 0 else "bookmark is full")
else:
    print("Bookmark is full. u cant add more")
    print("your bookmark list: ")
    i = 0
    while i < len(favWebsites):
        print(favWebsites[i])
        i += 1
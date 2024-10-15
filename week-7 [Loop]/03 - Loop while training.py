# ----------------------------------------------------
# ---- While Loop - Training ----
# ----------------------------------------------------
# Password guess
# ----------------------------------------------------


mainPassword = "1234"

print("u have 5 chances to guess the password. the password is only integer digits")

tries = 5

inputPass = input("enter ur guess: ")

while tries > 0:
    if inputPass == mainPassword:
        print("winner :)")
        break
    else:
        tries -= 1
        if tries == 0: 
            print("loooser :(")
            break
        print(f"wrong choice u have {tries} left")
        inputPass = input("enter ur new guess: ")

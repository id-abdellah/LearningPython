# ----------------------------------------------------
# ---- Practical Membership Control ----
# ----------------------------------------------------
#
# ----------------------------------------------------


admins = ["Mohamed", "Obito", "Madara"]


# Login

name = input("Please enter your name to login: ").strip().capitalize()


if name in admins:
    print(f"Hi Mr. {name} Welcome Back")
    option = input("U wanna \"Delete\" or \"Update\" your name (d: delete/u: update) ").lower()
    
    if option == "d" or option == "delete":
        admins.remove(name)
        print(f"Successfuly Deleted. Admins List => {admins}")        
    elif option == "u" or option == "update":
        newName = input("Please enter the new name to update: ").strip().capitalize()
        admins[admins.index(name)] = newName
        print(f"Your name is Successful updated into {newName}")
        print(f"Admine List {admins}")
    else : print("Wrong Choice")
else:
    print("sorry you are not admin. but, u wanna be one of the admins?")
    confirmation = input("y/n ").strip().lower()
    
    if confirmation == "y" or confirmation == "yes":
        print("Your name is successfuly added to admins list. u are one of the admins now")
        admins.append(name)
        print(f"Admins List {admins}")
    elif confirmation == "n" or confirmation == "no":
        print("Ok!")
    else:
        print("wrong choice. (y: yes /n: no) only")
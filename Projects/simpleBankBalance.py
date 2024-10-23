from termcolor import colored


def showBalance():
    print(colored(f"Your Bank Balance is: {balance:.2f}$", "light_blue"))

def depositeBalanc(currBalance):
    moneyToDeposite = input("Enter Balance To Deposite: ")
    currBalance += float(moneyToDeposite)
    return currBalance

def withdraw(currBalance):
    moneyToWithdraw = input("Enter a Balance to withdraw: ")
    if currBalance < float(moneyToWithdraw):
        print(colored("Not Enought Balance", "light_red"))
    elif float(moneyToWithdraw) < 0:
        print(colored("Amount must be greater than 0", "light_red"))
    else:
        currBalance -= float(moneyToWithdraw)
    return currBalance

balance = 0

is_running = True


while is_running:
    print(colored("#" * 50, "green"))
    print(colored("Banking Program".center(50, " "), "green"))
    print(colored("#" * 50, "green"))
    print(colored("1. Show Balance", "green"))
    print(colored("2. Deposite", "green"))
    print(colored("3. Withdraw", "green"))
    print(colored("4. Exite", "green"))

    choice = input("Please Enter Your Choice (1-4): ")

    match choice:
        case "1":
            showBalance()
        case "2":
            balance = depositeBalanc(balance)
        case "3":
            balance = withdraw(balance)
        case "4":
            is_running = False
            print(colored("Goodby. See u again :D", "green"))
        case _:
            print(colored("Sorry. Wrong choice", "light_red"))


# assignment 1

# num1 = int(input("first operand: "))
# num2 = int(input("second operand: "))

# operation = input("'+' or '-' or '*' or '%' or '/': ").strip()

# if operation == "+": print(num1 + num2)
# elif operation == "-": print(num1 - num2)
# elif operation == "*": print(num1 * num2)
# elif operation == "/": print(num1 / num2)
# elif operation == "%": print(num1 % num2)



# assignment 2


# age = 15

# print("app is suitable for u" if age > 16 else "app is not")



# assignment 3

# userAge = input("ur age please: ")
# userAge = int(userAge)

# if userAge >= 10 and userAge < 100:
#     inMonths = userAge * 12
#     inWeeks = inMonths * 4
#     inDays = userAge * 365
#     inHours = inDays * 12
#     inMinutes = inHours * 60
#     inSeconds = inMinutes * 60

#     print(f"your age inMonths is: {inMonths:,d}\n\
# your age inWeeks is: {inWeeks:,d}\n\
# your age inDays is: {inDays:,d}\n\
# your age inHours is: {inHours:,d}\n\
# your age inMinutes is: {inMinutes:,d}\n\
# your age inSeconds is: {inSeconds:,d}")
# else:
#     print("invalid")




# assignment 4

country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30


if country in countries:
    print(f"Booyah. u have a {discount} discount. ${price} => ${price - 30}")
else:
    print(f"No. there is no discount for u the price is ${price}")



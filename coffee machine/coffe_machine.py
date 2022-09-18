from main_coffee_menu import menu
from main_coffee_menu import resources
from cake import cake_figure


def left_over_resources():
    resources['water'] = resources['water'] - menu[a]['ingredients']['water']
    resources['milk'] = resources['milk'] - menu[a]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - menu[a]['ingredients']['coffee']

    return resources['water']
    return resources['milk']
    return resources['coffee']


def insert_coins():
    print("Please insert coins")

    quarters = int(input("How many quarters?: "))

    dimes = int(input("How many dimes?: "))

    nickles = int(input("How many nickles?: "))

    pennies = int(input("How many pennies?: "))

    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    for j in menu:
        if choice == j and money < menu[j]['cost']:
            print("Sorry. That is not enough money.")

        elif choice == j and money >= menu[j]['cost']:
            change = round(money - menu[j]['cost'], 2)
            print(f"Here is ${change} change.")
            print(f"Here is your ☕. Enjoy your {j}.")


print(cake_figure)

cont = True
while cont:

    choice = input("What would you like to drink? espresso, latte, cappuccino: ").lower()
    if choice == "off":
        cont = False
    elif choice == "report":
        print(f"Left-over water = {resources['water']}\nLeft-over milk = {resources['milk']}\nLeft-over coffee = {resources['coffee']}")

    for i in menu:
        if choice == i:
            a = i
    if resources['water'] >= menu[a]['ingredients']['water'] and resources['milk'] >= menu[a]['ingredients']['milk'] and \
            resources['coffee'] >= menu[a]['ingredients']['coffee']:
        print(f"Your {a} is ready")
        insert_coins()
        left_over_resources()

    elif resources['coffee'] < menu[a]['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")

    elif resources['water'] < menu[a]['ingredients']['water']:
        print("Sorry, there is not enough water.")

    elif resources['milk'] < menu[a]['ingredients']['milk']:
        print("Sorry, there is not enough water milk.")

















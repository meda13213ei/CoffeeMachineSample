from menu import MENU
from menu import resources


def coffee(variety):
    print("Please insert the coins")
    total = float(input("How many Quarters?: "))*0.25
    total += float(input("How Many Dimes?: "))*0.1
    total += float(input("How Many Nickels?: "))*0.05
    total += float(input("How many pennies?: "))*0.01
    return total


def transaction_success(total, variety):
    if total >= MENU[variety]["cost"]:
        if total > MENU[variety]["cost"]:
            change = round(total - MENU[variety]["cost"], 2)
            print(f"here is {change} in change")
        print(f"here is your {variety} ☕ enjoy")
    if total < MENU[variety]["cost"]:
        print("Sorry That's not enough money. Money refunded")
    return MENU[variety]["cost"]


def update_resource(variety):
    for item in MENU[variety]["ingredients"]:
        resources[item] -= MENU[variety]["ingredients"][item]


def check_resources(variety):
    for item in MENU[variety]["ingredients"]:
        if MENU[variety]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


profit = 0.0
machine_status = "on"
while machine_status == "on":
    user_entry = input("What would you like? (espresso/latte/cappuccino):")
    if user_entry == "espresso" or user_entry == "latte" or user_entry == "cappuccino":
        if check_resources(user_entry):
            update_resource(user_entry)
            profit += transaction_success(coffee(user_entry), user_entry)
    if user_entry == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : ${resources['milk']}ml")
        print(f"coffee : ${resources['coffee']}g")
        print(f"Money : ${profit}")
    if user_entry == "off":
        machine_status = "off"

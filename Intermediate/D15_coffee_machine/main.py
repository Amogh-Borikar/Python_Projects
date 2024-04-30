MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(user):
    for i in MENU[user]["ingredients"]:
        if MENU[user]["ingredients"][i] > resources[i]:
            print(f"Sorry, {i} is not sufficient.")
            return False
        else:
            return True


def process_money():
    print("Please insert coins: ")
    Total_coins = int(input("How many quarters? : ")) * 0.25
    Total_coins += int(input(f"How many dimes? : ")) * 0.1
    Total_coins += int(input(f"How many nickles? : ")) * 0.05
    Total_coins += int(input(f"How many pennies? : ")) * 0.01
    return Total_coins


def transaction_check(process_op, drink_cost):
    if float(process_op) >= float(drink_cost):
        print(f"here is your change : ${round(process_op - drink_cost, 2)}.")
        return True
    else:
        print(f"You are short of : ${drink_cost - process_op} to buy this drink, try again.")
        return False


coffee_machine_on = True
money = 0


while coffee_machine_on:
    print("""

 ██████     ██████     ███████    ███████    ███████    ███████          ███    ███     █████      ██████    ██   ██    ██    ███    ██    ███████ 
██         ██    ██    ██         ██         ██         ██               ████  ████    ██   ██    ██         ██   ██    ██    ████   ██    ██      
██         ██    ██    █████      █████      █████      █████            ██ ████ ██    ███████    ██         ███████    ██    ██ ██  ██    █████   
██         ██    ██    ██         ██         ██         ██               ██  ██  ██    ██   ██    ██         ██   ██    ██    ██  ██ ██    ██      
 ██████     ██████     ██         ██         ███████    ███████          ██      ██    ██   ██     ██████    ██   ██    ██    ██   ████    ███████ 
                                                                                                                                                   
                                                                                                                                                   
                                      
    """)

    user_input = input("What would you like? ☕ espresso / latte / cappuccino: ")
    if user_input == "off":
        coffee_machine_on = False
    elif user_input == "report":
        print(f"Water: {resources["water"]}\n"
              f"Milk: {resources["milk"]}\n"
              f"Coffee: {resources["coffee"]}\n"
              f"Money: ${money}")
    elif user_input == "restock":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    elif (user_input == "espresso" or user_input == "latte" or user_input == "cappuccino") and resources_sufficient(user_input):
        if transaction_check(process_money(), MENU[user_input]["cost"]):
            print(f"Here is your {user_input}, Enjoy! ☕")
            money += MENU[user_input]["cost"]
            for i in MENU[user_input]["ingredients"]:
                resources[i] -= MENU[user_input]["ingredients"][i]
    else:
        coffee_machine_on = False
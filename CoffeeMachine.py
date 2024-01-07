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


is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input('how many quarters?: ')) * 0.25
    total+= int(input('how many dimes?: ')) * 0.1
    total+= int(input('how many nickel?: ')) * 0.05
    total+= int(input('how many pennies?: ')) * 0.01
    return total

def serve(order_ingredients):
    """Serve customer"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

while is_on:
    coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")
    
    if coffee_choice == "off":
        is_on = False

    elif coffee_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif coffee_choice in MENU:
        drinks = MENU[coffee_choice]
        if is_resource_sufficient(drinks['ingredients']):
            payment = round(process_coins(), 2)
            if payment >= drinks['cost']:
                serve(drinks['ingredients'])
                profit += drinks["cost"]
                change = round(payment - drinks["cost"], 2)
                print(f"Enjoy your {coffee_choice}☕. Here's your change ${change}")
            else:
                print(f"Insufficient payment. Here's your refund ${payment}")

    else:
        print('Invalid Input!')

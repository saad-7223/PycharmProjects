menu = {
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
account = 0
machine_on = True

def sufficient_resources(order):
    for source in order:
        if resources[source] >= order[source]:
            continue
        else:
            return source
    else:
        return 'sufficient'

def update_resources(order):
    for source in order:
        dec = resources[source]
        if resources[source] > order[source]:
            resources[source] = dec - order[source]

def put_resource(r):
    update = True
    while update:
        thing = input("Which source you want to update (Water/Coffee/Milk) : ").lower()
        if thing in ['water', 'coffee', 'milk']:
            a = float(input("Enter the quantity to update : "))
            r[thing] = r[thing] + a
        elif thing == 'stop':
            update = False
        else:
            print("Sorry i don not understand ??")


while machine_on:
    item = input("What would you like ? (Espresso/Latte/Cappuccino) : ").lower()

    if item == 'report':
        for k, v in resources.items():
            print(f"{k}\t: {v}")
        print(f"Money\t: {account}")

    elif item == 'off':
        print("Machine Turning off .......")
        machine_on = False

    elif item in ['latte', 'cappuccino', 'espresso']:
        s = sufficient_resources(menu[item]['ingredients'])
        if s == 'sufficient':
            print("Enter the coins")
            d = float(input("How many dimes ? "))
            p = float(input("How many pennies ? "))
            q = float(input("How many quarter ? "))
            n = float(input("How many nickles ? "))
            amt = 0.10*d + 0.01*p + 0.25*q + 0.05*n
            if menu[item]['cost'] < amt:
                update_resources(menu[item]['ingredients'])
                account += menu[item]['cost']
                print(f"The remaining change : {amt-menu[item]['cost']} ")
                print(f"Here is Your drink ... Enjoy !!!")
            else:
                print("The amount is insufficient ..... Here is your remaining coins ")
        else:
            print(f"Sorry {s} is not enough")

    elif item == 'update':
        put_resource(resources)

    else:
        print("We don't sell that !!!! ")
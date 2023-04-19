from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
m = Menu()
cm = CoffeeMaker()
machine_on = True

while machine_on:
    option = m.get_items()
    choice = input(f"What would you like ? ({option}) : ")
    if choice == 'off':
        print("Machine is turning off ......")
        machine_on = False
    elif choice == 'report':
        cm.report()
        mm.report()
    else:
        drink = m.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)

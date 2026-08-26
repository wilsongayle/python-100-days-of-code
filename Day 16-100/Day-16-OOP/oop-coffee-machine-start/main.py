from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def start_coffee_machine():
    """Starts the coffee machine."""
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "report":
            coffee_machine.report()
            money_machine.report()
        elif choice == "off":
            is_on = False
        else:
            drink = menu.find_drink(choice)
            if drink is not None:
                if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)

start_coffee_machine()
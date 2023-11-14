from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create object called my_machine from CoffeeMaker class
my_machine = CoffeeMaker()
# create object called my_menu from Menu class
my_menu = Menu()
# create object called my_till from MoneyMachine class
my_till = MoneyMachine()

# variable to keep track if machine is on
machine_on = True

# continue program until user triggers switch for machine to turn off
while machine_on:
    # check what the user would like to do
    action = input("What would you like to do? Type 'order' to order a drink, 'report' to see the resources, or 'off' "
                   "to turn off the machine.\n").lower()

    if action == 'order':
        # ask user what drink they want and check if it is in the menu
        chosen_drink = input(f"Which drink would you like? ({my_menu.get_items()}): ").lower()
        drink_object = my_menu.find_drink(chosen_drink)
        # if drink is in menu
        if drink_object:
            # check if there's enough resources
            enough_resources = my_machine.is_resource_sufficient(drink_object)
            # if there's enough resources, check price and take payment
            if enough_resources:
                payment = my_till.make_payment(drink_object.cost)
                # if payment went through, make drink
                if payment:
                    my_machine.make_coffee(drink_object)

    elif action == 'report':
        # use report method for my_machine to print on hand ingredients and report method for my_till to print profit
        my_machine.report()
        my_till.report()

    elif action == 'off':
        print("Goodbye")
        machine_on = False

    else:
        print("Sorry that was not an option. Please try again.")

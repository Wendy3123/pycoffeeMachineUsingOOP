from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()


is_on = True

while is_on:
    options = menu.get_items() #    Returns all the names of the available menu items as a concatenated string.
    choice = input(f'What would you like ({options})?: ').lower()
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()   #prints ingredients
        money_machine.report()  #prints money made so far  
    else: 
        drink = menu.find_drink(choice) #Searches the menu for particular drink by name.Returns a MenuItem object if it exists,otherwise returns None.
        if coffee_maker.is_resource_sufficient(drink): #Returns True when drink order can be made, False if ingredients are insufficient.
            if money_machine.make_payment(drink.cost): # ask how many quart,dime,nickel,penny?Returns change when payment accepted & prints money if insufficient.
                coffee_maker.make_coffee(drink)




'''
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import hunter
import shop

class CheeseShop:
    def __init__(self):
        self.cheeses = {"Cheddar": 10, "Marble": 50, "Swiss": 100}
        self.menu = {1: "Buy cheese", 2: "View inventory", 3: "Leave shop"}

    # Retrieves cheese types and their costs
    def get_cheeses(self) -> str:
        keys = list(self.cheeses.keys())
        return f'{keys[0]} - {self.cheeses["Cheddar"]} gold\n{keys[1]} - {self.cheeses["Marble"]} gold\n{keys[2]} - {self.cheeses["Swiss"]} gold'

    # Retrieve the menu
    def get_menu(self) -> str:
        keys = list(self.menu.keys())
        return f'{keys[0]}. {self.menu[1]}\n{keys[1]}. {self.menu[2]}\n{keys[2]}. {self.menu[3]}'

    # Greet players upon entering cheese shop
    def greet(self) -> str:
        return f"Welcome to The Cheese Shop!\n{self.get_cheeses()}"

    # Allows the purchase of cheese and subtracts gold spent from gold the player has
    def buy_cheese(self, gold: int) -> tuple:
        diff = shop.buy_cheese(gold)
        gold -= diff[0]
        return gold, diff[1]

    # Access cheese shop to buy cheese and display inventory
    def move_to(self, player: hunter.Hunter()):
        choice = 0

        while choice != 3:
            print("How can I help ye?")
            print(self.get_menu())
            choice = input()

            # Typecast done only if isdigit() is True. This prevents strings from crashing the program
            if choice.isdigit():
                choice = int(choice)
                # Check that number entered is within range
                if choice < 1 or choice > 3:
                    raise ValueError
            # If user input is not a number
            else:
                print("I did not understand.\n")

            # Buy cheese
            if choice == 1:
                gold = player.get_gold()
                diff = self.buy_cheese(gold)
                player.set_gold(diff[0])
                player.update_cheese(diff[1])
                print()
            # View inventory
            elif choice == 2:
                print(player.display_inventory())
                print()


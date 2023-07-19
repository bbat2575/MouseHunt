'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

def buy_cheese(gold: int) -> tuple:
    # Declare Variables
    sale = ""
    gold_spent = 0
    cheese_bought = 0
    cheese_count = [0, 0, 0]
    
    while True:
        
        print(f"You have {gold} gold to spend.")
        sale = input("State [cheese quantity]: ").lower()
    
        if sale == "back":
            return (gold_spent, tuple(cheese_count))
        
        sale = sale.split(" ")

        # If cheese unknown
        if sale[0] != "cheddar" and sale[0] != "marble" and sale[0] != "swiss":
            print(f"We don't sell {sale[0]}!")
        # If quantity not stated
        elif len(sale) < 2:
            print("Missing quantity.")
        else:
            # try/except statement to prevent sale values such as "cheddar a3/" from crashing the program
            # Note: using sale[1].isdigit() to resolve this also prevents negative numbers from getting through
            try:
                cheese_bought = int(sale[1])
                if sale[0] == "cheddar":
                    gold_used = cheese_bought * CHEESE_MENU[0][1]
                elif sale[0] == "marble":
                    gold_used = cheese_bought * CHEESE_MENU[1][1]
                elif sale[0] == "swiss":
                    gold_used = cheese_bought * CHEESE_MENU[2][1]  
            except ValueError:
                print("Invalid quantity.")
                continue

            if cheese_bought <= 0:
                print("Must purchase positive amount of cheese.")
            elif gold_used > gold:
                print("Insufficient gold.")
            else:
                if sale[0] == "cheddar":
                    gold -= gold_used
                    gold_spent += gold_used
                    cheese_count[0] += cheese_bought
                elif sale[0] == "marble":
                    gold -= gold_used
                    gold_spent += gold_used
                    cheese_count[1] += cheese_bought
                elif sale[0] == "swiss":
                    gold -= gold_used
                    gold_spent += gold_used  
                    cheese_count[2] += cheese_bought
                    
                print(f"Successfully purchase {cheese_bought} {sale[0]}.")


def display_inventory(gold: int, cheese: list, trap: str) -> None:
    print(f"Gold - {gold}")
    print(f"{cheese[0][0]} - {cheese[0][1]}")
    print(f"{cheese[1][0]} - {cheese[1][1]}")
    print(f"{cheese[2][0]} - {cheese[2][1]}")
    print(f"Trap - {trap}")


def main():
    # Declare variables
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    option = 0

    print("Welcome to The Cheese Shop!")
    print("Cheddar - 10 gold")
    print("Marble - 50 gold")
    print("Swiss - 100 gold")

    while option != 3:
        print("\nHow can I help ye?")
        print("1. Buy cheese")
        print("2. View inventory")
        print("3. Leave shop")
        option = input()

        # Typecast done only if isdigit() is True. This prevents strings from crashing the program
        if option.isdigit():
            option = int(option)

        # Buy cheese
        if option == 1:
            diff = buy_cheese(gold)
            gold -= diff[0]
            cheese[0][1] += diff[1][0]
            cheese[1][1] += diff[1][1]
            cheese[2][1] += diff[1][2]
        # View inventory
        elif option == 2:
            display_inventory(gold, cheese, trap)


if __name__ == "__main__":
    main()

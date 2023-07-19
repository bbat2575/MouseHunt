'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import name
import trap

class Hunter:
    def __init__(self):
        self.name = "Bob"
        self.cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
        self.trap = trap.Trap()
        self.gold = 125
        self.points = 0

    def set_name(self, player_name: str):
        if name.is_valid_name(player_name):
            self.name = player_name  
    
    def set_cheese(self, cheese: tuple):
        if type(cheese) == tuple:
            self.cheese[0][1] = cheese[0]
            self.cheese[1][1] = cheese[1]
            self.cheese[2][1] = cheese[2]

    def set_gold(self, gold: int):
        if type(gold) == int:
            self.gold = gold
    
    def set_points(self, points: int):
        if type(points) == int:
            self.points = points

    def get_name(self) -> str:
        return self.name

    def get_cheese(self) -> str:
        return f"{self.cheese[0][0]} - {self.cheese[0][1]}\n{self.cheese[1][0]} - {self.cheese[1][1]}\n{self.cheese[2][0]} - {self.cheese[2][1]}"

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points
    
    def __str__(self) -> str:
        if self.trap.get_one_time_enchantment() == True:
            self.trap.set_one_time_enchantment(self.trap.get_one_time_enchantment())
        return f"Hunter {self.name}\n{self.display_inventory()}"

    # Display user's inventory
    def display_inventory(self) -> str:
        return f"Gold - {self.gold}\n{self.get_cheese()}\nTrap - {self.trap.get_trap_name()}"

    # Take cheese quantities as an argument and update the Hunter's values
    def update_cheese(self, cheese_count: tuple):
        if type(cheese_count) == tuple:
            self.cheese[0][1] += cheese_count[0]
            self.cheese[1][1] += cheese_count[1]
            self.cheese[2][1] += cheese_count[2]
    
    # Update gold by appending amount parsed as argument
    def update_gold(self, loot: int):
        if type(loot) == int:
            self.gold += loot

    # Update points by appending amount parsed as argument
    def update_points(self, loot: int):
        if type(loot) == int:
            self.points += loot

    # Remove one cheese from the cheese type given as an argument
    def consume_cheese(self, cheese_type: str):
        # Check if valid cheese
        i = 0
        while i < len(self.cheese):
            if cheese_type.capitalize() == self.cheese[i][0]:
                # Check if quantity is zero to ensure we don't subtract into the negatives
                if self.cheese[i][1] != 0:
                    self.cheese[i][1] -= 1
                # If it is zero, unarm the trap and change trap cheese to None
                else:
                    self.trap.set_trap_cheese(None)
                break
            i += 1

    # Returns the quantity of a type of cheese that a player has
    def have_cheese(self, cheese_type = "Cheddar") -> int:
        if type(cheese_type) == str and (cheese_type == "Cheddar" or cheese_type == "Marble" or cheese_type == "Swiss"):
            i = 0
            while i < len(self.cheese):
                if cheese_type == self.cheese[i][0]:   
                    return self.cheese[i][1]
                i += 1
        else:
            return 0

    # If cheese is valid we arm the trap with it
    def arm_trap(self, cheese_type: str):
        # Check if valid cheese
        i = 0
        while i < len(self.cheese):
            if cheese_type == self.cheese[i][0]:
                if self.cheese[i][1] == 0:
                    break
                self.trap.set_trap_cheese(cheese_type)
                self.trap.set_arm_status()
                break
            i += 1
        self.trap.set_trap_cheese(None)
    


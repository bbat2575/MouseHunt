'''
The Trap Class
'''

TYPE_OF_TRAP = ("Cardboard and Hook Trap", "High Strain Steel Trap", "Hot Tub Trap")
TYPE_OF_CHEESE = (None, "Cheddar", "Marble", "Swiss")

class Trap:
    def __init__(self):
        self.trap_name = ""
        self.trap_cheese = None
        self.arm_status = False
        self.one_time_enchantment = False

    def set_trap_name(self, name: str):
        if Trap.look_for(name, TYPE_OF_TRAP) == 1:
            self.trap_name = name        
    
    def set_trap_cheese(self, cheese: str):
        if Trap.look_for(cheese, TYPE_OF_CHEESE) == 1:
            self.trap_cheese = cheese

    def set_arm_status(self):
        if Trap.look_for(self.trap_name, TYPE_OF_TRAP) == 1 and Trap.look_for(self.trap_cheese, TYPE_OF_CHEESE) == 1:
            self.arm_status = True
        else:
            self.arm_status = False
    
    def set_one_time_enchantment(self, toggle: bool):
        # Only if trap is not the default trap
        if self.trap_name != "Cardboard and Hook Trap" and toggle == True:
            # Toggle to true
            self.one_time_enchantment = True
            # Update trap name to reflect enchantment
            if self.trap_name.find("One-time Enchanted") == -1:
                self.trap_name = f"One-time Enchanted {self.trap_name}"
            # If enchanted then toggle enchanted to False (has now been used) and update the trap name
        elif self.trap_name != "Cardboard and Hook Trap" and toggle == False:
            self.one_time_enchantment = False
            # Update trap name to reflect disenchantment
            if self.trap_name.find("One-time Enchanted") != -1:
                self.trap_name = self.trap_name.replace("One-time Enchanted ", "")
        else:
            self.one_time_enchantment = False

    def get_trap_name(self) -> str:
        return self.trap_name

    def get_trap_cheese(self) -> str:
        return self.trap_cheese

    def get_arm_status(self) -> bool:
        return self.arm_status

    def get_one_time_enchantment(self) -> bool:
        return self.one_time_enchantment

    def __str__(self) -> str:
        if self.one_time_enchantment:
            self.set_one_time_enchantment(self.one_time_enchantment)
            #return f"One-time Enchanted {self.trap_name}"
        return self.trap_name

    # Provides the benefit of each type of cheese upon enchantment of the trap
    def get_benefit(cheese: str) -> str:
        if cheese == "Cheddar":
            return "+25 points drop by next Brown mouse"
        elif cheese == "Marble":
            return "+25 gold drop by next Brown mouse"
        elif cheese == "Swiss":
            return "+0.25 attraction to Tiny mouse"

    # A static function to search for a target inside a data structure (such as a string inside a tuple)
    def look_for(target: str, structure: tuple) -> int:
        i = 0
        while i < len(structure):
            if target == structure[i]:
                return 1
            i += 1
        return 0


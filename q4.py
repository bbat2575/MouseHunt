'''
Answer for Question 4 - The Training

Name: Bassam Batch
SID: 310229251
unikey: bbat2575

'''

def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    user = input("Press Enter to travel to the Meadow...")

    # Use try/except block to prevent program from crashing
    try:
        if ord(user) == 27: # this ensures ESC+Enter meets the condition
            return ord(user)
    except:
        pass
        
    print("Travelling to the Meadow...")
    print("Larry: This is your camp. Here you'll set up your mouse trap.")

def setup_trap() -> tuple:
    print("Larry: Let's get your first trap...")
    user = input("Press Enter to view traps that Larry is holding...")
    
    # Use try/except block to prevent program from crashing
    try:
        if ord(user) == 27: # this ensures ESC+Enter meets the condition
            return ord(user)
    except:
        pass

    print("Larry is holding...")
    print("Left: High Strain Steel Trap")
    print("Right: Hot Tub Trap")

    user = input('Select a trap by typing "left" or "right": ').lower().strip()

    if user == "left":
        print("Larry: Excellent choice.")
        print('Your "High Strain Steel Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("High Strain Steel Trap", 1)
    elif user == "right":
        print("Larry: Excellent choice.")
        print('Your "Hot Tub Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("Hot Tub Trap", 1)
    else:
        try:
            if ord(user) == 27: # this ensures ESC+Enter meets the condition
                return ord(user)
        except:
            pass

        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        return ("Cardboard and Hook Trap", 0)

    # PASSED THIS POINT THEY HAVE OFFICIALLY SELECTED A TRAP

def sound_horn() -> str:
    print("Sound the horn to call for the mouse...")
    
    user = input('Sound the horn by typing "yes": ').lower().strip()

    try:
        if ord(user) == 27: # this ensures ESC+Enter meets the condition
            return ord(user)
    except:
        pass

    return user

def basic_hunt(cheddar: int, horn_input: str) -> bool:  
    if cheddar and horn_input == "yes":
        print("Caught a Brown mouse!")
        print("Congratulations. Ye have completed the training.")
        end(1)
    else:
        print("Nothing happens.")
        if cheddar or horn_input == "yes":
            print("To catch a mouse, you need both trap and cheese!") 

def end(hunt_status: bool):
    if hunt_status:
        print("Good luck~")

def main():
    intro()
    travel_to_camp()
    has_trap = setup_trap()
    horn_input = sound_horn()
    basic_hunt(has_trap[1], horn_input)

if __name__ == '__main__':
    main()

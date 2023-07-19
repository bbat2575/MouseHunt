'''
The Training

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import training

def training():
    # Intro & Travel to camp
    training.intro()
    has_trap = training.travel_to_camp()
    # Check if ESC+Enter was pressed
    if has_trap ==  27:
        return ("Cardboard and Hook Trap", 0)

    repeat = ""
    while repeat != "no":
        # Select trap
        has_trap = training.setup_trap()
        # Check if ESC+Enter was pressed
        if has_trap == 27:
            return ("Cardboard and Hook Trap", 0)

        # Sound the horn?
        horn_input = training.sound_horn()
        # Check if ESC+Enter was pressed
        if horn_input == 27:
            return ("Cardboard and Hook Trap", 0)

        # Hunt a mouse
        training.basic_hunt(has_trap[1], horn_input)

        # Ask the player if they want to repeat training
        repeat = input('\nPress Enter to continue training and "no" to stop training: ').lower().strip()

        # Check if ESC+Enter was pressed
        # Use try/except block to prevent program from crashing
        try:
            if ord(repeat) == 27:
                return has_trap
        except:
            pass
    
    return has_trap

def main():
    training()

if __name__ == '__main__':
    main()

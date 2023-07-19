'''
Write solutions to 4. New Mouse Release here.

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import mouse

def test01(num_tests):
    i = 0
    while i < num_tests:
        new_mouse = mouse.Mouse()
        if new_mouse.get_name() == None:
            assert new_mouse.get_gold() == 0, "None mouse gold does not equal 0"
            assert new_mouse.get_points() == 0, "None mouse points does not equal 0"
        elif new_mouse.get_name() == "Brown":
            assert new_mouse.get_gold() == 125, "Brown mouse gold does not equal 125"
            assert new_mouse.get_points() == 115, "Brown mouse points does not equal 115"
        elif new_mouse.get_name() == "Field":
            assert new_mouse.get_gold() == 200, "Field mouse gold does not equal 200"
            assert new_mouse.get_points() == 200, "Field mouse points does not equal 200"
        elif new_mouse.get_name() == "Grey":
            assert new_mouse.get_gold() == 125, "Grey mouse gold does not equal 125"
            assert new_mouse.get_points() == 90, "Grey mouse points does not equal 90"
        elif new_mouse.get_name() == "White":
            assert new_mouse.get_gold() == 100, "White mouse gold does not equal 100"
            assert new_mouse.get_points() == 70, "White mouse points does not equal 70"
        elif new_mouse.get_name() == "Tiny":
            assert new_mouse.get_gold() == 900, "Tiny mouse gold does not equal 900"
            assert new_mouse.get_points() == 200, "Tiny mouse points does not equal 200"

        print(f"Test {i+1} Successful:")
        print(f"- {new_mouse.get_name()} awards {new_mouse.get_gold()} gold and {new_mouse.get_points()} points")
        i += 1

test01(100)
    

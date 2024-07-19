from Map import Map
from Wall import Wall
import run





def testcase_1():
    """
    This testcase tests the initial construction of the map, and then adding of walls
    """
    # ------------------- Initialisation ---------------------
    testmap = Map()
    testmap.create_map(3, 5)
    print("Map made with width 3 and height of 5")
    print(testmap.map_state)
    testcase_1_prewall_correct_state = [[None, None, None], [None, None, None], [None, None, None], [None, None, None],
                                        [None, None, None]]

    # testing if initialisation is correct
    assert testmap.map_state == testcase_1_prewall_correct_state, print("Testcase 1 Pre wall adding Failed")
    print("Blank map")
    print(testmap.display_map())
    
# -------------------------- Add Walls ------------------------
    wall1 = Wall(1,1)
    wall2 = Wall(2, 3)
    testmap.add_wall(wall1)
    testmap.add_wall(wall2)
    
# --------------------- print statement --------------------
    print("Map with walls")
    print(testmap.display_map())

    testcase_1_correct_state = [[wall1, None, None], [None, None, None], [None, wall2, None], [None, None, None],
                                [None, None, None]]
    
    assert testmap.map_state == testcase_1_correct_state, print("Testcase 1 Failed")
    
    print("-------------------")
    print("Testcase 1 Passed!")
    print("-------------------")
    
    
def testcase_2():
    """
    testing the functionality of the update map function
    """
    # ------------------- Initialisation ---------------------
    testmap = Map()
    testmap.create_map(3, 5)
    print("Map made with width 3 and height of 5")
    print(testmap.map_state)
    testcase_1_prewall_correct_state = [[None, None, None], [None, None, None], [None, None, None], [None, None, None],
                                        [None, None, None]]
    
    # Adding walls
    wall1 = Wall(1,1)   
    wall2 = Wall(2, 3)
    testmap.add_wall(wall1)
    testmap.add_wall(wall2)
    
# --------------------- print statement --------------------
    print("Map with walls")
    print(testmap.display_map())
    
    
    


if __name__ == '__main__':
    testcase_1()


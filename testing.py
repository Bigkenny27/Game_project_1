from Map import Map
from Wall import Wall
from Player import Hero
import run

def test_add_wall():
    # create variables
    test_map = Map()
    test_map.create_map(3, 3)
    test_wall = Wall(1,1)
    
    try:
        test_map.add_Wall(test_wall)

    except AssertionError:
        print("Failed")
        

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

    # ------------------ Add Player ------------------
    player = Hero("cool")
    player.set_position(1,2)
    testmap.add_hero(player)
    

    # testing if initialisation is correct
    testmap.update_map()
    assert testmap.map_state == testcase_1_prewall_correct_state, print("Testcase 1 Pre wall adding Failed")
    print("Blank map")
    print(testmap.display_map())
    
# -------------------------- Add Walls ------------------------
    wall1 = Wall(1, 1)
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
    
    # Adding walls
    wall1 = Wall(1,1)   
    wall2 = Wall(2, 3)
    testmap.add_wall(wall1)
    testmap.add_wall(wall2)
    print(testmap.display_map())
    
    # Setting up Hero
    player_hero = Hero("hero")
    player_hero.set_position(2,2)
    testmap.add_hero(player_hero)
    print(testmap.display_map())
    

    # Moving
    player_hero.move_right()
    testmap.update_map()
    print(testmap.display_map())
    
    
def main():
    while True:
        print("What testcase would you like to perform? (h) for help (X) to stop")
        wanted_test = input("> ")
        
        if wanted_test == "X":
            break
        
        elif wanted_test == "h":
            print("""
                (1) testcase 1 - construction of map, display_map and add_wall
                (2) testcase 2 - 
                """)

        elif wanted_test == "1":
            testcase_1()
            
        elif wanted_test == "2":
            testcase_2()

    return
    

if __name__ == '__main__':
    main()


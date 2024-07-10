from Map import Map
from Wall import Wall

def map_check(map: Map):
    map.create_map(3, 5)
    print("Map made with width 3 and height of 5")
    print(map.map_state)


def testcase_1():
    # ------------------- Initialisation ---------------------
    testmap = Map()
    map_check(testmap)
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

if __name__ == '__main__':
    testcase_1()


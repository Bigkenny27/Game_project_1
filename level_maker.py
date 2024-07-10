from Wall import Wall
from Map import Map
from Player import Hero

def build_level_test(level_map: Map, hero: Hero):
    
    print("Creating temporary level...")
    level_map.create_map(3, 5)

    print("Adding walls...")
    level_map.add_wall(Wall(1,2))
    level_map.add_wall(Wall(3,2))
    level_map.add_wall(Wall(2,4))
    level_map.add_wall(Wall(3,3))
    hero.set_position(1,1)
    level_map.add_hero(hero)
    return level_map

def find_level(level_id, level_map: Map, Hero: Hero):
    """
    This function will find a specific level

    Args:
        level_id (Any): ID of a level
    """
    if level_id == "test":
        build_level_test(level_map, Hero)
        
    return

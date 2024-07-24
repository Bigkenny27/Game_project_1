import parser
# from Enemy import Enemy
from Player import Hero
from Map import Map
from Wall import Wall
import level_maker


def print_help_list():
    print("""
Commands: 
Movement (m)
....
          
        """)
    return


def player_choices_in_map(input: str, player: Hero):
    """
    This function will check what the input of the player and perform an action based on the input
    Args:
        input (str): player input
    """
    # ---------------- Help -------------------
    if input == "help":
        print_help_list()
    # -------------- Movement -----------------
    elif input == "a":
        player.move_left()
        return
    
    elif input == "d":
        player.move_right()
        return
    
    elif input == "w":
        player.move_up()
        return
    
    elif input == "s":
        player.move_down()
        return
    # -------------- Error --------------------
    else:
        print("")
        
    return
    
    # MOVE TO MAP.PY
# def update_map(level_map: Map):
        
#     # recreate the map
#     map_width = level_map.map_width
#     map_height = level_map.map_height
#     level_map.create_map(map_width, map_height)

    
#     # re-add the walls
#     for i in level_map.list_walls:
#         wall_map_y_pos = i.get_map_y_pos 
#         wall_map_x_pos = i.get_map_x_pos
#         level_map.map_state[wall_map_y_pos][wall_map_x_pos]
        
#     # add the player
#     level_map.add_hero(level_map.hero)
#     return

def in_map_movement(level_map: Map, player: Hero):
    """
    this function will allow for the infinite loop that makes every turn
    
    Args:
        level_map (Map): _description_
        player (Hero): _description_
    """
    in_map = True
    while in_map:
        # Display map
        print(level_map.display_map())
        
        print("what would you like to do")
        player_decision = input("> ")
        player_choices_in_map(player_decision, player)
        # update map
        
        
        

def main():
    """ 
    this function will include character select and stuff 
    but currently only the basics are added

    """
    print("Welcome to the game!")
    # character select and stuff will be here
    print("Select your class")
    hero_class = input("> ")
    player = Hero(hero_class)
    
    # Game Startup
    print("Setting up...")
    
    # make the level
    level_map: Map = Map()
    level_maker.find_level("test", level_map, player)
    print("Displaying map...")
    
    # in map movement
    in_map_movement(level_map, player)
    
    
    


if __name__ == "__main__":
    main()
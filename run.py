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

def player_movement(player: Hero, level_map: Map, direction: str) -> str | None:
    """ 
    This function will move the player and return what action must be taken for the movement
    
    Args:
        player (Hero): Player character
        level_map (Map): the map of the level
        direction (str): direction of movement

    Returns:
        str: Action
    """
    # move the player
    if direction == "a": player.move_left()
    elif direction == "d": player.move_right()
    elif direction == "w": player.move_up()
    elif direction == "s": player.move_down()
    else: assert ValueError("Somehow player_movement has an incorrect direction specified")
    # Check if movement is valid
    
    
    if level_map.check_cell(player.get_x_pos(), player.get_y_pos()) is None:
        return None
    
    
    if level_map.check_cell(player.get_x_pos(), player.get_y_pos()) == "Enemy":
        # TODO:
        pass
    
    
    if isinstance(level_map.check_cell(player.get_x_pos(), player.get_y_pos()), Wall):
        # Send them back
        if direction == "a": player.move_right()
        elif direction == "d": player.move_left()
        elif direction == "w": player.move_down()
        elif direction == "s": player.move_up()
        
        
        # if wall is breakable cause it to break here
        
        return
    
        
    return

def player_choices_in_map(player_input: str, player: Hero, level_map: Map) -> str | None:
    """
    This function will check what the input of the player and perform an action based on the input
    This function can also return a string - repersenting needing a different message displayed.
    Args:
        input (str): player input
    """
    # ---------------- Help -------------------
    if player_input == "help":
        print_help_list()
        
    elif player_input == "Quit":
        raise ValueError("End game")
    # -------------- Movement -----------------
    movement = ["a", "d", "s", "w"]
    if player_input in movement:
        player_movement(player, level_map, player_input)
        
        # inventory function
        
        # afk function
    else:
        return "invalid"
    return
    
    
    
# -------------- Error --------------------

        
    return


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
        action_required = player_choices_in_map(player_decision, player, level_map)
        
        #TODO: somehow get this to replace the default "what do you like to do message"
        if action_required == "invalid":
            print("Invalid action, type 'help' to check list of avaliable actions")
        # isinstance(action_required, None):
        
        # update map
        level_map.update_map()
        
        

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
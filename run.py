import parser
# from Enemy import Enemy
from Player import Hero
from Map import Map
from Wall import Wall
import level_maker

def player_choices_in_map(input: str):
    """
    This function will check what the input of the player and perform an action based on the input
    Args:
        input (str): player input
    """
    
        
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
from Player import Hero
from Wall import Wall


class Map:
    def __init__(self):
        self.hero = None
        self.list_enemies: list = []
        self.list_walls: list = []
        self.list_items: list = []
        self.map_state: list = [] # Height before length
        self.map_width: int = 0
        self.map_height: int = 0



# ------------------ Adding entities -------------------
    #     def add_enemy(self, enemy):
    #         self.list_enemies.append(enemy)
    #
    #     def add_item(self, item):
    #         self.list_items.append(item)

# ------------------- Create Map -------------------
    def create_map(self, width: int, height: int):
        """ 
        Sets the dimentions for a map
        Args:
            width (int): width of the map
            height (int): height of the map
        """
        temp_map = []
        for i in range(height):
            temp_map.append([None] * width)
        self.map_state = temp_map
        
        self.map_width = width
        self.map_height = height
# ------------------- Checks ----------------------
    def is_in_map(self, entity: Hero | Wall) -> bool:
        """
        Checks if the point is inside the map
        :param x_int: x coordinate of the point
        :param y_int: y coordinate of the point
        :return: bool
        """
        
        x_int = entity.get_x_pos()
        y_int = entity.get_y_pos()
        
        # Checks if values are within the lower bound
        if x_int <= 0 or y_int <= 0:
            print(f"{type(entity)} is lower than the lower bounds of the map")
            print(f"{type(entity)} is at ({entity.get_x_pos()}, {entity.get_y_pos()})")
            return False
        
        # Checks if values are within the upper bound
        if x_int > self.map_width or y_int > self.map_height:
            print(f"{type(entity)} is higher than the upper bounds of the map")
            print(f"{type(entity)} is at ({entity.get_x_pos()}, {entity.get_y_pos()})")
            print(f"Map size is {self.map_width}x{self.map_height}")
            return False
        return True

    def check_cell(self, y_pos: int, x_pos: int) -> Hero | Wall | None:
        """ Checks if the cell contains any entities 
        Use the 
        Args:
            y_pos (int):
            x_pos (int): 
        Returns:
            Hero | Wall | None: entity that is occupying the cell
        """
        print(self.map_state)
        return self.map_state[y_pos - 1][x_pos - 1] 
    
    
    # Update Map
    def update_map(self):
            
        # create the map
        height = self.map_height
        width = self.map_width
        
        temp_map = []
        for i in range(height):
            temp_map.append([None] * width)
            
        self.map_state = temp_map
        

        # re-add the walls
        for i in self.list_walls:
            wall_map_y_pos = i.get_map_y_pos() 
            wall_map_x_pos = i.get_map_x_pos()
            
            self.map_state[wall_map_y_pos][wall_map_x_pos] = i
            
        # add the player 
        # for i in self.hero:
        
        self.map_state[self.hero.get_map_y_pos()][self.hero.get_map_x_pos()] = self.hero
            
            
# ------------------- Add Entities ----------------------
    # ALL add commands can be fused in the future

    def add_hero(self, hero: Hero) -> None:
        """
        Parses and adds the Hero to self.hero.
        make sure that hero has a location set
        
        :param hero:
        :return: 
        """
        
        # checks if the values are within the bounds of the map
        if not self.is_in_map(hero):
            return
        
        # check if something is occupying same space
        
        print(hero.get_x_pos())
        print(hero.get_y_pos())
        cell = self.check_cell(hero.get_x_pos(), hero.get_y_pos())
        if cell is not None:
            print(
                f"Cell {hero.get_x_pos}, {hero.get_y_pos}is already occupied by {cell}")
            return
        # Adds the Hero to the Hero list
        self.hero = hero
        
        

    def add_wall(self, wall: Wall) -> None:
        """
        This function parses and adds a wall into maps wall list.
        Args:
            wall (Wall): 
        """
       
        print(f"Wall being added at {wall.get_x_pos() - 1}, {wall.get_y_pos() - 1}")
        
        # Checks if the wall is inside the boundaries of the map
        if not self.is_in_map(wall):
            return

        # Checks if the cell is already occupied by something else
        cell = self.check_cell(wall.get_x_pos(),wall.get_y_pos())
        
        if cell is not None:
            print(f"Cell {wall.get_x_pos}, {wall.get_y_pos}is already occupied by {cell}")
            return

        # add to the lists if all of these pass
        self.list_walls.append(wall)
        self.update_map()
        return

# ------------------- Get Methods ---------------------
    def get_list_enemies(self):
        return self.list_enemies

    def get_list_walls(self):
        return self.list_walls

    def get_list_items(self):
        return self.list_items

    def get_map_state(self):
        return self.map_state

# -----------------------------------------------------
    def display_map(self) -> str:
        """
        Prints the map from the map state.
        NOTE: map_state[height][length]
        NOTE: this command does not compile the entity lists onto the map state.
        :return: str
        """
        
        # update the map
        self.update_map()
         
        # initialise the map variable
        print_map = ""
        # make a new row for each height level
        for i in range(self.map_height):
            new_row = ""
            
            # add the symbols to the new row
            for j in range(self.map_width):
                
                # this makes 1, 1 the bottom left corner
                cell = self.map_state[self.map_height - i - 1][j]

                # if the cell is None, add the placeholder symbol
                if cell is None:
                    new_row += "-"

                # else if the cell contains a entity, add the symbol for the entity
                # ADD NEW CLASSES AFTER ADDING
                elif isinstance(cell, Wall | Hero):
                    new_row += cell.map_symbol

            # Add the rows up to form the full map
            print_map += new_row + "\n"
        return print_map


# ------------------- Main ---------------------
if __name__ == '__main__':
    print("You are running map.py, please run the right file")

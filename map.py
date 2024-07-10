from Player import Hero
from Wall import Wall


class Map:
    def __init__(self):
        self.hero = None
        self.list_enemies: list = []
        self.list_walls: list = []
        self.list_items: list = []
        self.map_state: list = []
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
        temp_map = []
        for i in range(height):
            temp_map.append([None] * width)
        self.map_state = temp_map
        self.map_width = width
        self.map_height = height

# ------------------- Checks ----------------------
    def is_in_map(self, x_int: int, y_int: int) -> bool:
        """
        Checks if the point is inside the map
        :param x_int: x coordinate of the point
        :param y_int: y coordinate of the point
        :return: bool
        """
        # Checks if values are within the lower bound
        if x_int <= 0 or y_int <= 0:
            return False
        # Checks if values are within the upper bound
        if x_int > self.map_width or y_int > self.map_height:
            return False
        return True

    def check_cell(self, x_pos: int, y_pos: int) -> Hero | Wall | None:
        return self.map_state[y_pos - 1][x_pos - 1]
    
# ------------------- Add Hero ----------------------
    # ALL add commands can be fused in the future

    def add_hero(self, hero: Hero) -> None:
        """
        Adds the Hero to the board state.
        :param hero:
        :return: 
        """

        # checks if the values are within the bounds of the map
        if hero.get_x_pos() <= 0 or hero.get_y_pos() <= 0:
            print("Hero is lower than the lower bound of the map"
                  f"Hero is at ({hero.get_x_pos()}, {hero.get_y_pos()})")
            return
        # Checks if values are within the upper bound
        if hero.get_x_pos() > self.map_width or hero.get_y_pos() > self.map_height:
            print("Hero is not within the upper bound of the map"
                  f"Map size is {self.map_width}x{self.map_height}"
                  f"Hero is at ({hero.get_x_pos()}, {hero.get_y_pos()})")
            return

        if self.map_state[hero.get_map_y_pos()][hero.get_map_x_pos()] is not None:
            print(
                f"Cell {hero.get_x_pos}, {hero.get_y_pos}is already occupied by {self.map_state[hero.get_map_y_pos()][hero.get_map_x_pos()]}")
            return
        # Adds the Hero to the Hero list
        self.hero = Hero
        self.map_state[hero.get_map_y_pos()][hero.get_map_x_pos()] = hero

# -------------------- Add Wall -----------------------
    def add_wall(self, wall: Wall) -> None:

        # Checks if values are within the lower bound
        if wall.get_x_pos() <= 0 or wall.get_y_pos() <= 0:
            return
        # Checks if values are within the upper bound
        if wall.get_x_pos() > self.map_width or wall.get_y_pos() > self.map_height:
            return

        # Checks if the cell is already occupied by something else
        if self.map_state[wall.get_map_y_pos()][wall.get_map_x_pos()] is not None:
            print(f"Cell {wall.get_x_pos}, {wall.get_y_pos}is already occupied by {self.map_state[wall.get_map_y_pos()][wall.get_map_x_pos()]}")
            return

        # add to the lists if all of these pass
        self.list_walls.append(wall)

        # add the wall to the map_state
        self.map_state[wall.get_map_y_pos()][wall.get_map_x_pos()] = wall
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
    def print_map(self) -> str:
        """
        Prints the map from the map state.
        NOTE: this command does not compile the entity lists onto the map state.
        :return: str
        """
        # initialise the map variable

        print_map = ""
        # make a new row for each height level
        for i in range(self.map_height):
            new_row = ""

            # add the symbols to the new row
            for j in range(self.map_width):

                # this makes 1, 1 the bottom left corner
                cell = self.map_state[self.map_width - i + 1][j]

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

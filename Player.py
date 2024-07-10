class Hero:
    # ---------------------------- Initialisation -----------------------------
    def __init__(self, hero_class: str, x_pos: int, y_pos: int):

        self.hero_class: str = hero_class
        self.hero_level: int = 1
        self.hero_experience_points = 0
        self.hero_health_points: int = 0
        self.hero_level_up_requirement: int = 0
        self.hero_is_dead: bool = False

        # map stuff
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.map_symbol: str = "H"

    # --------------------------- Movement ----------------------------
    # movement of character by changing the self.hero_location list
    def move_left(self): self.x_pos -= 1
    def move_right(self): self.x_pos += 1
    def move_up(self): self.y_pos += 1
    def move_down(self): self.y_pos -= 1

    # -------------------------- Player Methods -----------------------------
    def level_up(self) -> None:
        self.hero_level += 1
        return

    def gain_experience_points(self, experience_gain: int) -> None:
        # increase the hero's exp points
        self.hero_experience_points += experience_gain
        # if the exp requirement is met, level the player up.
        if self.hero_experience_points >= self.hero_level_up_requirement:
            self.level_up()

    def player_take_damage(self, damage: int) -> None:
        self.hero_health_points -= damage
        return

    def player_check_alive_after_damage(self) -> None:
        """
        Checks if the hero's health is equal or less than zero, if it is, then set hero_is_dead to True
        :return: None
        """
        if self.hero_health_points <= 0:
            print("u dead")  # change this to the game over function
            self.hero_is_dead = True
        return

    # ---------------------- Standard Get Methods --------------------------
    def get_x_pos(self) -> int: return self.x_pos
    def get_y_pos(self) -> int: return self.y_pos
    def get_map_symbol(self) -> str: return self.map_symbol
    def get_player_class(self) -> str: return self.hero_class
    def get_player_level(self) -> int: return self.hero_level
    def get_player_experience_points(self) -> int: return self.hero_experience_points
    def get_player_health_points(self) -> int: return self.hero_health_points

    # ---------------------- Complex Get Methods --------------------------
    def get_map_x_pos(self) -> int:
        """
        This function is used to return the x position indexed on the map
        :return: x_pos - 1
        """
        return self.x_pos - 1

    def get_map_y_pos(self) -> int:
        """
        This function is used to return the y position indexed on the map
        :return: y_pos - 1
        """
        return self.y_pos - 1


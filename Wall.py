class Wall:
    def __init__(self, x_pos: int, y_pos:int):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.object_type = "Wall"
        self.map_symbol = "#"

# ------------- Methods --------------
    def get_x_pos(self) -> int:
        return self.x_pos

    def get_y_pos(self) -> int:
        return self.y_pos

    def get_map_x_pos(self):
        """
        This function is used to return the x position indexed on the map
        :return: x_pos - 1
        """
        return self.x_pos - 1

    def get_map_y_pos(self):
        """
        This function is used to return the y position indexed on the map
        :return: y_pos - 1
        """
        return self.y_pos - 1

    def get_object_type(self) -> str:
        return self.object_type


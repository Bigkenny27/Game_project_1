class Spell:

    def __init__(self, title: str, mana_cost: int, damage_type: str, damage: int, spell_range: int):
        self.title: str = title
        self.description: str = "Default description"
        self.mana_cost: int = mana_cost
        self.damage: int = damage

    def set_description(self, description: str):
        """
        This method will set the description of the spell.
        :param description: the description that will be set as the spell description
        """
        self.description = description
        pass

    def get_title(self) -> str:
        """
        This method will return the title of the spell
        :return: the title of the spell
        """
        return self.title

    def get_description(self) -> str:
        """
        This method will return the description of the spell
        :return: the description of the spell
        """
        return self.description

    def get_mana_cost(self) -> int:
        """
        This method will return the mana cost of the spell
        :return: the mana cost of the spell
        """
        return self.mana_cost

    def get_damage(self) -> int:
        """
        This method will return the spell damage
        :return: the spell damage
        """
        return self.damage



    def __str__(self):
        """
        :return: description of the spell, including the Title, Mana cost, Damage, Range and Description
        """
        output = f"""{self.title}, 
        {self.damage}damage {self.mana_cost}mana cost,
        {self.description}
        """
        return output

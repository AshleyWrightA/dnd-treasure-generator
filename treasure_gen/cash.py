# Standard Library
import random
# Local
from treasure_gen.treasure_components import treasure


class Cash(treasure.Treasure):
    """Cash does not have quality and has preset rarity based off its material."""

    TREASURE_FORM = "Cash"

    def __init__(self, players):
        super().__init__()

        self.treasure_form = "Cash"
        self.players = players
        self._cash_material = None
        self._cash_form = None
        self._cash_crafting_material = None

        self._set_cash_material()
        self._set_cash_form()
        self._set_cash_value()
        self._set_cash_name()
        self._set_cash_crafting_material()
        self._set_cash_rarity()
        self._set_cash_weight()

    def __str__(self):
        cash_str = ""
        cash_str += f"Name: {self.name}\n"
        if self._cash_form == "Coins":
            cash_str += f"Divided: {self._get_coins_divided()} per player\n"
        if self._cash_form == "Bar":
            cash_str += f"Crafting Material: {self._cash_crafting_material}\n"
            cash_str += f"Value: {self.value}\n"
            cash_str += f"Weight: {self.weight}\n"
        cash_str += "-" * 40
        return cash_str

    def _set_cash_name(self):
        if self._cash_form == "Coins":
            self.name = str(self.value) + " " + self._cash_material + " " + self._cash_form
        elif self._cash_form == "Bar":
            self.name = str(1) + " " + self._cash_material + " " + self._cash_form

    def _set_cash_material(self):
        self._cash_material = "".join(random.choices(("Copper", "Silver", "Gold"), weights=(50, 40, 10)))

    def _set_cash_form(self):
        self._cash_form = "".join(random.choices(("Coins", "Bar"), weights=(80, 20)))

    def _set_cash_weight(self):
        if self._cash_form == "Bar":
            self.weight = 1

    def _set_cash_value(self):
        """Generates a value based on the form of cash. Coins will always be evenly dividable amongst players.
        Returns an int."""
        if self._cash_form == "Bar":
            self.value = 100

        if self._cash_form == "Coins":
            result = 1
            if self._cash_material == "Copper":
                while result % self.players != 0:
                    result = random.randint(100, 1000)
            elif self._cash_material == "Silver":
                while result % self.players != 0:
                    result = random.randint(10, 100)
            elif self._cash_material == "Gold":
                while result % self.players != 0:
                    result = random.randint(1, 10)
            self.value = result

    def _set_cash_rarity(self):
        if self._cash_material == "Copper":
            return "Common"
        elif self._cash_material == "Silver":
            return "Uncommon"
        elif self._cash_material == "Gold":
            return "Rare"

    def _set_cash_crafting_material(self):
        if self._cash_form == "Bar":
            self._cash_crafting_material = "Metal"

    def _get_coins_divided(self):
        return self.value // self.players

"""Core functionality shared between different types of treasure."""

# Standard Library
import random
# Third-Party
import dice
# Local
from treasure_gen.treasure_components import quality


class Treasure:

    def __init__(self):
        # All treasure attributes are initialized to None and are then set in the subclasses.
        # Each subclass has a different way of determining the attributes.
        # Each Getter Method gives context to the attributes.

        self.treasure_dict = {}
        self.name = None
        self.crafting_material_1 = None
        self.crafting_material_2 = None
        self.treasure_form = None
        self.value = None
        self.weight = None
        self.appraisal_DC = None
        self.market_limits = None

    def get_dm_treasure_string(self, quality, rarity, treasure_form, market_limits):
        """Treasure properties that the DM should record. Returns a string."""
        if quality == "Normal":
            dm_list = [rarity, treasure_form + ",", market_limits]
        else:
            dm_list = [quality, rarity, treasure_form + ",", market_limits]
        return "DM: [" + " ".join([str(item) for item in dm_list]) + "]"

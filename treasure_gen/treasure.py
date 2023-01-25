# Standard Library
from abc import ABC
import random
# Third-Party
import dice
# Local
from treasure_gen.components import quality


class Treasure(ABC):

    @staticmethod
    def _build_treasure_object(dict_item):
        return random.choice(list(dict_item))

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

    def _appraisal(self, appraisal_dice, appraisal_multiplier_list):
        """Takes a string containing the dice to roll and takes a list of multipliers.
        Returns a sorted list, containing two appraisals of the treasure."""
        appraisals = [self._quality_appraisal(appraisal_dice, appraisal_multiplier_list),
                      self._quality_appraisal(appraisal_dice, appraisal_multiplier_list)]
        appraisals.sort()
        return appraisals

    def _quality_appraisal(self, appraisal_dice, appraisal_multiplier_list):
        """Alter the value if the treasure object has a quality modifier."""
        appraisal = self._base_appraisal(appraisal_dice, appraisal_multiplier_list)
        if self.quality is not None:
            # Half the value
            if self.quality == "Inferior":
                return appraisal // 2
            # Double the value
            elif self.quality == "Superior":
                return appraisal * 2
        return appraisal

    def _base_appraisal(self, appraisal_dice, appraisal_multiplier_list):
        """Generate a value based on the treasure objects dice and value multiplier."""
        # Roll the number of dice and sum them.
        dice_roll = sum(dice.roll(appraisal_dice))
        if self.rarity == "Common":
            return dice_roll * appraisal_multiplier_list[0]
        elif self.rarity == "Uncommon":
            return dice_roll * appraisal_multiplier_list[1]
        elif self.rarity == "Rare":
            return dice_roll * appraisal_multiplier_list[2]
        elif self.rarity == "Very-Rare":
            return dice_roll * appraisal_multiplier_list[3]

    def _set_appraisal_DC(self):
        if self.rarity == "Common":
            self.appraisal_DC = 10
        elif self.rarity == "Uncommon":
            self.appraisal_DC = 15
        elif self.rarity == "Rare":
            self.appraisal_DC = 20
        elif self.rarity == "Very-Rare":
            self.appraisal_DC = 25

    def _get_market_limit_string(self):
        market_limit_string = ""
        temp_list = self.market_limits
        if "Outpost" in temp_list:
            market_limit_string += "O"
        if "Village" in temp_list:
            market_limit_string += "V"
        if "Town" in temp_list:
            market_limit_string += "T"
        if "City" in temp_list:
            market_limit_string += "C"
        return market_limit_string

    def _get_dm_treasure_string(self):
        """A piece of treasures fundamental properties that the DM should record. Returns a string."""
        dm_list = []
        if self.quality is not None:
            dm_list.append(self.quality)
        dm_list.append(self.rarity)
        dm_list.append(self.treasure_form + ",")
        dm_list.append(self._get_market_limit_string())
        return "DM: [" + " ".join([str(item) for item in dm_list]) + "]"


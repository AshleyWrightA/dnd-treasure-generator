# Standard Library
import csv
import random
# Local
from treasure_gen.utilities import *
from treasure_gen.treasure_components.quality import Quality
from treasure_gen.treasure_components.appraisal import Appraisal
from treasure_gen.treasure_components.market_limit import MarketLimit
from treasure_gen.treasure_components.crafting_material import CraftingMaterial

class Gemstone():
    """Gemstones have pre-determined rarities and always have a weight of 1. They always have two crafting materials."""

    TREASURE_FORM = "gemstone"
    GEMSTONE_VALUE_DICE = "3d6"
    GEMSTONE_VALUE_MULTIPLIER = [5, 10, 50, 100]
    GEMSTONE_WEIGHT = 1

    def __init__(self, game_tier_dict):
        super().__init__()

        self.game_tier_dict = game_tier_dict
        self._load_gemstone()

        # Components
        self.quality = Quality().get_random_quality()
        self.name = self.gemstone["Name"]
        self.gemstone_description = self.gemstone["Description"]
        self.rarity = self.gemstone["Rarity"]
        self.appraisal = Appraisal(self.quality, self.rarity, self.GEMSTONE_VALUE_DICE, self.GEMSTONE_VALUE_MULTIPLIER)
        self.weight = self.GEMSTONE_WEIGHT
        self.market_limits = MarketLimit(self.TREASURE_FORM, self.rarity)
        self.crafting_material_1 = CraftingMaterial(self.rarity, self.gemstone["Crafting-Material-1"])
        self.crafting_material_2 = CraftingMaterial(self.rarity, self.gemstone["Crafting-Material-2"])

    def __str__(self):
        gem_str = "-" * 40 +"\n"
        gem_str += f"Gemstone: {self.name}\n"
        gem_str += f"Description: {self.gemstone_description}\n"
        gem_str += f"Rarity: {self.rarity}\n"
        gem_str += f"Weight: {self.weight}\n"
        gem_str += f"Market Limits: {self.market_limits}\n"
        gem_str += f"Crafting Materials: {self.crafting_material_1}, {self.crafting_material_2}\n"
        gem_str += f"Appraisal DC: {self.appraisal.appraisal_DC}\n"
        gem_str += f"Approx Value (Gold): {self.appraisal.appraisal_value}\n"
        gem_str += f"{get_dm_treasure_string(self.quality, self.rarity, self.TREASURE_FORM, self.market_limits)}\n"
        gem_str += "-" * 40
        return gem_str

    def _load_gemstone(self):
        self.gemstone = {}
        with open("treasure_data/Gemstones.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            e = random.choice(list(reader))
            self.gemstone.update(
                {
                    "Name": e["Name"], "Description": e["Description"], "Rarity": e["Rarity"],
                    "Crafting-Material-1": e["Crafting-Material-1"], "Crafting-Material-2": e["Crafting-Material-2"]
                }
            )

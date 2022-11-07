# Standard Library
import csv
# Local
from crafting_material import CraftingMaterial
import treasure


class Gemstone(treasure.Treasure):
    """Gemstones have pre-determined rarities and always have a weight of 1. They have two crafting materials."""

    GEMSTONE_APPRAISAL_DICE = "3d6"
    GEMSTONE_APPRAISAL_MULTIPLIER = [5, 10, 50, 100]
    GEMSTONE_WEIGHT = 1

    def __init__(self):
        super().__init__()

        self.treasure_form = "Gemstone"
        self._set_quality()

        self._load_gemstone_dict()
        self._gemstone = self._build_treasure_object(self.treasure_dict.items())

        self.name = self._gemstone[0]
        self.gemstone_description = self._gemstone[1]["Description"]
        self.rarity = self._gemstone[1]["Rarity"]
        self.value = self._appraisal(self.GEMSTONE_APPRAISAL_DICE, self.GEMSTONE_APPRAISAL_MULTIPLIER)
        self.weight = self.GEMSTONE_WEIGHT
        self._set_appraisal_DC()

        self._set_gemstone_crafting_materials()
        self._set_gemstone_market_limits()

    def __str__(self):
        gem_str = ""
        gem_str += f"{self._get_dm_treasure_string()}\n"
        gem_str += f"Name: {self.name}\n"
        gem_str += f"Description: {self.gemstone_description}\n"
        gem_str += f"Crafting Materials: {self.crafting_material_1}, {self.crafting_material_2}\n"
        gem_str += f"Rarity: {self.crafting_material_1}, {self.crafting_material_2}\n"
        gem_str += f"Weight: {self.weight}\n"
        gem_str += f"Value(Silver): {self.value}\n"
        gem_str += f"Appraisal DC: {self.appraisal_DC}\n"
        gem_str += f"Market Limits: {self.market_limits}\n"
        gem_str += "-" * 40
        return gem_str

    def _set_gemstone_market_limits(self):
        if self.rarity == "Common" or self.rarity == "Uncommon":
            self.market_limits = ["Village", "Town", "City"]
        elif self.rarity == "Rare":
            self.market_limits = ["Town", "City"]
        elif self.rarity == "Very-Rare":
            self.market_limits = ["City"]

    def _load_gemstone_dict(self):
        with open("treasure_gen/Gems.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            for e in reader:
                self.treasure_dict.update(
                    {e["Name"]: {"Description": e["Description"], "Crafting-Material-1": e["Crafting-Material-1"],
                                 "Crafting-Material-2": e["Crafting-Material-2"], "Rarity": e["Rarity"]}}
                )

    def _set_gemstone_crafting_materials(self):
        if len(self._gemstone[1]["Crafting-Material-1"]) != 0:
            self.crafting_material_1 = CraftingMaterial(self.rarity, self._gemstone[1]["Crafting-Material-1"])
        if len(self._gemstone[1]["Crafting-Material-2"]) != 0:
            self.crafting_material_2 = CraftingMaterial(self.rarity, self._gemstone[1]["Crafting-Material-2"])

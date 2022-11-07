import csv

import treasure
from crafting_material import CraftingMaterial


class Trade_Good(treasure.Treasure):
    """Trade Goods have pre-determined rarities & weights. They can have 1 crafting material.
    They also have categories which affect where they can be found. (An ancient dungeon shouldn't contain
    fresh fruit for example)"""

    TRADE_GOOD_DICE = "1d6"
    TRADE_GOOD_MULTIPLIER = [1, 5, 10, 50]

    def __init__(self):
        super().__init__()

        self._set_quality()
        self.treasure_form = "Trade-Good"

        self._load_trade_good_dict()
        self._trade_good = self._build_treasure_object(self.treasure_dict.items())

        self.name = self._trade_good[0]
        self.category = self._trade_good[1]["Category"]
        self.rarity = self._trade_good[1]["Rarity"]
        self.weight = self._trade_good[1]["Weight"]
        self.value = self._appraisal(self.TRADE_GOOD_DICE, self.TRADE_GOOD_MULTIPLIER)

        self._set_trade_good_crafting_materials()
        self._set_trade_good_market_limits()
        self._set_appraisal_DC()

    def __str__(self):
        tg_str = ""
        tg_str += f"{self._get_dm_treasure_string()}\n"
        tg_str += f"Name: {self.name}\n"
        tg_str += f"Category: {self.category}\n"
        tg_str += f"Crafting Material: {self.crafting_material_1}\n"
        tg_str += f"Weight: {self.weight}\n"
        tg_str += f"Value(Silver): {self.value}\n"
        tg_str += f"Appraisal DC: {self.appraisal_DC}\n"
        tg_str += f"Market Limits: {self.market_limits}\n"
        tg_str += "-" * 40
        return tg_str

    def _set_trade_good_market_limits(self):
        if self.rarity == "Common" or self.rarity == "Uncommon":
            self.market_limits = ["Outpost", "Village", "Town", "City"]
        elif self.rarity == "Rare":
            self.market_limits = ["Village", "Town", "City"]
        elif self.rarity == "Very-Rare":
            self.market_limits = ["Town", "City"]

    def _load_trade_good_dict(self):
        with open("treasure_gen/Trade Goods.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            for e in reader:
                self.treasure_dict.update(
                    {e["Name"]: {"Category": e["Category"], "Rarity": e["Rarity"], "Weight": e["Weight"],
                                 "Crafting-Material-1": e["Crafting-Material-1"]}}
                )

    def _set_trade_good_crafting_materials(self):
        if len(self._trade_good[1]["Crafting-Material-1"]) != 0:
            self.crafting_material_1 = CraftingMaterial(self.rarity, self._trade_good[1]["Crafting-Material-1"])

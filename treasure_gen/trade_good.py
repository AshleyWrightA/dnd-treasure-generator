import csv
import random

from treasure_gen.treasure_components.quality import Quality
from treasure_gen.treasure_components.appraisal import Appraisal
from treasure_gen.treasure_components.market_limit import MarketLimit
from treasure_gen.treasure_components.crafting_material import CraftingMaterial
from treasure_gen.utilities import get_dm_treasure_string

class TradeGood:
    """Trade Goods have pre-determined rarities & weights. They can have 1 crafting material.
    They also have categories which affect where they can be found. (An ancient dungeon shouldn't contain
    fresh fruit for example)"""

    TREASURE_FORM = "Trade-Good"
    TRADE_GOOD_VALUE_DICE = "1d6"
    TRADE_GOOD_VALUE_MULTIPLIER = [1, 5, 10, 50]

    def __init__(self, game_tier_dict):
        super().__init__()

        self.game_tier_dict = game_tier_dict
        self.quality = Quality().get_random_quality()
        self._load_trade_good()

        self.name = self.trade_good["Name"]
        self.category = self.trade_good["Category"]
        self.rarity = self.trade_good["Rarity"]
        self.weight = self.trade_good["Weight"]
        self.appraisal = Appraisal(self.quality, self.rarity, self.TRADE_GOOD_VALUE_DICE, self.TRADE_GOOD_VALUE_MULTIPLIER)
        self.market_limits = MarketLimit(self.TREASURE_FORM, self.rarity)
        self._set_trade_good_crafting_materials()

    def __str__(self):
        tg_str = "-"*40+"\n"
        tg_str += f"{self.TREASURE_FORM}\n"
        tg_str += "-"*40+"\n"
        tg_str += f"Name: {self.name}\n"
        tg_str += f"Category: {self.category}\n"
        if hasattr(self, "crafting_material_1"):
            tg_str += f"Crafting Material: {self.crafting_material_1}\n"
        tg_str += f"Rarity: {self.rarity}\n"
        tg_str += f"Weight: {self.weight}\n"
        tg_str += f"Market Limits: {self.market_limits}\n"
        tg_str += f"Appraisal DC: {self.appraisal.appraisal_DC}\n"
        tg_str += f"Approx Value (Gold): {self.appraisal.appraisal_value}\n"
        tg_str += f"{get_dm_treasure_string(self.quality, self.rarity, self.TREASURE_FORM, self.market_limits)}\n"
        tg_str += "-" * 40
        return tg_str

    def _load_trade_good(self):
        self.trade_good = {}
        with open("treasure_data/Trade Goods.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            e = random.choice(list(reader))
            self.trade_good.update({"Name": e["Name"], "Category": e["Category"], "Rarity": e["Rarity"],
                                    "Weight": e["Weight"], "Crafting-Material-1": e["Crafting-Material-1"]})

    def _set_trade_good_crafting_materials(self):
        if len(self.trade_good["Crafting-Material-1"]) != 0:
            self.crafting_material_1 = CraftingMaterial(self.rarity, self.trade_good["Crafting-Material-1"])

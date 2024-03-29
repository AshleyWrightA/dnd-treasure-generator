import csv
import os
import random

from treasure_gen.utilities import *
from treasure_gen.treasure_components.quality import Quality
from treasure_gen.treasure_components.appraisal import Appraisal
from treasure_gen.treasure_components.market_limit import MarketLimit
from treasure_gen.treasure_components.crafting_material import CraftingMaterial


class ArtPiece:
    """Art objects have randomly determined rarities & some art-pieces have variable weight. They can have 1, 2 or no
    crafting materials."""

    TREASURE_FORM = "Art-Piece"
    ART_VALUE_DICE = "3d6"
    ART_VALUE_MULTIPLIER = [10, 50, 100, 500, 1000]

    def __init__(self, rarity):

        self.rarity = rarity
        # Components
        self.quality = Quality().get_random_quality()
        self.appraisal = Appraisal(self.quality, self.rarity, self.ART_VALUE_DICE, self.ART_VALUE_MULTIPLIER)
        self.market_limits = MarketLimit(self.TREASURE_FORM, self.rarity)

        # Data
        self._load_art_piece()
        self._set_art_weight()

        self.name = self.art_piece["Name"]
        self._set_art_piece_crafting_materials()

    def __str__(self):
        art_str = f"-"*40+"\n"
        art_str += f"{self.TREASURE_FORM}\n".capitalize()
        art_str += f"-"*40+"\n"
        art_str += f"Art-Piece: {self.name}\n"
        if self.quality != "Normal":
            art_str += f"Quality: {self.quality}\n"
        art_str += f"Rarity: {self.rarity}\n"
        art_str += f"Weight: {self.weight}lbs\n"
        art_str += f"Market Limits: {self.market_limits}\n"
        if hasattr(self, "crafting_material_2"):
            art_str += f"Crafting Materials: {self.crafting_material_1}, {self.crafting_material_2}\n"
        elif hasattr(self, "crafting_material_1"):
            art_str += f"Crafting Materials: {self.crafting_material_1}\n"
        art_str += f"Appraisal DC: {self.appraisal.appraisal_DC}\n"
        art_str += f"Approx Value (Gold): {self.appraisal.appraisal_value}\n"
        art_str += f"{get_dm_treasure_string(self.quality, self.rarity, self.TREASURE_FORM, self.market_limits)}\n"
        art_str += "-" * 40
        return art_str

    def _set_art_weight(self):
        art_piece_size = [5, 10, 20, 30, 40]
        temp_weight = int(self.art_piece["Weight"])
        if temp_weight == 0:
            self.weight = random.choice(art_piece_size)
        else:
            # Weights in CSV are using SimpleWeight
            self.weight = temp_weight*5

    def _load_art_piece(self):
        with open("treasure_data/Art Pieces.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            art_piece_list = list(reader)
            self.art_piece = get_random_treasure(art_piece_list)

    def _set_art_piece_crafting_materials(self):
        if len(self.art_piece["Crafting-Material-1"]) != 0:
            self.crafting_material_1 = CraftingMaterial(self.rarity, self.art_piece["Crafting-Material-1"])
        if len(self.art_piece["Crafting-Material-2"]) != 0:
            self.crafting_material_2 = CraftingMaterial(self.rarity, self.art_piece["Crafting-Material-2"])

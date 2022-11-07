import csv
import random

from crafting_material import CraftingMaterial
import treasure


class Art(treasure.Treasure):
    """Art objects have randomly determined rarities & some art-pieces have variable weight. They can have 1, 2 or no
    crafting materials."""

    ART_DICE = "3d6"
    ART_MULTIPLIER = [10, 50, 100, 500]

    def __init__(self):
        super().__init__()

        self.treasure_form = "Art-Piece"
        self._set_quality()

        self._load_art_dict()
        self._art_piece = self._build_treasure_object(self.treasure_dict.items())

        self.name = self._art_piece[0]
        self._set_art_rarity()
        self._set_art_weight()
        self.value = self._appraisal(Art.ART_DICE, Art.ART_MULTIPLIER)

        self._set_art_piece_crafting_materials()
        self._set_art_market_limits()
        self._set_appraisal_DC()

    def __str__(self):
        art_str = ""
        art_str += f"{self._get_dm_treasure_string()}\n"
        art_str += f"Name: {self.name}\n"
        art_str += f"Crafting Materials: {self.crafting_material_1}, {self.crafting_material_2}\n"
        art_str += f"Weight: {self.weight}\n"
        art_str += f"Value (Silver): {self.value}\n"
        art_str += f"Appraisal DC: {self.appraisal_DC}\n"
        art_str += f"Market Limits: {self.market_limits}\n"
        art_str += "-" * 40
        return art_str

    def _set_art_market_limits(self):
        if self.rarity == "Common":
            self.market_limits = ["Village", "Town", "City"]
        elif self.rarity == "Uncommon":
            self.market_limits = ["Town", "City"]
        elif self.rarity == "Rare" or "Very-Rare":
            self.market_limits = ["City"]

    def _set_art_rarity(self):
        self.rarity = "".join(random.choices(("Common", "Uncommon", "Rare", "Very-Rare"), weights=(40, 30, 20, 10)))

    def _set_art_weight(self):
        art_piece_weights = ["1 (Tiny)", "2 (Small)", "3 (Medium)", "4 (Big)", "5 (Large)"]
        temp_weight = int(self._art_piece[1]["Weight"])
        if temp_weight == 0:
            temp_weight = random.choice(art_piece_weights)
        self.weight = temp_weight

    def _load_art_dict(self):
        with open("treasure_gen/Art Pieces.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            for e in reader:
                self.treasure_dict.update(
                    {e["Name"]: {"Weight": e["Weight"], "Crafting-Material-1": e["Crafting-Material-1"],
                                 "Crafting-Material-2": e["Crafting-Material-2"]}})

    def _set_art_piece_crafting_materials(self):
        if len(self._art_piece[1]["Crafting-Material-1"]) != 0:
            self.crafting_material_1 = CraftingMaterial(self.rarity, self._art_piece[1]["Crafting-Material-1"])
        if len(self._art_piece[1]["Crafting-Material-2"]) != 0:
            self.crafting_material_2 = CraftingMaterial(self.rarity, self._art_piece[1]["Crafting-Material-2"])

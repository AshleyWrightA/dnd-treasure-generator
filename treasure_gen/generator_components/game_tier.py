import csv

from treasure_gen.utilities import string_to_list
import treasure_gen.treasure_data

class GameTier:

    def __init__(self, party_level):
        self.party_level = party_level
        self._read_game_tier_data()

    def _read_game_tier_data(self):
        self.game_tier_dict = {}
        with open("./treasure_data/GameTier.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            for e in reader:
                if self.party_level in string_to_list(e["Level Range"]):
                    self.game_tier_dict.update(
                        {"Tier": e["Tier"], "Level Range": string_to_list(e["Level Range"]),
                         "Trove Dice": e["Trove Dice"],"Coin Multiplier": e["Coin Multiplier"],
                         "Rarity Weight": string_to_list(e["Rarity Weight"])}
                    )
from csv import DictReader

from treasure_gen.generator_components.game_tier import GameTier
from treasure_gen.utilities import int_string_to_list

class GameState:

    def __init__(self, party_size, party_level):
        self.party_size = party_size
        self.party_level = party_level

        self._load_game_tier_data()

    def _load_game_tier_data(self):
        with open("./treasure_data/GameTier.csv", "r") as input_file:
            reader = DictReader(input_file)
            for e in reader:
                if self.party_level in int_string_to_list(e["Level Range"]):
                    self.game_tier = GameTier(e["Tier"], e["Level Range"], e["Trove Dice"], e["Coin Multiplier"],
                                              e["Rarity Weight"])

    def get_rarity_weight(self):
        return int_string_to_list(self.game_tier.rarity_weight)

    def get_tier(self):
        return self.game_tier.tier
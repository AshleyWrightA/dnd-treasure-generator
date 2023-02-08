import random
class Rarity:

    def __init__(self, rarity=None):
        if rarity is not None:
            self.rarity = rarity

    @staticmethod
    def get_random_rarity(weight_list):
        """Takes an array of five weights to determine rarity. Returns a rarity."""
        return random.choices(("Common", "Uncommon", "Rare", "Very Rare", "Legendary"),
                              weights=(weight_list[0], weight_list[1], weight_list[2], weight_list[3], weight_list[4]))[0]

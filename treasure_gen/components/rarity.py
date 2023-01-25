import random


class RarityFactory:
    """Takes a string and returns a rarity. String is initialized to None in the case a random rarity is needed."""

    def __init__(self, rarity=None):
        if rarity is not None:
            self.rarity = rarity
        else:
            pass

    def get_rarity(self):
        if self.rarity == "Common":
            return Common
        if self.rarity == "Uncommon":
            return Uncommon
        if self.rarity == "Rare":
            return Rare
        if self.rarity == "Very Rare":
            return VeryRare

    @staticmethod
    def get_random_rarity(common_weight, uncommon_weight, rare_weight, very_rare_weight):
        return (random.choices((Common, Uncommon, Rare, VeryRare), weights=(common_weight, uncommon_weight,
                                                                            rare_weight, very_rare_weight)))


class Common:
    def __init__(self):
        self.rarity = "Common"

    def __str__(self):
        strRarity = ""
        strRarity += self.rarity
        return strRarity


class Uncommon:
    def __init__(self):
        self.rarity = "Uncommon"

    def __str__(self):
        strRarity = ""
        strRarity += self.rarity
        return strRarity


class Rare:
    def __init__(self):
        self.rarity = "Rare"

    def __str__(self):
        strRarity = ""
        strRarity += self.rarity
        return strRarity


class VeryRare:
    def __init__(self):
        self.rarity = "Very Rare"

    def __str__(self):
        strRarity = ""
        strRarity += self.rarity
        return strRarity

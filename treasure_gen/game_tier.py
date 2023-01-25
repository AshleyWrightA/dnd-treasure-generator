
class GameTierFactory:
    def __init__(self, game_tier):
        self.game_tier = game_tier

    def get_game_tier(self):
        if self.game_tier == "Apprentice":
            return Apprentice
        if self.game_tier == "Journeyman":
            return Journeyman
        if self.game_tier == "Adventurer":
            return Adventurer
        if self.game_tier == "Veteran":
            return Veteran
        if self.game_tier == "Champion":
            return Champion
        if self.game_tier == "Heroic":
            return Heroic
        if self.game_tier == "Legendary":
            return Legendary


class Apprentice:
    def __init__(self):
        self.level_range = [1, 2]
        self.trove_dice = "2d6"
        self.coin_multiplier = 25


class Journeyman:
    def __init__(self):
        self.level_range = [3, 4, 5]
        self.trove_dice = "3d6"
        self.coin_multiplier = 50


class Adventurer:
    def __init__(self):
        self.level_range = [6, 7, 8]
        self.trove_dice = "3d6"
        self.coin_multiplier = 100


class Veteran:
    def __init__(self):
        self.level_range = [9, 10, 11]
        self.trove_dice = "4d6"
        self.coin_multiplier = 250


class Champion:
    def __init__(self):
        self.level_range = [12, 13, 14]
        self.trove_dice = "4d6"
        self.coin_multiplier = 1000


class Heroic:
    def __init__(self):
        self.level_range = [15, 16, 17]
        self.trove_dice = "5d6"
        self.coin_multiplier = 2500


class Legendary:
    def __init__(self):
        self.level_range = [18, 19, 20]
        self.trove_dice = "5d6"
        self.coin_multiplier = 5000

import dice

import art

class Trove:

    def __init__(self, player_levels):
        self.__player_levels = player_levels
        self.__tier = None
        self.__trove_dice = ["2d6", "3d6", "3d6", "4d6", "4d6"]
        self.__coin_multiplier = [125, 250, 500, 1250, 5000]

    @staticmethod
    def __get_average_player_level(player_levels):
        total = 0
        for e in player_levels:
            total += e
        return total // sum(player_levels)



    def set_trove_tier(self):
        if self.get_average_player_level(self.)
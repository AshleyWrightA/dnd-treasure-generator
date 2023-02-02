import random

import dice

class Appraisal:

    def __init__(self, quality, rarity, value_dice, value_multiplier):
        self.quality = quality
        self.rarity = rarity
        self.value_dice = value_dice
        self.value_multiplier = value_multiplier
        self._get_appraisal()
        self._get_appraisal_DC()

    def _get_appraisal(self):
        """Takes a string containing the dice to roll and takes a list of multipliers.
        Returns a sorted list, containing two appraisals of the treasure."""
        result = dice.roll("1d3")[0]

        # Average Appraisal
        if result == 1:
            self.appraisal_value = self._average_appraisal()

        # Tight Appraisal
        if result == 2:
            self.appraisal_value = self._tight_appraisal()

        # Broad Appraisal
        if result == 3:
            self.appraisal_value = self._broad_appraisal()

    def _average_appraisal(self):
        """Roll 3 times and return the average."""
        appraisal_sum = 0
        appraisal_sum += self._quality_appraisal()
        appraisal_sum += self._quality_appraisal()
        appraisal_sum += self._quality_appraisal()
        return appraisal_sum // 3

    def _tight_appraisal(self):
        """Roll 3 times and only return the highest and lowest."""
        appraisal_range = [self._quality_appraisal(), self._quality_appraisal(), self._quality_appraisal()]
        appraisal_range.sort()
        return [appraisal_range[0], appraisal_range[2]]

    def _broad_appraisal(self):
        """Roll 6 times and only return the highest and lowest"""
        appraisal_range = [self._quality_appraisal(), self._quality_appraisal(), self._quality_appraisal(),
                           self._quality_appraisal(), self._quality_appraisal(), self._quality_appraisal()]
        appraisal_range.sort()
        return [appraisal_range[0], appraisal_range[5]]

    def _quality_appraisal(self):
        """Alter the value if the treasure object has a quality modifier."""
        appraisal = self._base_appraisal()
        if self.quality == "Inferior":
            return appraisal // 2
        # Double the value
        elif self.quality == "Superior":
           return appraisal * 2
        return appraisal

    def _base_appraisal(self):
        """Generate a value based on the treasure objects dice and value multiplier."""
        dice_roll = sum(dice.roll(self.value_dice))
        if self.rarity == "Common":
            return dice_roll * self.value_multiplier[0]
        if self.rarity == "Uncommon":
            return dice_roll * self.value_multiplier[1]
        if self.rarity == "Rare":
            return dice_roll * self.value_multiplier[2]
        if self.rarity == "Very-Rare":
            return dice_roll * self.value_multiplier[3]
        if self.rarity == "Legendary":
           return dice_roll * self.value_multiplier[4]

    def _get_appraisal_DC(self):
        if self.rarity == "Common":
            self.appraisal_DC = 5
        elif self.rarity == "Uncommon":
            self.appraisal_DC = 10
        elif self.rarity == "Rare":
            self.appraisal_DC = 15
        elif self.rarity == "Very Rare":
            self.appraisal_DC = 20
        elif self.rarity == "Legendary":
            self.appraisal_DC = 25


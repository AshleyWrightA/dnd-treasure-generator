from dataclasses import dataclass

@dataclass
class GameTier:

    tier: str
    level_range: list
    trove_dice: str
    coin_multiplier: int
    rarity_weight: list

    def __str__(self):
        return f"{self.tier}, {self.level_range}, {self.trove_dice}, {self.coin_multiplier}, {self.rarity_weight}"

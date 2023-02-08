class MarketLimit:

    def __init__(self, treasure_form, rarity):
        self.treasure_form = treasure_form
        self.rarity = rarity
        self._get_market_limits()

    def __str__(self):
        market_limit_string = ""
        if "Outpost" in self.market_limits:
            market_limit_string += "O"
        if "Village" in self.market_limits:
                market_limit_string += "V"
        if "Town" in self.market_limits:
                market_limit_string += "T"
        if "City" in self.market_limits:
                market_limit_string += "C"
        return market_limit_string

    def _get_market_limits(self):
        if self.treasure_form == "Trade-Good":
            if self.rarity == "Common" or self.rarity == "Uncommon":
                self.market_limits = ["Outpost", "Village", "Town", "City"]
            elif self.rarity == "Rare":
                self.market_limits = ["Village", "Town", "City"]
            elif self.rarity == "Very Rare":
                self.market_limits = ["Town", "City"]
            elif self.rarity == "Legendary":
                self.market_limits = ["City"]

        if self.treasure_form == "gemstone":
            if self.rarity == "Common" or self.rarity == "Uncommon":
                self.market_limits = ["Village", "Town", "City"]
            elif self.rarity == "Rare":
                self.market_limits = ["Town", "City"]
            else:
                self.market_limits = ["City"]

        if self.treasure_form == "Art-Piece":
            if self.rarity == "Common":
                self.market_limits = ["Village", "Town", "City"]
            elif self.rarity == "Uncommon":
                self.market_limits = ["Town", "City"]
            else:
                self.market_limits = ["City"]


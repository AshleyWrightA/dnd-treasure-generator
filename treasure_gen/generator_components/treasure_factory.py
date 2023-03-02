# standard library
import random
# local
from treasure_gen.treasure_objects.art_piece import ArtPiece
from treasure_gen.treasure_objects.cash import Cash
from treasure_gen.treasure_objects.gemstone import Gemstone
from treasure_gen.treasure_objects.trade_good import TradeGood
from treasure_gen.utilities import get_random_rarity

class TreasureFactory:

    def __init__(self, game_state):
        self.game_state = game_state

    def build_treasure(self):
        """Builds and returns one treasure object."""
        # Chooses via a string first to prevent unnecessary object building.
        choice = random.choices(("art_piece", "gemstone", "trade_good", "cash"), weights=(25, 25, 25, 25))[0]
        if choice == "art_piece":
            return self._build_art()
        elif choice == "gemstone":
            return self._build_gemstone()
        elif choice == "trade_good":
            return self._build_trade_good()
        elif choice == "cash":
            return self._build_cash()
    def _build_art(self):
        return ArtPiece(rarity=get_random_rarity(self.game_state.get_rarity_weight()))
    def _build_gemstone(self):
        return Gemstone(rarity=get_random_rarity(self.game_state.get_rarity_weight()))
    def _build_trade_good(self):
        return TradeGood(rarity=get_random_rarity(self.game_state.get_rarity_weight()))
    def _build_cash(self):
        return Cash(self.game_state.party_size)

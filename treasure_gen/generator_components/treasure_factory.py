# standard library
import random
# local
from treasure_gen.art import Art
# import treasure_gen.cash
from treasure_gen.gemstone import Gemstone
from treasure_gen.trade_good import TradeGood


def treasure_factory(party_size, game_tier):
    """Builds and returns one treasure object."""
    # Chooses via a string first to prevent unnecessary object building.
    choice = random.choices(("art-piece", "gemstone", "trade_good"), weights=(33, 33, 33))[0]
    if choice == "art-piece":
        return Art(game_tier)
    elif choice == "gemstone":
        return Gemstone(game_tier)
    elif choice == "trade_good":
        return TradeGood(game_tier)
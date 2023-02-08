# standard library
import random
# local
from treasure_gen.art import Art
# import treasure_gen.cash
from treasure_gen.gemstone import Gemstone
# import treasure_gen.trade_good


def treasure_factory(party_size, game_tier):
    """Builds and returns one treasure object."""
    # Chooses via a string first to prevent unnecessary object building.
    choice = random.choices(("art-piece", "gemstone"), weights=(50, 50))[0]
    if choice == "art-piece":
        return Art(game_tier)
    elif choice == "gemstone":
        return Gemstone(game_tier)
    # return random.choices((art.Art(game_tier), cash.Cash(party_size), gemstone.Gemstone(), trade_good.Trade_Good()), (25,25,25,25) )
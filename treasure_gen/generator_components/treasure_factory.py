# standard library
import random
# local
import treasure_gen.art as art
import treasure_gen.cash as cash
import treasure_gen.gemstone as gemstone
import treasure_gen.trade_good as trade_good


def treasure_factory(party_size, game_tier):
    """Builds and returns one treasure object."""
    # Chooses via a string first to prevent unnecessary object building.
    return art.Art(game_tier)
    # return random.choices((art.Art(game_tier), cash.Cash(party_size), gemstone.Gemstone(), trade_good.Trade_Good()), (25,25,25,25) )
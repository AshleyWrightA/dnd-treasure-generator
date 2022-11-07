# standard library
import random
# local
import art
import cash
import gemstone
import trade_good


def treasure_factory(players):
    """Builds and returns one treasure object."""
    # Chooses via a string first to prevent unnecessary object building.
    dice_roll = random.choice(("Art-Piece", "Cash", "Gemstone", "Trade-Good"))
    if dice_roll == "Art-Piece":
        return print(art.Art())
    elif dice_roll == "Cash":
        return print(cash.Cash(players))
    elif dice_roll == "Gemstone":
        return print(gemstone.Gemstone())
    elif dice_roll == "Trade-Good":
        return print(trade_good.Trade_Good())

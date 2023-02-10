# Standard Library
# Third Party
# Local
from treasure_gen.generator_components.treasure_factory import TreasureFactory
from treasure_gen.generator_components.game_state import GameState
from utilities import get_valid_int


def treasure_gen_mainloop():
    treasure_gen = True

    party_size = get_valid_int("How many party members?: ")
    party_level = get_valid_int("What level (or average level) is the party?: ")
    game_state = GameState(party_size, party_level)

    while treasure_gen:
        print(f"Party of {party_size} at the {game_state.get_tier()} Tier.")
        build_treasure = input("\nBuild treasure? y/n: ").lower()
        if build_treasure == "y":
            print(TreasureFactory(game_state).build_treasure())
        elif build_treasure == "n":
            treasure_gen = False
            print("Goodbye")
        else:
            print("Invalid. You must enter y or n!")




treasure_gen_mainloop()

#TODO
# Gemstones & Trade Goods need to use GameTier rarity weighting.
# Refactor Cash
# Build Trove

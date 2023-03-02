# Standard Library
# Third Party
# Local
from treasure_gen.generator_components.treasure_factory import TreasureFactory
from treasure_gen.generator_components.game_state import GameState
from treasure_gen.generator_components.trove_factory import Trove
from utilities import get_valid_int


def treasure_gen_mainloop():
    treasure_gen = True

    party_size = get_valid_int("How many party members?: ")
    party_level = get_valid_int("What level (or average level) is the party?: ")
    game_state = GameState(party_size, party_level)

    while treasure_gen:
        print(f"Party of {party_size} at the {game_state.get_tier()} Tier.")
        build_treasure = input("\nBuild treasure? (b), Build Trove? (t), Quit? (q): ").lower()
        if build_treasure == "b":
            print(TreasureFactory(game_state).build_treasure())
        elif build_treasure == "t":
            treasure_trove = Trove(game_state)
            treasure_trove.set_trove_allocation()
            treasure_trove.roll_trove_dice()
        elif build_treasure == "q":
            treasure_gen = False
            print("Goodbye")
        else:
            print("Invalid. You must enter b, t or q!")




treasure_gen_mainloop()

#TODO
# Gemstones & Trade Goods need to use GameTier rarity weighting.
# Refactor Cash
# Build Trove

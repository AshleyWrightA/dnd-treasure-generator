# Standard Library
import os
# Third Party
import dice
# Local
from treasure_gen.generator_components.treasure_factory import treasure_factory
from treasure_gen.generator_components.game_tier import GameTier
from utilities import get_valid_int


def treasure_gen_mainloop():
    treasure_gen = True

    party_size = get_valid_int("How many party members?: ")
    party_tier = get_valid_int("What level (or average level) is the party?: ")
    game_tier_dict = GameTier(party_tier).game_tier_dict

    while treasure_gen:
        print(f"Party of {party_size} at the {game_tier_dict.get('Tier')} tier.")
        build_treasure = input("\nBuild treasure? y/n: ").lower()
        if build_treasure == "y":
            print(treasure_factory(party_size, game_tier_dict))
        elif build_treasure == "n":
            treasure_gen = False
            print("Goodbye")
        else:
            print("Invalid. You must enter y or n!")




treasure_gen_mainloop()

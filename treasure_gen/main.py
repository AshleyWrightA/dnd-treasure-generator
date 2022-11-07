# standard library
import os
# local
from treasure_factory import treasure_factory


def treasure_gen_mainloop():
    treasure_gen = True
    players = try_except_int_input("How many players?: ")
    while treasure_gen:
        build_treasure = input("\nBuild treasure? y/n: ").lower()
        if build_treasure == "y":
            os.system("cls")
            treasure_factory(players)
        elif build_treasure == "n":
            treasure_gen = False
            print("Goodbye")
        else:
            print("You must enter y or n!")


def try_except_int_input(str_input):
    try:
        var_input = int(input(str_input))
    except ValueError:
        print("Must be a number!")
        try_except_int_input(str_input)
    else:
        return var_input


treasure_gen_mainloop()

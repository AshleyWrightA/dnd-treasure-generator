import random

def get_valid_int(message):
    int_input = 0
    try:
        int_input = int(input(message))
    except ValueError:
        print("Must be a number!")
        get_valid_int(message)
    else:
        if int_input <= 0:
            print("Must be a positive number!")
            get_valid_int(message)
        else:
            return int_input

def int_string_to_list(_):
    return list(map(int, _.split(",")))

def get_dm_treasure_string(quality, rarity, treasure_form, market_limits):
    """Treasure properties that the DM should record. Returns a string."""
    if quality == "Normal":
        dm_list = [rarity, treasure_form + ",", market_limits]
    else:
        dm_list = [quality, rarity, treasure_form + ",", market_limits]
    return "DM: [" + " ".join([str(item) for item in dm_list]) + "]"

def get_random_treasure(treasure_list):
    return random.choice(treasure_list)

def get_random_rarity(weight_list):
    """Takes an array of five weights to determine rarity. Returns a rarity."""
    return random.choices(("Common", "Uncommon", "Rare", "Very Rare", "Legendary"),
                                 weights=(weight_list[0], weight_list[1], weight_list[2], weight_list[3],
                                          weight_list[4]))[0]
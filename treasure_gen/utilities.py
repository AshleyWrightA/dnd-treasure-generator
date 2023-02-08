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

def string_to_list(_):
    return list(map(int, _.split(",")))

def get_dm_treasure_string(quality, rarity, treasure_form, market_limits):
    """Treasure properties that the DM should record. Returns a string."""
    if quality == "Normal":
        dm_list = [rarity, treasure_form + ",", market_limits]
    else:
        dm_list = [quality, rarity, treasure_form + ",", market_limits]
    return "DM: [" + " ".join([str(item) for item in dm_list]) + "]"
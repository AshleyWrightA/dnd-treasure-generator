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
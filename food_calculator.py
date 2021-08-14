MAX_CAPACITY = 30

def calculate_food(num_small, num_medium, num_large, lbs_surplus):
    if (num_small + num_medium + num_large > MAX_CAPACITY):
        raise Exception("Number of dogs exceeds capacity.")
    if (type(num_small) != int or type(num_medium) != int or type(num_large) != int):
        raise TypeError("Number of dogs must be an integer.")
    if (num_small < 0 or num_medium < 0 or num_large < 0 or lbs_surplus < 0):
        raise Exception("Values entered must be positive.")

    food_amount = (((num_small * 10) + (num_medium * 20) + (num_large * 30)) - lbs_surplus) * 1.2
    if (food_amount < 0):
        return 0
    else:
        return round(food_amount, 2)
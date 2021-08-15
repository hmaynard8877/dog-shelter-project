MAX_CAPACITY = 30

def calculate_food(num_small, num_medium, num_large, lbs_surplus):
    #Check that number of dog values are integers
    if (type(num_small) != int or type(num_medium) != int or type(num_large) != int):
        raise TypeError("Error: Number of dogs must be an integer.")
    #Check that all values are positive
    if (num_small < 0 or num_medium < 0 or num_large < 0 or lbs_surplus < 0):
        raise Exception("Error: Values entered must be positive.")
    #Check that values are not null
    if (num_small is None or num_medium is None or num_large is None or lbs_surplus is None):
        raise Exception("Error: At least one variable is set to None.")
    #Check number of dogs against maximum capacity of shelter
    if (num_small + num_medium + num_large > MAX_CAPACITY):
        raise Exception("Error: Number of dogs exceeds capacity.")

    #Calculate amount of dog food to order for next month
    food_amount = (((num_small * 10) + (num_medium * 20) + (num_large * 30)) - lbs_surplus) * 1.2
    if (food_amount < 0):
        return 0
    else:
        return round(food_amount, 2)
# Dog Shelter Food Calculator
Dog Shelter Food Calculator is a Python program that will calculate the amount of dog food (lbs) to order for the next month. This is determined by the number of small, medium, and large dogs currently in the shelter and the amount of leftover dog food from the previous month.

## Assumptions
- The shelter can hold at most 30 dogs.
- Each small dog requires 10 lbs of food.
- Each medium dog requires 20 lbs of food.
- Each large dog requires 30 lbs of food.
- You need to order 20% more than the minimum needed to feed all dogs currently in the shelter.

## Prerequisites
- Python 3 is installed on the local machine.

## Instructions to run unit tests
In the command prompt, navigate to the directory where test_food_calculator.py is located. Then run the following command:

`py -m unittest -v test_food_calculator.py`

## Files in this project
### `food_calcultor.py`

This file contains one function `calculate_food` that will calculate the amount of dog food needed for the next month.
It accepts four parameters:
- `num_small` - the number of small dogs at the shelter
- `num_medium` - the number of medium dogs at the shelter
- `num_large` - the number of large dogs at the shelter
- `lbs_surplus` - the amount of leftover dog food from the previous month

There are several checks within the function to determine whether the parameters are valid. If any are invalid, an exception will be raised.
- `num_small`, `num_medium`, and `num_large` must be integers.
- `lbs_surplus` must be either an integer or float.
- All parameters must be positive and not null.
- The sum of `num_small`, `sum_medium`, and `sum_large` must not be larger than 30, since that is the maximum number of dogs the shelter can hold.

The function will then calculate the amount of dog food that needs to be ordered for the next month using the given parameters. If the calculated result is negative, that means the shelter already has enough food to cover the next month and will return 0. Othwerise, it will return the calculated value, rounded to two decimal places.

### `program.py`

This file is an example of how a dog shelter might use the `calculate_food` function. It asks for the user's input for the four parameters needed to call the function. If there are any invalid entries, it will ask the user to try again. Once it has the four valid parameters, it will pass them into the `calculate_food` function. Finally, it will tell the user how much dog food they must order for the next month.

### `test_food_calculator.py`

This file contains the unit tests for the `calculate_food` function:
- `test_food_calc` - verify calculator is working with valid inputs
- `test_no_dogs` - if no dogs in the shelter, don't order any food
- `test_no_leftover_food` - verify calculator when there's no leftover food
- `test_max_food_amount` - verify calculator for the maximum amount of food the shelter would need to order
- `test_leftover_surplus` - if leftover food is enough to cover next month, don't order any food
- `test_float_leftover` - verify calculator when leftover value is a float
- `test_max_capacity` - verify exception occurs when there are more than 30 dogs
- `test_value_types` - verify exception occurs when value types are not valid
- `test_positive_values` - verify exception occurs if any value is negative
- `test_values_exist` - verify exception occurs if any value is null

import food_calculator

successful_run = False
while(not successful_run):
    try:
        small_dogs = int(input("How many small dogs are in the shelter? "))
        medium_dogs = int(input("How many medium dogs are in the shelter? "))
        large_dogs = int(input("How many large dogs are in the shelter? "))
        leftover_food = float(input("How many pounds of dog food is left over from last month? "))

        dog_food_ordered = food_calculator.calculate_food(small_dogs, medium_dogs, large_dogs, leftover_food)
        print("You should order " + str(dog_food_ordered) + " lbs of dog food.")
        successful_run = True
    except ValueError:
        print("Value is not valid. Please try again. ")




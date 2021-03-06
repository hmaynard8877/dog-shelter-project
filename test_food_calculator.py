import unittest
import food_calculator

class TestFoodCalculator(unittest.TestCase):
    def test_food_calc(self):
        #Verify calculator gives correct amount of food
        self.assertEqual(food_calculator.calculate_food(5, 3, 7, 17), 363.6)

    def test_no_dogs(self):
        #If no dogs in shelter, don't order any food
        self.assertEqual(food_calculator.calculate_food(0, 0, 0, 14), 0)

    def test_no_leftover_food(self):
        #Verify calculation when there is no leftover food
        self.assertEqual(food_calculator.calculate_food(5, 3, 7, 0), 384)

    def test_max_food_amount(self):
        #Verify maximum amount of food shelter would need
        self.assertEqual(food_calculator.calculate_food(0, 0, 30, 0), 1080)

    def test_leftover_surplus(self):
        #If there's enough leftover food to cover next month, don't order any food
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 100), 0)
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 220), 0)

    def test_float_leftover(self):
        #Verify float value for extra food
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 20.5), 95.4)    

    def test_max_capacity(self): 
        #Verify too many dogs in the shelter raises exception
        with self.assertRaises(Exception):
            food_calculator.calculate_food(10, 10, 11, 10)  

    def test_value_types(self):
        #Verify invalid entry for number of dogs raises exception
        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5.4, 4, 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food("cat", 4, 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(True, 4, 6, 5)
        
        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4.5, 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, "cat", 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, False, 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, 6.5, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, "cat", 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, True, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, 6, "cat")

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, 6, False)

    def test_positive_values(self):
        #Verify negative values raises exception
        with self.assertRaises(Exception):
            food_calculator.calculate_food(-2, 4, 6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, -4, 6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, 4, -6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, 4, 6, -5)

    def test_values_exist(self):
        #Verify None values raises exception
        with self.assertRaises(Exception):
            food_calculator.calculate_food(None, 3, 5, 10)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(3, None, 5, 10)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(3, 3, None, 10)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(3, 3, 5, None)

if __name__ == '__main__':
    unittest.main()
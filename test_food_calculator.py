import unittest
import food_calculator

class TestFoodCalculator(unittest.TestCase):
    def test_food_calc(self):
        #Verify example from assignment instructions
        self.assertEqual(food_calculator.calculate_food(5, 3, 7, 17), 363.6)
        #Verify no dogs in shelter
        self.assertEqual(food_calculator.calculate_food(0, 0, 0, 14), 0)
        #Verify no leftover food
        self.assertEqual(food_calculator.calculate_food(5, 3, 7, 0), 384)
        #Verify maximum amount of food needed for shelter
        self.assertEqual(food_calculator.calculate_food(0, 0, 30, 0), 1080)
        #Verify enough leftover food to cover next month
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 100), 0)
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 220), 0)
        #Verify float value for extra food
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 20.5), 95.4)

        #Verify too many dogs in the shelter raises exception
        with self.assertRaises(Exception):
            food_calculator.calculate_food(10, 10, 11, 10)

        #Verify invalid entry for number of dogs raises exception
        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5.4, 4, 6, 5)
        
        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, "cat", 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, True, 5)

        #Verify negitive values raises exception
        with self.assertRaises(Exception):
            food_calculator.calculate_food(-2, 4, 6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, -4, 6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, 4, -6, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(2, 4, 6, -5)

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
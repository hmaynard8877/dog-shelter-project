import unittest
import food_calculator

class TestFoodCalculator(unittest.TestCase):
    def test_food_calc(self):
        self.assertEqual(food_calculator.calculate_food(5, 3, 7, 17), 363.6)
        self.assertEqual(food_calculator.calculate_food(0, 0, 0, 14), 0)
        self.assertEqual(food_calculator.calculate_food(0, 0, 30, 0), 1080)
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 100), 0)
        self.assertEqual(food_calculator.calculate_food(3, 2, 1, 20.5), 95.4)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(10, 10, 11, 10)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5.4, 4, 6, 5)
        
        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, "cat", 6, 5)

        with self.assertRaises(TypeError):
            food_calculator.calculate_food(5, 4, 6.8, 5)

        with self.assertRaises(Exception):
            food_calculator.calculate_food(0, -4, 6, 5)


if __name__ == '__main__':
    unittest.main()
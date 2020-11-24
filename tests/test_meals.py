import unittest
from src.meals.meals import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_get_meal_by_name(self):
        self.assertGreater(len(self.temp.get_meal_by_name("spaghetti")), 0)

    def test_get_meal_by_name_input_not_str(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_name, 12)

    def test_get_meal_by_first_letter(self):
        self.assertGreater(len(self.temp.get_meal_by_first_letter("a")), 0)

    def test_get_meal_by_first_letter_too_long_input(self):
        self.assertRaises(Exception, self.temp.get_meal_by_first_letter, "ab")

    def test_get_meal_by_first_letter_input_not_str(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_first_letter, 4532+1j)

    def test_get_meal_details_by_id_int_input(self):
        self.assertGreater(len(self.temp.get_meal_details_by_id(52772)), 0)

    def test_get_meal_details_by_id_str_input(self):
        self.assertGreater(len(self.temp.get_meal_details_by_id("52772")), 0)
    
    def test_get_meal_details_by_id_invalid_input(self):
        self.assertRaises(TypeError, self.temp.get_meal_details_by_id, 12321+2j)

    def test_get_random_meal(self):
        self.assertGreater(len(self.temp.get_random_meal()), 0)

    def test_get_meal_categories(self):
        self.assertEqual(len(self.temp.get_meal_categories()["categories"]), 14)

    def test_filter_by_category(self):
        self.assertGreater(len(self.temp.filter_by_category('Seafood')), 0)

    def test_filter_by_category_wrong_input(self):
        self.assertRaises(TypeError, self.temp.filter_by_category, 123124325324)
    
    def test_filter_by_area(self):
        self.assertGreater(len(self.temp.filter_by_area('Canadian')), 0)

    def test_filter_by_area_wrong_input(self):
        self.assertRaises(TypeError, self.temp.filter_by_area, 5432668323)

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()

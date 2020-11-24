import unittest
from src.meals.meals import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_get_meal_by_name(self):
        self.assertGreater(len(self.temp.get_meal_by_name("spaghetti")), 0)

    def test_get_meal_by_first_letter(self):
        self.assertGreater(len(self.temp.get_meal_by_first_letter("a")), 0)

    def test_get_meal_details_by_id(self):
        self.assertGreater(len(self.temp.get_meal_details_by_id(52772)), 0)

    def test_get_random_meal(self):
        self.assertGreater(len(self.temp.get_random_meal()), 0)

    def test_get_meal_categories(self):
        self.assertGreater(len(self.temp.get_meal_categories()), 0)

    def test_filter_by_category(self):
        self.assertGreater(len(self.temp.filter_by_category('Seafood')), 0)
    
    def test_filter_by_area(self):
        self.assertGreater(len(self.temp.filter_by_area('Canadian')), 0)

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()

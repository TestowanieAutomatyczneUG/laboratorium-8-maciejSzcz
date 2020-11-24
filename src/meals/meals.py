import requests

class Meal:
    def get_meal_by_name(self, name):
        return requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}').json()

    def get_meal_by_first_letter(self, letter):
        return requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}').json()
    
    def get_meal_details_by_id(self, id_value):
        return requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id_value}').json()

    def get_random_meal(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()

    def get_meal_categories(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/categories.php').json()

    def filter_by_category(self, category):
        return requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}').json()
    
    def filter_by_area(self, area):
        return requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}').json()

import requests

class Meal:
    def get_meal_by_name(self, name):
        if type(name) != str:
            raise TypeError("Input must be of string type!")

        return requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name}').json()

    def get_meal_by_first_letter(self, letter):
        if len(letter) > 1:
            raise Exception("Input must be a single letter")
        elif type(letter) != str:
            raise TypeError("Input must be of string type!")

        return requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}').json()
    
    def get_meal_details_by_id(self, id_value):
        if type(id_value) != str and type(id_value) != int:
            raise TypeError("Input must be of string or integer type!")

        return requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id_value}').json()

    def get_random_meal(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/random.php').json()

    def get_meal_categories(self):
        return requests.get('https://www.themealdb.com/api/json/v1/1/categories.php').json()

    def filter_by_category(self, category):
        if type(category) != str:
            raise TypeError("Input must be of string type!")

        return requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}').json()
    
    def filter_by_area(self, area):
        if type(area) != str:
            raise TypeError("Input must be of string type!")

        return requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}').json()

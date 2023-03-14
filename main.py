import requests
from pprint import pprint

def recipe_search(ingredient, mealType, health):
    app_id = "c571a1e3"
    app_key = "2a78af3ce15e5e2b04be2768fa646d2d"

    result = requests.get("https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}&health={}".format(ingredient, app_id, app_key, mealType, health))

    data = result.json()
    for result in data['hits']:
        recipe = result['recipe']
        pprint(f"Recipe Title: {recipe['label']}")

        calories = f"calories: {round(recipe['calories'])}"
        protein = round(recipe['totalNutrients']['PROCNT']['quantity'])
        pprint(protein)

        pprint(calories)
        pprint(recipe['url'])

def run():
    ingredient = input('Enter an ingredient: ')
    mealTypeList = ['breakfast', 'lunch', 'dinner']
    mealType = input('Enter meal type(Breakfast, Lunch or Dinner): ')
    if mealType not in mealTypeList:
        pprint(f"wrong fool: {mealType} is not in {mealTypeList})")
        return run()
    health = input('Dietary requirements: ')
    healthList = ['kosher', 'low-sugar', 'gluten-free']
    if health in healthList:
        recipe_search(ingredient, mealType, health)
    else:
        pprint(f"wrong fool: {health} is not in {healthList})")
        return run()

run()


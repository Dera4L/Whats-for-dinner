import random

def decide_dinner(available_ingredients):
    if not available_ingredients:
        return "You don't have any ingredients. Order takeout!"

    possible_meals = {
        "Pasta": ["pasta", "tomato sauce", "cheese", "garlic"],
        "Stir-fry": ["chicken", "vegetables", "soy sauce", "rice"],
        "Sandwich": ["bread", "ham", "cheese", "lettuce", "tomato"],
        "Salad": ["lettuce", "tomato", "cucumber", "dressing"],
    }

    matching_meals = []

    for meal, ingredients in possible_meals.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            matching_meals.append(meal)

    if not matching_meals:
        return "You don't have enough ingredients for any meal. Order takeout!"

    chosen_meal = random.choice(matching_meals)
    return f"Tonight's dinner: {chosen_meal}"

# Example usage:
# ingredients_at_home = ["pasta", "tomato sauce", "cheese", "garlic"]
ingredients_at_home = input('Input dish name and ingredients : ')
print(decide_dinner(ingredients_at_home))

import pandas as pd

# Load recipe data
recipes_df = pd.read_csv('recipe_data.csv')

def recommend_recipes(ingredients):
    ingredients = [ingredient.strip().lower() for ingredient in ingredients]
    recommended = []

    for index, row in recipes_df.iterrows():
        recipe_ingredients = row['ingredients'].lower().split(", ")
        if all(ingredient in recipe_ingredients for ingredient in ingredients):
            recommended.append(row['recipe_name'])

    return recommended

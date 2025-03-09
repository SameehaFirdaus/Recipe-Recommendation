import streamlit as st

# Sample recipe data
recipes = {
    "Chicken Biryani": ["chicken", "basmati rice", "onion", "yogurt", "garlic", "ginger", "spices"],
    "Butter Chicken": ["chicken", "butter", "cream", "tomato puree", "garlic", "ginger", "spices"],
    "Fish Curry": ["fish", "coconut milk", "onion", "tomato", "garlic", "ginger", "curry leaves", "spices"],
    "Mutton Rogan Josh": ["mutton", "yogurt", "onion", "garlic", "ginger", "spices"],
    "Chicken Tikka Masala": ["chicken", "yogurt", "tomato", "cream", "garlic", "ginger", "spices"],
    "Prawn Masala": ["prawns", "onion", "tomato", "coconut milk", "garlic", "ginger", "spices"],
    "Egg Curry": ["eggs", "onion", "tomato", "garlic", "ginger", "spices"],
    "Tandoori Chicken": ["chicken", "yogurt", "lemon juice", "garlic", "ginger", "spices"],
    "Kadai Chicken": ["chicken", "bell pepper", "onion", "tomato", "garlic", "ginger", "spices"],
    "Chettinad Chicken": ["chicken", "coconut", "onion", "tomato", "garlic", "ginger", "spices"],
    "Paneer Tikka": ["paneer", "yogurt", "bell pepper", "onion", "spices"],
    "Hakka Noodles": ["noodles", "chicken", "bell pepper", "soy sauce", "garlic", "ginger", "vegetables"],
    "Samosa": ["potatoes", "peas", "spices", "flour", "oil"],
    "Aloo Tikki": ["potatoes", "peas", "spices", "bread crumbs", "oil"],
    "Chole Bhature": ["chickpeas", "flour", "yogurt", "spices", "onion", "tomato"],
    "Gulab Jamun": ["milk powder", "flour", "sugar", "ghee", "cardamom"],
    "Jalebi": ["maida", "sugar", "yogurt", "saffron", "ghee"],
    "Rasgulla": ["chenna", "sugar", "water", "cardamom"],
    "Kheer": ["rice", "milk", "sugar", "cardamom", "nuts"],
    "Lassi": ["yogurt", "sugar", "water", "cardamom"],
    "Mango Lassi": ["yogurt", "mango", "sugar", "cardamom"],
    "Buttermilk": ["yogurt", "water", "spices", "salt"],
    "Masala Chai": ["tea leaves", "milk", "sugar", "spices"],
    "Coffee": ["coffee powder", "water", "milk", "sugar"],
    "Mojito": ["mint leaves", "lime", "sugar", "soda water"]
}

# Streamlit app
st.title("Recipe Recommendation App")
st.write("Enter at least two ingredients you have:")

# User input for ingredients
user_ingredients = st.text_input("Ingredients (comma-separated):", "")

if user_ingredients:
    # Split the input into a list of ingredients
    user_ingredients_list = [ingredient.strip().lower() for ingredient in user_ingredients.split(",")]

    if len(user_ingredients_list) < 2:
        st.write("Please enter at least two ingredients.")
    else:
        st.write("You have the following ingredients:", user_ingredients_list)

        # Find matching recipes
        matching_recipes = []
        for recipe, ingredients in recipes.items():
            # Check if at least two ingredients match
            if sum(1 for ingredient in user_ingredients_list if ingredient in ingredients) >= 2:
                matching_recipes.append(recipe)

        if matching_recipes:
            st.write("You can make the following recipes:")
            for recipe in matching_recipes:
                st.subheader(recipe)
        else:
            st.write("No recipes found with the provided ingredients.")

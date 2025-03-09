import streamlit as st

# Sample recipe data with instructions
recipes = {
    "Chicken Biryani": {
        "ingredients": ["chicken", "basmati rice", "onion", "yogurt", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with spices, add rice and yogurt, and cook until done."
    },
    "Butter Chicken": {
        "ingredients": ["chicken", "butter", "cream", "tomato puree", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken in butter, add tomato puree and cream, and simmer."
    },
    "Fish Curry": {
        "ingredients": ["fish", "coconut milk", "onion", "tomato", "garlic", "ginger", "curry leaves", "spices"],
        "instructions": "Cook onion and spices, add fish and coconut milk, and simmer."
    },
    "Mutton Rogan Josh": {
        "ingredients": ["mutton", "yogurt", "onion", "garlic", "ginger", "spices"],
        "instructions": "Cook mutton with spices and yogurt until tender."
    },
    "Chicken Tikka Masala": {
        "ingredients": ["chicken", "yogurt", "tomato", "cream", "garlic", "ginger", "spices"],
        "instructions": "Marinate chicken in yogurt, grill, and then cook in a tomato cream sauce."
    },
    "Prawn Masala": {
        "ingredients": ["prawns", "onion", "tomato", "coconut milk", "garlic", "ginger", "spices"],
        "instructions": "Cook prawns with onion, tomato, and spices, then add coconut milk."
    },
    "Egg Curry": {
        "ingredients": ["eggs", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Boil eggs, then cook with onion, tomato, and spices."
    },
    "Tandoori Chicken": {
        "ingredients": ["chicken", "yogurt", "lemon juice", "garlic", "ginger", "spices"],
        "instructions": "Marinate chicken in yogurt, lemon juice, and spices, then grill."
    },
    "Kadai Chicken": {
        "ingredients": ["chicken", "bell pepper", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with bell peppers, onion, and spices."
    },
    "Chettinad Chicken": {
        "ingredients": ["chicken", "coconut", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with coconut and spices."
    },
    "Paneer Tikka": {
        "ingredients": ["paneer", "yogurt", "bell pepper", "onion", "spices"],
        "instructions": "Marinate paneer in yogurt and spices, then grill with vegetables."
    },
    "Hakka Noodles": {
        "ingredients": ["noodles", "chicken", "bell pepper", "soy sauce", "garlic", "ginger", "vegetables"],
        "instructions": "Stir-fry noodles with chicken and vegetables."
    },
    "Samosa": {
        "ingredients": ["potatoes", "peas", "spices", "flour", "oil"],
        "instructions": "Make a filling with potatoes and peas, wrap in dough, and fry."
    },
    "Aloo Tikki": {
        "ingredients": ["potatoes", "peas", "spices", "bread crumbs", "oil"],
        "instructions": "Mash potatoes and peas, form into patties, and fry."
    },
    "Chole Bhature": {
        "ingredients": ["chickpeas", "flour", "yogurt", "spices", "onion", "tomato"],
        "instructions": "Cook chickpeas with spices and serve with fried bread."
    },
    "Gulab Jamun": {
        "ingredients": ["milk powder", "flour", "sugar", "ghee", "cardamom"],
        "instructions": "Make dough, shape into balls, fry, and soak in sugar syrup."
    },
    "Jalebi": {
        "ingredients": ["maida", "sugar", "yogurt", "saffron", "ghee"],
        "instructions": "Make a batter, fry in spiral shapes, and soak in sugar syrup."
    },
    "Rasgulla": {
        "ingredients": ["chenna", "sugar", "water", "cardamom"],
        "instructions": "Make balls from chenna, boil in sugar syrup until spongy."
    },
    "Kheer": {
        "ingredients": ["rice", "milk", "sugar", "cardamom", "nuts"],
        "instructions": "Cook rice in milk, add sugar and cardamom, and garnish with nuts."
    },
    "Lassi": {
        "ingredients": ["yogurt", "sugar", "water", "cardamom"],
        "instructions": "Blend yogurt with sugar and water, and serve chilled."
    },
    "Mango Lassi": {
        "ingredients": ["yogurt", "mango", "sugar", "cardamom"],
        "instructions": "Blend yogurt with mango and sugar until smooth."
    },
        "Buttermilk": {
        "ingredients": ["yogurt", "water", "spices", "salt"],
        "instructions": "Whisk yogurt with water and spices, and serve chilled."
    },
    "Masala Chai": {
        "ingredients": ["tea leaves", "milk", "sugar", "spices"],
        "instructions": "Boil tea leaves with spices, add milk and sugar, and serve hot."
    },
    "Coffee": {
        "ingredients": ["coffee powder", "water", "milk", "sugar"],
        "instructions": "Brew coffee powder with water, add milk and sugar to taste."
    },
    "Mojito": {
        "ingredients": ["mint leaves", "lime", "sugar", "soda water"],
        "instructions": "Muddle mint leaves and lime with sugar, add soda water, and serve chilled."
    }
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
        for recipe, details in recipes.items():
            # Check if at least two ingredients match
            if sum(1 for ingredient in user_ingredients_list if ingredient in details["ingredients"]) >= 2:
                matching_recipes.append(recipe)

        if matching_recipes:
            st.write("You can make the following recipes:")
            for recipe in matching_recipes:
                st.subheader(recipe)

            # If more than two recipes are found, ask the user to select one
            if len(matching_recipes) > 2:
                selected_recipe = st.selectbox("Select a recipe to see its ingredients and instructions:", matching_recipes)
                st.write(f"You selected: **{selected_recipe}**")
                st.write("Ingredients:", recipes[selected_recipe]["ingredients"])
                st.write("Instructions:", recipes[selected_recipe]["instructions"])
            else:
                # If two or fewer recipes are found, display them directly
                for recipe in matching_recipes:
                    st.write(f"**{recipe}**")
                    st.write("Ingredients:", recipes[recipe]["ingredients"])
                    st.write("Instructions:", recipes[recipe]["instructions"])
        else:
            st.write("No recipes found with the provided ingredients.")
